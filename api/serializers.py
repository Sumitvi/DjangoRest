from rest_framework import serializers
from .views import *
from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User



class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError('Username is Taken')
            

    def validate(self, data):
        if data['email']:
            if User.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError('Username is Taken')

        return data
    
    def create(self, validated_data):
         user = User.objects.create(username = validated_data['username'] , email = validated_data['email'])
         user.set_password(password = validated_data['password'])
         return validated_data
         print(validated_data)





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