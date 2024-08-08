from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Properties,PropertyImages
from .serializers import PropertySerializer,PropertyImageSerializer
from rest_framework import permissions

from rest_framework import status
# Create your views here.

class PropertiesEndpoint(APIView):
    def get(self,request):
        permission_classes = [permissions.AllowAny]

        

        properties = Properties.objects.all()
        title = request.query_params.get('title',None)
        location = request.query_params.get('location',None)
        # print(location)
        pricing_range = request.query_params.get('pricing',None)
        property_size = request.query_params.get('size',None)
        property_type = request.query_params.get('property_type',None)
        if title!= None:
            properties=properties.filter(title = title)
        if location!=None:
            properties=properties.filter(location= location)
        # if pricing_range!=None:
        #     match(pricing_range):
        #         case'1000 - 5000':
        #             if  properties.
        if property_size!= None:
            properties=properties.filter(size = property_size)

        # print(properties)

        serializer = PropertySerializer(properties,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class SpecificPropertyEndpoint(APIView):
    def get(self,request,id):
        permission_classes = [permissions.AllowAny]
        serializer = PropertySerializer
        try:
            property = Properties.objects.get(id = id)
        except:
            raise Response("Property not found",status=status.HTTP_204_NO_CONTENT)
        serializer = PropertySerializer(property,many= False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class SpecificPropertyImagesEndpoint(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request,id):
        property = Properties.objects.get(id = id)
        image = PropertyImages.objects.get(owner_property = property)
        serializer = PropertyImageSerializer(image,many = False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
        





        



