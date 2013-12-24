#coding: utf-8

from django import forms
from django.conf import settings
from django.core.mail import EmailMessage
from captcha.fields import CaptchaField


class ContactForm(forms.Form):

	name = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label='Email')
	phone = forms.CharField(label='Telefone', max_length=20)
	subject = forms.CharField(label='Assunto', max_length=50)
	message = forms.CharField(label='Mensagem', widget=forms.Textarea)
	captcha = CaptchaField()

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['phone'].widget.attrs['class'] = 'form-control'
		self.fields['subject'].widget.attrs['class'] = 'form-control'
		self.fields['message'].widget.attrs['class'] = 'form-control'
		self.fields['captcha'].widget.attrs['class'] = 'form-control captcha-input'

	def send(self):        
		texto = """
		Nome: %(name)s
		E-mail: %(email)s
		Telefone: %(phone)s
		Assunto: %(subject)s
		Mensagem:
		%(message)s
		""" % (self.cleaned_data)
		titulo = 'Contato'
		destino = settings.EMAILS_CONTATO
		fromemail = self.cleaned_data["email"]        
		email = EmailMessage(titulo,texto,"",destino, headers={'Reply-To': fromemail})                
		send = email.send()


