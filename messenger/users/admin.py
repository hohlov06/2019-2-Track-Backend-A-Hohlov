from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
    list_filter = ('is_superuser', 'is_staff')


admin.site.register(User, UserAdmin)
