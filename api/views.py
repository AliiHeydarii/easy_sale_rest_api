from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Advertisement
from .serializers import AdListSerializer , AdDetailSerializer , CustomUserSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class AdListApiView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        ad_list = Advertisement.objects.all()
        serializer = AdListSerializer(ad_list , many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = AdListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    

class AdDetailApiView(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    def get(self,request,pk):
        ad = get_object_or_404(Advertisement,pk=pk)
        serializer = AdDetailSerializer(ad)
        return Response(serializer.data)
    
    def put(self,request,pk):
        ad = get_object_or_404(Advertisement,pk=pk)
        serializer = AdDetailSerializer(ad , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
       ad = get_object_or_404(Advertisement,pk=pk)
       ad.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
   
   
class UserCreateApiView(APIView):
    def post(self,request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)