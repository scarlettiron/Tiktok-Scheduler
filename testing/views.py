from django.shortcuts import render
from .models import test_model
import pendulum as pen

def test_it(request, pk):
    if pk == 0:
        pen_tz = pen.timezone('EST')
        utc_time = pen.timezone('UTC')
            
        local_scheduled_time = pen.datetime(2023,  1, 20, 8, 46, tz = pen_tz)
        utc_scheduled_time = utc_time.convert(local_scheduled_time)
        iso8601 = utc_scheduled_time.to_iso8601_string()
        
        test_model.objects.create(schedule=iso8601)
        return render(request, 'test.html', {'test':{'text':'None', 'uploaded':'None'}})
    
    else:
        test = test_model.objects.get(pk=pk)
        return render(request, 'test.html', {'test':test})