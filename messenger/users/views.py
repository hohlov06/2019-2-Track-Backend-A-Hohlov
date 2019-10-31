from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["GET", "POST"])
def home(request):
    return render(request, 'users_home.html')


@require_http_methods(["GET", "POST"])
def users_list(request):
    #return JsonResponse({'resp': str(request.method)})
    return JsonResponse({'users_list': ['first', 'second', 'fifth', 'forth']})


@require_http_methods(["GET", "POST"])
def users_profile(request, pk):
    return JsonResponse({'user': {'number': pk, 'some_info': 'some additional info'}})


