from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import PeopleSerializer , LoginSerializer , RegisterSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth.models import User



class RegisterView(APIView):

    def post(self , request):
        data = request.data
        serializer = RegisterSerializer(data = data)

        if not serializer.is_valid():
            return Response({
                "status": False,
                "message": serializer.errors
            })
        
        serializer.save()

        return Response({"status" : True , "message" : "User Created"})



    # Model View Sets

class PersonViewSet(viewsets.ModelViewSet):
        queryset = Person.objects.all()
        serializer_class = PeopleSerializer




class PersonAPI(APIView):

    def get(self , request):
        return Response({"message": "GET Request Called"})
    
    def post(self , request):
        return Response({"message": "POST Request Called"})
    
    def put(self , request):
        return Response({"message": "PUT Request Called"})
    
    def patch(self , request):
        return Response({"message": "PATCH Request Called"})
    
    def delete(self , request):
        return Response({"message": "DELETE Request Called"})






@api_view(['GET','POST','PUT'])
def login(request):
    course = {
        'name': 'Python Backend Development',
        'skills covered' : ['python' , 'django', 'djangorest'],
        'tutor': 'codeWithDurgesh'
    }

    if request.method == 'GET':
        return Response(course)
    if request.method == 'POST':
        data = request.data
        print(data)
        return Response(course)




@api_view(['POST'])
def Auth(request):
    data = request.data
    serializer = LoginSerializer(data = data)

    if serializer.is_valid():
        data = serializer.validated_data
        return Response({'message': 'Login Sucessfully'})
    
    return Response(serializer.errors)



@api_view(['GET', 'POST' , 'PUT' , 'PATCH'])
def person(request):
    if request.method == 'GET':
        obj = Person.objects.all()
        serializer = PeopleSerializer(obj , many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])

        serializer = PeopleSerializer(obj , data = data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    


