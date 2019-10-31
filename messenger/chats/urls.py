from django.urls import path
from chats.views import home, chats_detail, chats_list

urlpatterns = [
    path('', home, name='chats_home'),
    path('list/', chats_list, name='chats_list'),
    path('detail/<int:pk>/', chats_detail, name='chats_detail')
]
