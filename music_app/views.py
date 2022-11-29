from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Songs, Downloads
from .serializers import UserSerializer, SongsSerializer

# todo how to load data into the database (python manage.py load data app_name/fixtures/data.json)
@api_view(
    ["GET", "POST"]
)
def user_list(request):
    if request.method == "GET":
        querySet = User.objects.all()
        serializer = SongsSerializer(querySet, many=True, context={'request', request})
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status.HTTP_201_CREATED)

    # elif request.method == "DELETE":
    #     User.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(
    ["GET", "PATCH", "DELETE"]
)
def user_detail(request, pk):
    songs = get_object_or_404(Songs, pk=pk, context={"request": request})
    if request.method == "GET":
        # querySet= User.objects.all()
        serializer = UserSerializer(songs, context={'request', request})
        return Response(serializer.data)

    elif request.method in ("PUT", "PATCH"):
        serializer = SongsSerializer(Songs, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    elif request.method == "DELETE":
        Songs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# creating the user business logic
@api_view(
    ["GET", "POST"]
)
def user_list(request):
    if request.method == "GET":
        userquery = User.objects.all()
        serializer = SongsSerializer(userquery, many=True, context={'request', request})
        return Response(serializer.data, serializer.create(User))
    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status.HTTP_201_CREATED)


@api_view(
    ["GET", "PATCH", "DELETE"]
)
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk, context={"request": request})
    if request.method == "GET":
        # querySet= User.objects.all()
        serializer = UserSerializer(User, context={'request', request})
        return Response(serializer.data)

    elif request.method in ("PUT", "PATCH"):
        serializer = SongsSerializer(User, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        User.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

