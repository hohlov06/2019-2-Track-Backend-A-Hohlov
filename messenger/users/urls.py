from django.urls import path
from users.views import home, users_list, users_profile

urlpatterns = [
    path('', home, name='users_home'),
    path('list/', users_list, name='users_list'),
    path('profile/<int:pk>/', users_profile, name='users_profile')
]
