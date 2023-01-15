from django import forms

class tiktok_scheduler_form(forms.form):
    video = forms.FileField(label = 'video')
    year = forms.IntegerField(label= 'year')
    month = forms.IntegerField(label= 'month')
    day = forms.IntegerField(label= 'day')
    hour = forms.IntegerField(label= 'hour')
    minutes = forms.IntegerField(label= 'minutes')
    tz = forms.CharField(label='timezone')
    ampm = forms.CharField(label='am or pm')
    