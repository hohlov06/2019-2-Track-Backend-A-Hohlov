from django.contrib import admin
from chats.models import Chat, Attachment, Message, Member


class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_group_chat', 'topic', 'last_message')
    list_filter = ('is_group_chat', )


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'chat_id', 'message_id', 'type', 'url')
    list_filter = ('user_id', 'chat_id', 'type')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'chat_id', 'content', 'added_at')
    list_filter = ('user_id', 'chat_id')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'chat_id', 'new_messages', 'last_read_message_id')
    list_filter = ('user_id', 'chat_id')


admin.site.register(Member, MemberAdmin)
admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
