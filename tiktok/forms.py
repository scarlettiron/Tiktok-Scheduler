from django import forms
import pendulum as pd

time = pd.now()


days = ((None, 'Day'), (1, 1))

hours = ((None, 'Hour'), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), 
                 (6, 6), (7, 7) , (8, 8), (9, 9), (10, 10),
                 (11, 11), (12, 12))

minutes = ((None, 'Minutes'), (0, 0), (15, 15), (30, 30), (45, 45))

timezones = ((None, 'Timezone'), ('Central', 'US/Central'), ('Pacific', 'US/Pacific'),
                    ('Eastern', 'US/Central'))

ampm = (('am', 'AM'), ('pm', 'PM'))

months = ((None, 'Month'), (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'),
          (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'),
          (10, 'October'), (11, 'November'), (12, 'December'))

next_year = time.year + 1
#years = [time.year, next_year]
years = ((None, 'Year'), (time.year, time.year), (next_year, next_year))

class tiktok_scheduler_form(forms.Form):
    video = forms.FileField(label = 'video', widget=forms.FileInput(attrs={'label':'Video',
                                                                            'accept':'video/mp4',
                                                                           'class':'tiktok-input'}))
    year = forms.IntegerField(label= 'year', widget=forms.Select(choices = years, 
                                                                 attrs={'placeholder':'Year',
                                                                           'class':'tiktok-input', 
                                                                           'default':'Year', 'selected':'Year'}))
    month = forms.IntegerField(label= 'month', widget=forms.Select(choices = months, 
                                                                   attrs={'placeholder':'Month',
                                                                        'class':'tiktok-input'}))
    day = forms.IntegerField(label= 'day', widget=forms.Select(choices = days, 
                                                               attrs={'placeholder':'Day',
                                                                           'class':'tiktok-input'}))
    hour = forms.IntegerField(label= 'hour', widget=forms.Select(choices = hours, 
                                                                 attrs={'placeholder':'Hour',
                                                                           'class':'tiktok-input'}))
    minutes = forms.IntegerField(label= 'minutes', widget=forms.Select(choices = minutes, 
                                                                       attrs={'placeholder':'Year',
                                                                           'class':'tiktok-input'}))
    timezone = forms.CharField(label='timezone', widget = forms.HiddenInput())
    
    ampm = forms.CharField(label='am or pm', widget = forms.Select(choices = ampm, attrs = {
                                                                                'class':'tiktok-input'}))
    

     

        
        
    