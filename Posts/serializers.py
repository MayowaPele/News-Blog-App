from django.db.models import fields
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'categories', 'title', 'overview', 'featured', 'thumbnail']