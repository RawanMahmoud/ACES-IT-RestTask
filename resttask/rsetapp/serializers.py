from rest_framework import serializers
from .models import committee
from .models import member



class committeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = committee
        fields = '__all__'



class memberSerializer(serializers.ModelSerializer):

    class Meta:
        model = member
        fields = '__all__'
