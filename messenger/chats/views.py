from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from chats.models import Chat, Member, Message
from users.models import User
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


@require_http_methods(["GET", "POST"])
def home(request):
    return render(request, 'chats_home.html')


@require_http_methods(["GET"])
def chats_list(request):
    user_id = request.GET.get('user_id', False)
    number = request.GET.get('number', 30)
    try:
        number = int(number)
    except ...:
        number = 30
    if not user_id:
        return HttpResponseBadRequest  # TODO correct response, user_id presence in DB httpResponse
    # user_member = get_object_or_404(Member, user_id=user_id)
    user_member = Member.objects.select_related('chat').filter(user_id=user_id)
    chats_fields = user_member.values('chat__id', 'chat__is_group_chat', 'chat__topic', 'chat__last_message')
    chats_fields = chats_fields.order_by('-id')[:number]
    return JsonResponse({'data': list(chats_fields)})


@require_http_methods(["GET"])
def chats_detail(request, pk):
    chat = Chat.objects.values('is_group_chat', 'topic', 'last_message')
    chat = get_object_or_404(chat, id=pk)
    return JsonResponse({'data': dict(chat)})


@csrf_exempt  # delete later
@require_http_methods(["POST"])
def create_chat(request):
    user_id = request.POST.get('user_id', False)
    is_group_chat = request.POST.get('is_group_chat', False)
    topic = request.POST.get('topic', 'Default_topic')
    if not user_id:
        return HttpResponseBadRequest  # TODO correct response
    new_chat = Chat.objects.create(is_group_chat=is_group_chat, topic=topic)
    new_member = Member.objects.create(user_id=user_id, chat_id=new_chat.id, new_messages=0)
    return JsonResponse({'new_chat_id': new_chat.id, 'member_id': new_member.id}, status=201)


@require_http_methods(["GET"])
def messages_list(request):
    chat_id = request.GET.get('chat_id', False)
    number = request.GET.get('number', 30)
    try:
        number = int(number)
    except ...:
        number = 30
    if not chat_id:
        return HttpResponseBadRequest  # TODO correct response
    try:
        messages = Message.objects.values('id', 'user_id', 'content', 'added_at').filter(chat_id=chat_id)
        messages = messages.order_by('-id')[:number]
    except Message.DoesNotExist:
        raise Http404
    return JsonResponse({'data': list(messages)})


@csrf_exempt
@require_http_methods(["POST"])
def post_message(request):
    member_id = request.POST.get('member_id', False)
    content = request.POST.get('content')
    added_at = request.POST.get('added_at', False)  # TODO date validation
    if not member_id or not added_at:
        return HttpResponseBadRequest  # TODO correct response, user_id presence in DB httpResponse
    member = get_object_or_404(Member, id=member_id)
    new_message = Message.objects.create(user_id=member.user.id, chat_id=member.chat.id,
                                         content=content, added_at=datetime.now())  # TODO added_at
    member.chat.last_message = new_message.id
    member.chat.save()
    return JsonResponse({}, status=201)


@csrf_exempt
@require_http_methods(["POST"])
def read_message(request):
    member_id = request.POST.get('member_id', False)
    message_id = request.POST.get('message_id', False)
    unread_messages = request.POST.get('unread', -1)
    if not member_id or not message_id:
        return HttpResponseBadRequest  # TODO correct response
    member = get_object_or_404(Member, id=member_id)
    message = get_object_or_404(Message, id=message_id)
    if member.chat.id is not message.chat.id:
        return HttpResponseBadRequest  # TODO correct response
    member.last_read_message = message
    if unread_messages is not -1:
        member.new_messages = unread_messages
    member.save()
    return JsonResponse({}, status=200)
