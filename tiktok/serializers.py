from rest_framework.serializers import ModelSerializer
from .models import TiktokVideo

class tiktok_video_serializer(ModelSerializer):
    class Meta:
        model = TiktokVideo
        fields = '__all__'
        
        
        