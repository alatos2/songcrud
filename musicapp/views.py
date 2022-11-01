from django.shortcuts import render
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def SongView(request):
    if request.method == 'GET':
        posts = Song.objects.all() # queryset
        serializer = SongSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SongSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def SongDetailsView(request, pk):
    try:
        post = Song.objects.get(pk=pk)
    except post.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = SongSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=204)