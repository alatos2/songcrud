from rest_framework import serializers
from .models import Song, Lyric, Artiste

class SongSerializer(serializers.ModelSerializer):
    artiste = serializers.StringRelatedField() # this shows any field of foreign key instead of id
    class Meta:
        model = Song
        fields = ['title', 'date_released', 'likes', 'artiste']

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ['content', 'song']

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['first_name', 'last_name', 'age']