from rest_framework.serializers import ModelSerializer
from .models import Social

class SocialSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'