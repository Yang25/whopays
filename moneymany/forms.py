#! -*- encoding: utf-8 -*-

from django import forms
from .models import Message
from django.utils.translation import ugettext_lazy as _

class MessageForm(forms.ModelForm):
    # CharField  : Error message keys: required, max_length, min_length
    # EmailField : Error message keys: required, invalid
    # message = forms.CharField(widget = forms.Textarea)

    name    = forms.CharField(error_messages  = {'required' : 'your name is required','max_length':'too many characters'})
    email   = forms.EmailField(error_messages = {'required': 'your email is required','invalid':'Please enter a valid email address.'})
    message = forms.CharField(widget = forms.Textarea,error_messages  = {'required' : 'the message is required'})
    # name    = forms.CharField(error_messages  = {'required' : '請留下大名','max_length':'字數太多'})
    # email   = forms.EmailField(error_messages = {'required': '請留下信箱','invalid':'信箱格式錯誤'})
    # message = forms.CharField(widget = forms.Textarea,error_messages  = {'required' : '請留下想說的話'})

    class Meta:
        model = Message
        fields = ['name', 'email', 'message']