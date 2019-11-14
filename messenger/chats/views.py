from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from chats.models import Chat, Member, Message
from users.models import User
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from chats.forms import * # TODO fix


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


@require_http_methods(["GET"]) # TODO validate
def chats_detail(request, pk):
    chat = Chat.objects.values('is_group_chat', 'topic', 'last_message')
    chat = get_object_or_404(chat, id=pk)
    return JsonResponse({'data': dict(chat)})


@csrf_exempt  # delete later
@require_http_methods(["POST"]) # TODO validate
def create_chat(request):
    form = ChatForm(request)
    if form.is_valid():
        new_chat = form.save()
        new_member = Member.objects.create(user_id=new_chat.user.id, chat_id=new_chat.id, new_messages=0)
        return JsonResponse({'new_chat_id': new_chat.id, 'member_id': new_member.id}, status=201)
    return JsonResponse({}, status=400)

l
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
    member_id = request.POST.get('member_id', False)
    form = MessageForm(request.POST)

    if form.is_valid():
        user = form.cleaned_data['user']
        chat = form.cleaned_data['chat']
        member = get_object_or_404(Member, user_id=user.id, chat_id=chat.id)
        new_message = form.save()
        member.chat.last_message = new_message.id
        member.chat.save()
        member.new_messages = member.new_messages + 1
        member.save()
        return JsonResponse({}, status=201)
    return JsonResponse({}, status=400)


@csrf_exempt
@require_http_methods(["POST"])  # TODO validate
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
