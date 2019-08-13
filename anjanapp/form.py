from django import forms
from django.core import validators
from anjanapp.models import Document

class LoginForm(forms.Form):
    txt = forms.CharField(max_length=100)

class Calculation(forms.Form):
    adda= forms.CharField(max_length=100)
    addb= forms.CharField(max_length=100)

class LoginPass(forms.Form):
    log=forms.CharField(max_length=100)
    pas=forms.CharField(max_length=100,widget=forms.PasswordInput)

def valid_name(value):
    if value[0:3] !='WEL':
        raise forms.ValidationError('Name should start with WEL')

class FormName(forms.Form):
    name = forms.CharField(validators=[valid_name])
    email = forms.EmailField(validators=[validators.EmailValidator("please include @")])
    text = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        val = self.clean_name['name']
        if len(val)>5:
            raise forms.ValidationError('Name should be less than 5 characters')
        return val

class PostForm(forms.Form):
    tab = forms.CharField(max_length=50)

class Employee(forms.Form):
    eno = forms.CharField(max_length=264)
    ename = forms.CharField(max_length=264)
    email = forms.EmailField(max_length=264)


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description','document',)


class MailForm(forms.Form):
    subject = forms.CharField(max_length=50)
    message = forms.CharField(max_length=50)
    to = forms.CharField(max_length=50)