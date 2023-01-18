from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from django.conf import settings
User = settings.AUTH_USER_MODEL

from .forms import signup_form, login_form


def login_signup(request):
    login_f = login_form()
    signup_f = signup_form()
    
    args = {
        'login_form':login_f,
        'signup_form':signup_f,
        'errors':None
    }
    
    if request.user.is_authenticated:
        redirect(to='/')
        
    if request.method == 'GET':
        return render(request, 'login_signup.html', args)
    
    if request.method == 'POST':
        email = request.POST('email', None)
        
        #handle user login
        if not email:
            check = login_form(request.POST)
            #form validation
            if not check.is_valid():
                args['errors'] = check.errors
                return render(request, 'login_signup.html', args)
            check.clean()
            #check if user credentials are correct and login user
            user = authenticate(password = check.cleaned_data['password'], username = check.cleaned_data['username'].lower())
            if not user:
                args['errors'] = 'Invalid Credentials'
                return render(request, 'login_signup.html', args)
            login(request, user)
            redirect(to='/userhome')
            
         #handle user signup   
        if email:
            check = signup_form(request.POST)
            if not check.is_valid():
                args['errors'] = check.errors
                return render(request, 'login_signup.html', args)
            check.save()
            return redirect('/login')
            
    #to cover edge cases for request that are not supported
    if request.method != 'POST' or request.method != 'GET':
        redirect(to='/')
        
