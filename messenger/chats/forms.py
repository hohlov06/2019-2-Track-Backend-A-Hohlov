from django import forms
from chats.models import Chat, Member, Message, Attachment


def validate_iso8601(str_val):
    try:
        if match_iso8601(str_val) is not None:
            return True
    except ...:
        pass
    return False


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

    # def clean_added_at(self):
    #     added = self.cleaned_data['added_at']
    #     print(added)
    #     if match_iso8601(added):
    #         return added
    #     else:
    #         raise  # TODO


class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = '__all__'


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class GetChatListForm(forms.Form):
    user_id = forms.IntegerField(label="user_id")
    number = forms.IntegerField(label="number", required=False)

    def clean_number(self):
        numb = self.cleaned_data['number']
        if numb is None or numb < 0:
            return 30
        else:
            return numb


class GetMessagesListForm(forms.Form):
    chat_id = forms.IntegerField(label="chat_id")
    number = forms.IntegerField(label="number", required=False)

    def clean_number(self):
        numb = self.cleaned_data['number']
        if numb is None or numb < 0:
            return 30
        else:
            return numb


class ReadMessageForm(forms.Form):
    member_id = forms.IntegerField(label='member_id')
    message_id = forms.IntegerField(label='message_id')
    unread = forms.IntegerField(label='unread', required=False)
