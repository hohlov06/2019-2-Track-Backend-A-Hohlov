from django.urls import path, re_path
from chats.views import home, chats_detail, chats_list, create_chat, messages_list, post_message, read_message

urlpatterns = [
    path('', home, name='chats_home'),
    re_path(r'^list$', chats_list, name='chats_list'),
    path('detail/<int:pk>/', chats_detail, name='chats_detail'),
    path('create/', create_chat, name='create_chat'),
    re_path(r'^messages/list$', messages_list, name='messages_list'),
    path('messages/post/', post_message, name='post_message'),
    path('messages/read/', read_message, name='read_message'),
]
