from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer, TaskSerializer, PictureSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from . models import Task, Profile



@api_view(['POST'])
def signin(request):
    if request.method == "POST":
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token,created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "status": "success",
                "message": f"Welcome {user.username}"
            })
        else:
            return Response({
                "status":"error",
                "message": "Incorrect username or password"
            })
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['POST'])
def signup(request):
    if request.method == "POST":
        username = request.data['username']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        password = request.data['password']
        
        if User.objects.filter(username=username):
            return Response({
                "status": "error",
                "message": "Username is not available"
            })
        elif User.objects.filter(email=email):
            return Response({
                "status": "error",
                "message":"Email address already exists"
            })
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            token,created = Token.objects.get_or_create(user=user)
            return Response({
                "status":"created",
                "token": token.key,
                "message": f"Thanks for joining us {user.first_name}"
            })
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request):
    serializer = UserSerializer(request.user, many=False)
    profile = Profile.objects.filter(user=request.user).first()
    picture = PictureSerializer(profile, many=False).data
    
    return Response({
        "user": serializer.data,
        'picture':request.build_absolute_uri(picture['picture'])
    })
    
 
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])   
def uploadPicture(request):
    if request.method == "POST":
        img = request.data.get('picture')
        if Profile.objects.filter(user=request.user):
            profile = Profile.objects.filter(user=request.user).first()
            profile.picture = img
            profile.save()
            return Response({
                "status":"success",
                "message":"Profile picture updated"
            })
        else:
            picture = Profile.objects.create(
                user = request.user,
                picture = img
            )
            picture.save()
            return Response({
                "status":"success",
                "message": "Profile picture updated"
            })
 

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])   
def createTask(request):
    if request.method == "POST":
        title = request.data['title']
        date = request.data['date']
        time = request.data['time']
        desc = request.data['desc']
        
        task = Task.objects.create(
            user = request.user,
            title = title,
            date = date,
            time = time,
            desc = desc
        )
        task.save()
        return Response({
            "status":"created",
            "message": f"{title} created successfully"
        })
    
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def tasks(request):
    if request.method == "GET":
        tasks = Task.objects.filter(user=request.user).order_by('-id')
        serializer = TaskSerializer(tasks, many=True)
        return Response({
            "tasks": serializer.data
        })
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteTask(request, pk):
    if request.method == "DELETE":
        my_task = Task.objects.filter(user=request.user)
        task = my_task.get(id=pk)
        task.delete()
        return Response({
            "status":"deleted",
            "message": f"{task.title} deleted successfully"
        })
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def completeTask(request, pk):
    if request.method == "GET":
        my_task = Task.objects.filter(user=request.user)
        task = my_task.get(id=pk)
        task.is_completed = True
        task.save()
        return Response({
            "status":"completed",
            "message": f"{task.title} completed successfully"
        })
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



