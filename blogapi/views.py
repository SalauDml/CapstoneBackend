from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import BlogSerializer
from .models import Blogs
from rest_framework import status
# Create your views here.
class BlogPostView(APIView):
    permission_classes=[permissions.AllowAny]
    
    def get(self,request):
        blog = Blogs.objects.all()
        serializer = BlogSerializer(blog,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    def put(self,request,title):
        blog= Blogs.objects.get(title=title)
        serializer = BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            return Response("Updated Successfully",status=status.HTTP_200_OK)
        return Response("mess up o", status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        title = self.request.query_params.get('title',"not available")
        print(title)
        blog = Blogs.objects.get(title=title)
        # print(blog)
        serializer = BlogSerializer(blog,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        try:
            title = self.request.query_params.get('title',"not available")
            blog = Blogs.objects.get(title=title)    
        except:
            raise Response("Blog not found")
        blog.delete()
        return Response("object successfully deleted")


        


