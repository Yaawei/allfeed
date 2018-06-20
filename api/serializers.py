from rest_framework import serializers
from accounts.models import LikedEntry
from newsfeed.models import NewsPiece
from django.contrib.auth.models import User


class NewsPieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPiece
        fields = [
            'title',
            'publish_date',
            'description',
            'url',
            'author',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
        ]
        lookup_field = 'username'


class LikedEntrySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    liked_entry = NewsPieceSerializer(read_only=True)

    class Meta:
        model = LikedEntry
        fields = [
            'user',
            'liked_entry',
        ]
        lookup_field = 'user__username'
