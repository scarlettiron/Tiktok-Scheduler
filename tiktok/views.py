from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .serializers import tiktok_video_serializer
import pendulum as pen
from .forms import tiktok_scheduler_form
from .models import TiktokVideo
from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from users.models import CustomUser


#For django template version endpoint
#@login_required(login_url='/login')     
def upload_tiktok(request):
    tiktok_form = tiktok_scheduler_form()
    if request.method == 'GET':
        return render(request, 'upload_tiktok.html', {'form':tiktok_form})
    
    if request.method == 'POST':
        form = tiktok_scheduler_form(request.POST, request.FILES)
        
        if not form.is_valid():
            return render(request, 'upload_tiktok.html')
        
        fields = {}
        form.clean()
    
        fields['year'] = int(form.cleaned_data['year'])
        fields['month'] = int(form.cleaned_data['month'])
        fields['day'] = int(form.cleaned_data['day'])
        fields['hour'] = int(form.cleaned_data['hour'])
        fields['minutes'] = int(form.cleaned_data['minutes'])
        
        fields['timezone'] = form.cleaned_data['timezone']
        ampm = form.cleaned_data['ampm']
        video = form.cleaned_data['video']
        
        if ampm == 'pm':
            fields['hour'] = fields['hour'] + 12
            if fields['hour'] > 24:
                fields['hour'] = 0

        
        pen_tz = pen.timezone(fields['timezone'])
        utc_time = pen.timezone('UTC')
        
        local_scheduled_time = pen.datetime(form.cleaned_data['year'],  form.cleaned_data['month'],
                                        form.cleaned_data['day'], form.cleaned_data['hour'],
                                        form.cleaned_data['minutes'], tz = pen_tz)
        utc_scheduled_time = utc_time.convert(local_scheduled_time)
        iso8601 = utc_scheduled_time.to_iso8601_string()
        
        user = CustomUser.objects.get(username = request.user.username)
        print(user)
        serializer = tiktok_video_serializer(data={'file':video, 'user':request.user.pk, 'scheduled':iso8601})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
        return render(request, 'upload_tiktok.html', {'success':True, 'error':False}, status=204)



#For API version endpoint
class ScheduleTiktokPost(CreateAPIView):
    model = TiktokVideo
    serializer_class = tiktok_video_serializer
    #permission_classes = [permissions.IsAuthenticated]
    
             
        
    
        
        
        
