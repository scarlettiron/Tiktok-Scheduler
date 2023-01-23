from django.forms import ModelForm
from .models import Social

class SocialForm(ModelForm):
    class Meta:
        fields = '__all__'