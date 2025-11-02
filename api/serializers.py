from rest_framework import serializers
from .views import *
from .models import *
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    

class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = '__all__'
        depth = 1


        # Validations in serialization

    def validate(self , data):
        if data['age'] < 18:
            raise serializers.ValidationError('Age Should be Greater than 18')
        return data