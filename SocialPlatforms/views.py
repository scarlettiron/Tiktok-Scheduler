from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Social
from rest_framework.generics import GenericAPIView
from .platform_auth import TiktokUtils
from users.models import CustomUser

@login_required(login_url='/login') 
def add_social_template(request):
    if request.method == 'GET':
        platform  = request.GET.get('platform', None)
        
        if not platform:
            return render(request, 'add_platform.html')
        
        if platform == 'tiktok':
            url = TiktokUtils.authorize_tiktok_url()
            return redirect(url)
        
    

#for redirecting to correct url for platform authorization
def add_social_redirect(request):

    return render(request, 'add_platform.html')
    

#endpoint user is redirected to after successful login
def add_social_return_uri(request):
    print(request)
    platform = request.GET.get('platform', None)
    if not platform:
        return render(request, 'add_platform.html', {'errors':'Problem adding platform. Try again later.'})
    
    if platform == 'tiktok':
        code = request.GET.get('code', None)
        error = request.GET.get('error', None)
        print(code)
        print(error)
        if not error:
            user = CustomUser.objects.get(username = request.user.username)
            sucess = TiktokUtils().store_code(code = code, user=user) 
            if sucess:
                return redirect('/upload-tiktok') 

