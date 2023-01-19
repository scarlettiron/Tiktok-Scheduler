from django.forms import Form, ModelForm, CharField, TextInput, EmailInput
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models import Q

from .models import CustomUser

class login_form(Form):
    username=CharField(max_length=50, widget=TextInput(attrs = {
        'placeholder': 'Username',
        'class' : 'input-main'
    }))
    password=CharField(max_length=50, 
                       widget=TextInput(attrs = {
        'type': 'password',
        'placeholder': 'Password',
        'class' : 'input-main'
    }))
    

class signup_form(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        widgets = {
            'username':TextInput(attrs={
                        'placeholder': 'Username',
                        'class' : 'input-main'
            }),
            'password':TextInput(attrs={
                        'type':'password',
                        'placeholder': 'Password',
                        'class' : 'input-main'
            }), 
            'email':EmailInput(attrs={
                        'placeholder': 'Email',
                        'class' : 'input-main',
                        
            })
        }
        
    def clean(self):
        #check to make sure username and email are unique
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        check = CustomUser.objects.filter(Q(email = email) | Q(username = username))
        if len(check) > 0:
            raise ValidationError('Email or Username Exists')
        
        #make username lower cased
        self.cleaned_data['username'] = self.cleaned_data['username'].lower()
        return self.cleaned_data     



''' class signup_form(Form):
    username=CharField(max_length=50, widget=TextInput(attrs = {
        'placeholder': 'Username',
        'class' : 'input-main'
    }))
    password = CharField(max_length=50, widget=TextInput(attrs = {
        'placeholder': 'Password',
        'class' : 'input-main'
    }))
    verifypassword = CharField(max_length=50, widget=TextInput(attrs = {
        'placeholder': 'Verify Password',
        'class' : 'input-main'
    }))
    email = EmailField(max_length=150, widget=EmailInput(attrs = {
        'placeholder': 'Email',
        'class' : 'input-main'
    })) '''