from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.views.decorators.http import require_http_methods
from users.models import User


@require_http_methods(["GET", "POST"])
def home(request):
    return render(request, 'users_home.html')


@require_http_methods(["GET"])
def users_list(request):
    all_users = User.objects.values('id', 'username')
    return JsonResponse({'users': list(all_users)})


@require_http_methods(["GET"])
def users_profile(request, pk):
    user = User.objects.values('username', 'first_name', 'last_name', 'email', 'nick', 'avatar')
    try:
        user = user.get(id=pk)
    except User.DoesNotExist:
        raise Http404
    #user = user.values('username', 'first_name', 'last_name', 'email', 'nick', 'avatar')
    return JsonResponse({'user': dict(user)})


# def create_profile():
#     user = User().objects.create(is_superuser=False,
#                                  username='name',
#                                  )