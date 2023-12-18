from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ObjectDoesNotExist
class BathHouseModelSerilizer(serializers.ModelSerializer):

    class Meta:
        model = BathHouseModel
        fields = '__all__'

class BathHouseModelUpdateSerilizer(serializers.ModelSerializer):

    number_key = serializers.IntegerField(required=True)
    
    class Meta:
        model = BathHouseModel
        exclude = ('end_time',)
       
class BathHouseModelPostSerilizer(serializers.ModelSerializer):

    
    class Meta:
        model = BathHouseModel
        exclude = ('end_time',)
       
