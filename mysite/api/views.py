from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView
# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    def delete(self,request,*args,**kwrgs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"
    
class BlogPostList(APIView):
    def get(self,request,format=None):
        # get the title for query parameters (if none,default to empty string)
        title = request.query_params.get("title","")
        lookup_field = "title"
        if title:
            # filter the qury set base on title
            blog_post = BlogPost.objects.filter(title_icontains=title)
            
        else:
            # if no title is provided, return all blog post
            blog_post = BlogPost.objects.all()
            
        serialize = BlogPostSerializer(blog_post,many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)
        