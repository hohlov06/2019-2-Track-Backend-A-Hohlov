from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["GET", "POST"])
def home(request):
    return render(request, 'chats_home.html')


@require_http_methods(["GET", "POST"])
def chats_list(request):
    return JsonResponse({'chats_list': ['karl', 'klara', 'ukrala', 'koralli']})


@require_http_methods(["GET", "POST"])
def chats_detail(request, pk):
    return JsonResponse({'chat': {'number': pk, 'some_info': 'some additional info'}})
