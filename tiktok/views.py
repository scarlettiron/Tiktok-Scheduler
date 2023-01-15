from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .serializers import tiktok_video_serializer
import pendulum as pen
from .forms import tiktok_scheduler_form
from .models import TiktokVideo
from rest_framework.generics import CreateAPIView
from rest_framework import permissions

#@login_required(login_url='/login')
def upload_tiktokv1(self, request):
    if request.method == 'GET':
        return render(request, 'upload_tiktok.html')
    
    if request.method == 'POST':
        fields = {'year':None, 'month':None, 'day':None, 
                  'hour':None, 'minutes':None, 'seconds':0, 'tz':None}
        
        fields['year'] = request.data.get('year', None)
        fields['month'] = request.data.get('month', None)
        fields['day'] = request.data.get('day', None)
        fields['hour'] = request.data.get('hour', None)
        fields['minutes'] = request.data.get('minutes', None)
        
        print(request.data)
        
        tz = request.data.get('tz', None)
        ampm = request.data.get('time', None)
        video = request.FILES.get('video', None)
        
        if None in fields.values() or ampm == None or video == None or tz == None:
            return render(request, 'upload_tiktok.html', {'error':'Fill out all fields', 'success':False})
        
        #offset = dt.utcoffset(fields['tz'])
        
        if ampm == 'PM':
            fields['hour'] = fields['hour'] + 12
            
        #scheduled_time = dt(*fields.values())
        pen_tz = pen.timezone(tz)
        local_scheduled_time = pen.datetime(*fields.values(), tz = pen_tz)
        #utc_scheduled_time = dt.fromtimestamp(local_scheduled_time, tz = timezone.utc)
        utc_time = pen.timezone('UTC')
        utc_scheduled_time = utc_time.convert(local_scheduled_time)
        iso8601 = utc_scheduled_time.to_iso8601_string()
        
        print(local_scheduled_time)
        print(utc_scheduled_time)
        
        serializer = tiktok_video_serializer(data={'video':video, 'user':request.user, 'scheduled_time':iso8601})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
        return render(request, 'upload_tiktok.html', {'success':True, 'error':False})

#For django template version endpoint       
def upload_tiktok(self, request):
    tiktok_form = tiktok_scheduler_form()
    if request.method == 'GET':
        return render(request, 'upload_tiktok.html', {'form':tiktok_form})
    
    if request.method == 'POST':
        form = tiktok_scheduler_form(request.POST)
        
        if not form.is_valid():
            return
        
        fields = {'year':None, 'month':None, 'day':None, 
        'hour':None, 'minutes':None, 'seconds':0, 'tz':None}
    
        fields['year'] = form.cleaned_data['year']
        fields['month'] = form.cleaned_data['month']
        fields['day'] = form.cleaned_data['day']
        fields['hour'] = form.cleaned_data['hour']
        fields['minutes'] = form.cleaned_data['minutes'] 
        
        tz = form.cleaned_data['tz']
        ampm = form.cleaned_data['time']
        video = form.cleaned_data['video']
        
        if None in fields.values() or ampm == None or video == None or tz == None:
            return render(request, 'upload_tiktok.html', {'error':'Fill out all fields', 
                                                          'success':False,
                                                          'form':tiktok_form})
        if ampm == 'PM':
            fields['hour'] = fields['hour'] + 12
            if fields['hour'] > 24:
                fields['hour'] = 0
            
        print(fields)
        
        pen_tz = pen.timezone(tz)
        local_scheduled_time = pen.datetime(*fields.values(), tz = pen_tz)
        utc_time = pen.timezone('UTC')
        utc_scheduled_time = utc_time.convert(local_scheduled_time)
        iso8601 = utc_scheduled_time.to_iso8601_string()
        
        print(local_scheduled_time)
        print(utc_scheduled_time)
        
        serializer = tiktok_video_serializer(data={'video':video, 'user':request.user, 'scheduled_time':iso8601})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
        return render(request, 'upload_tiktok.html', {'success':True, 'error':False})



#For API version endpoint
class ScheduleTiktokPost(CreateAPIView):
    model = TiktokVideo
    serializer_class = tiktok_video_serializer
    #permission_classes = [permissions.IsAuthenticated]
    
             
        
    
        
        
        
