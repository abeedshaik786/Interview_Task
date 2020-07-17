from django.shortcuts import render
import requests
from bucketadmin.models import Status
from rest_framework.views import APIView
from rest_framework.response import Response
from pprint import pprint
from .serializers import StatusSerializers
from django.contrib.auth.models import User,auth

# Create your views here.

def Admin_Post(request,User_id):
    url = "http://127.0.0.1:8000/RestApi/"
    headers = {'Authorization': 'Token 1e8cff8c90ebc33cf5dcc4c16ecf720f872318b3'}
    r = requests.get(url,headers=headers).json()
    pprint(r)
    user_data = User.objects.get(id = User_id)
    
    url = "http://127.0.0.1:8000/Json_Status"
    headers = {'Authorization': 'Token 1e8cff8c90ebc33cf5dcc4c16ecf720f872318b3'}
    s = requests.get(url,headers=headers).json()
    print(s)
    return render(request,'userpage.html',{'r':r,'s':s,'user_data':user_data})
class Json_Status(APIView):
    def get(self,request):
        Data = Status.objects.all()
        Serializer = StatusSerializers(Data,many=True)
        return Response(Serializer.data)

    
    
