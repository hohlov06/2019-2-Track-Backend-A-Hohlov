from django.shortcuts import render
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from chats.models import Chat, Member
from users.models import User
from django.views.decorators.csrf import csrf_exempt


@require_http_methods(["GET", "POST"])
def home(request):
    return render(request, 'chats_home.html')


@require_http_methods(["GET"])
def chats_list(request, user_id):
    user_member = Member.objects.select_related('chat').filter(user_id=user_id)
    chats_fields = user_member.values('chat__id', 'chat__is_group_chat', 'chat__topic', 'chat__last_message')
    return JsonResponse({'users': list(chats_fields)})


@require_http_methods(["GET"])
def chats_detail(request, pk):
    chat = Chat.objects.values('is_group_chat', 'topic', 'last_message')
    try:
        chat = chat.get(id=pk)
    except User.DoesNotExist:
        raise Http404
    return JsonResponse({'chat': dict(chat)})


@csrf_exempt  # delete later
@require_http_methods(["POST"])
def create_chat(request):
    user_id = request.POST.get('user_id', False)
    if not user_id:
        return HttpResponseBadRequest
    new_chat = Chat.objects.create(is_group_chat=True, topic='Default topic')
    new_member = Member.objects.create(user_id=user_id, chat_id=new_chat.id, new_messages=0)
    return JsonResponse({'new_chat_id': new_chat.id, 'member_id': new_member.id})
