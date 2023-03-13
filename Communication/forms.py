from django import forms
from .models import Message


class NewMessageForm(forms.ModelForm):
    sender_detail = forms.JSONField(required=False)
    class Meta:
        model = Message
        # fields = '__all__'
        exclude = ('sender_detail',)