from django.urls import path, re_path
from chats.views import home, chats_detail, chats_list, create_chat

urlpatterns = [
    path('', home, name='chats_home'),
    path('list/<int:user_id>/', chats_list, name='chats_list'),
    path('detail/<int:pk>/', chats_detail, name='chats_detail'),
    re_path(r'^create/.*$', create_chat, name='create_chat'),
]
