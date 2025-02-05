from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Advertisement
from .serializers import AdSerializer
from rest_framework import status

class AdListApiView(APIView):
    def get(self, request):
        ad_list = Advertisement.objects.all()
        serializer = AdSerializer(ad_list , many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = AdSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)