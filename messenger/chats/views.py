from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from chats.models import Chat, Member, Message
from users.models import User
from django.views.decorators.csrf import csrf_exempt
from chats.forms import *  # TODO fix


@require_http_methods(["GET", "POST"])
def home(request):
    return render(request, 'chats_home.html')


@require_http_methods(["GET"])
def chats_list(request):
    form = GetChatListForm(request.GET)
    if form.is_valid():
        # user_member = get_object_or_404(Member, user_id=user_id)
        user_member = Member.objects.select_related('chat').filter(user_id=form.cleaned_data['user_id'])
        chats_fields = user_member.values('chat__id', 'chat__is_group_chat', 'chat__topic', 'chat__last_message')
        chats_fields = chats_fields.order_by('-chat__last_message')[:form.cleaned_data['number']]
        return JsonResponse({'data': list(chats_fields)})
    return JsonResponse({}, status=400)


@require_http_methods(["GET"])
def chats_detail(request, pk):
    chat = Chat.objects.values('is_group_chat', 'topic', 'last_message')
    chat = get_object_or_404(chat, id=pk)
    return JsonResponse({'data': dict(chat)})


@csrf_exempt  # delete later
@require_http_methods(["POST"])
def create_chat(request):
    form = ChatForm(request.POST)
    if form.is_valid():
        new_chat = form.save()
        return JsonResponse({'new_chat_id': new_chat.id}, status=201)
    return JsonResponse({}, status=400)


@csrf_exempt  # delete later
@require_http_methods(["POST"])
def create_member(request):
    form = MemberForm(request.POST)
    if form.is_valid():
        chat = form.cleaned_data['chat']
        if Member.objects.filter(chat_id=chat.id, user_id=form.cleaned_data['user'].id).count() > 0:
            return JsonResponse({'message': 'member already exists'}, status=406)
        if not chat.is_group_chat:
            if Member.objects.filter(chat_id=chat.id).count() > 1:
                return JsonResponse({'message': 'group chat can\'t contain more than 2 members'}, status=406)
        new_member = form.save()
        return JsonResponse({'member_id': new_member.id}, status=201)
    return JsonResponse({}, status=400)


@require_http_methods(["GET"])
def messages_list(request):
    form = GetMessagesListForm(request.GET)
    if form.is_valid():
        try:
            messages = Message.objects.values('id', 'user_id', 'content', 'added_at')
            messages = messages.filter(chat_id=form.cleaned_data['chat_id'])
            messages = messages.order_by('-id')[:form.cleaned_data['number']]
        except Message.DoesNotExist:
            raise Http404
        return JsonResponse({'data': list(messages)})
    return JsonResponse({}, status=400)  # TODO status code


@csrf_exempt
@require_http_methods(["POST"])
def post_message(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        user = form.cleaned_data['user']
        chat = form.cleaned_data['chat']
        members = get_list_or_404(Member, chat_id=chat.id)
        new_message = form.save()
        chat.last_message = new_message.id
        chat.save()
        for mem in members:
            if mem.user.id is not user.id:
                mem.new_messages = mem.new_messages + 1
                mem.save()
            else:
                mem.new_messages = 0
                mem.last_read_message = new_message
                mem.save()
        return JsonResponse({}, status=201)
    return JsonResponse({}, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def read_message(request):
    form = ReadMessageForm(request.POST)
    if form.is_valid():
        member = get_object_or_404(Member, id=form.cleaned_data['member_id'])
        message = get_object_or_404(Message, id=form.cleaned_data['message_id'])
        if member.chat.id is not message.chat.id:
            return HttpResponseBadRequest  # TODO correct response
        member.last_read_message = message
        unread = form.cleaned_data['unread']
        if unread is None:
            unread = Message.objects.filter(chat_id=member.chat.id, id__gt=member.last_read_message.id).count()
        member.new_messages = unread
        member.save()
        return JsonResponse({'new_messages': unread}, status=200)
    return JsonResponse({}, status=400)  # todo status code
