# -*- coding: utf-8 -*-
from django import forms
from django.contrib.comments.models import Comment
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):

    user_name = forms.CharField(label=u'Nome')
    user_email = forms.EmailField(label=u'E-mail')
    comment = forms.Field(label=u'Comentário',widget=forms.Textarea)
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ('user_name','user_email','comment','submit_date')
        exclude = "submit_date",

    def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.fields['user_name'].widget.attrs['class'] = 'form-control'
		self.fields['user_email'].widget.attrs['class'] = 'form-control'
		self.fields['comment'].widget.attrs['class'] = 'form-control'		
		self.fields['captcha'].widget.attrs['class'] = 'form-control captcha-input'