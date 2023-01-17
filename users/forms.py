from django.forms import Form, CharField, EmailField, TextInput, EmailInput


class login_form(Form):
    username=CharField(max_length=50, widget=TextInput(attrs = {
        'placeholder': 'Username',
        'class' : 'input-main'
    }))
    password=CharField(max_length=50, 
                       widget=TextInput(attrs = {
        'placeholder': 'Password',
        'class' : 'input-main'
    }))
    

class signup_form(Form):
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
    }))