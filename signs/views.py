from django.shortcuts import render
from .serializers import CategorSignsSerializer,RoadSignsSerializer
from .models import CategorySigns,RoadSigns
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ListCategoryApiView(APIView):
    def get(self,request):
        category=CategorySigns.objects.all()
        serializer=CategorSignsSerializer(category,many=True)
        serializer_data={
            'cateory': serializer.data,
            'status':'success',
            'status_code':status.HTTP_200_OK
        }
        return Response(serializer_data)