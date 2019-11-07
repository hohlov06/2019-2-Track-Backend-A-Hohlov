from django.contrib import admin
from chats.models import Chat, Attachment, Message, Member


class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_group_chat', 'topic', 'last_message')


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'chat_id', 'message_id', 'type', 'url')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'chat_id', 'content', 'added_at')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'chat_id', 'new_messages', 'last_read_message_id')


admin.site.register(Member, MemberAdmin)
admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
