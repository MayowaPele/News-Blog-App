from inspect import Parameter
from django.http.multipartparser import parse_header
from django.shortcuts import render
from rest_framework.response import Response
from .models import Post
from marketing.models import Signup
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .serializers import PostSerializer
from rest_framework import status


# Create your views here.
class PostAPIView(APIView):

    parser_classes = (MultiPartParser, )

    def get(self, response):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, response):
        serializer = PostSerializer(data=response.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(response):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    
    if response.method == "POST":
        email = response.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        
    context = {
        'object_list': featured,
        'latest': latest
    }
    return render(response, 'main/index.html', context)
    
def blog(response):
    return render(response, 'main/blog.html')

def post(response):
    return render(response, 'main/post.html')    