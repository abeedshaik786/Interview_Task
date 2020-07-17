from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Funpost,Status
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout,authenticate
from .forms import FunpostModel
from django.urls import reverse
from .serializers import FunpostSerializers
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
import requests
from rest_framework.generics import ListAPIView
# Create your views here.

def FresherRegister(request):
    # import pdb;pdb.set_trace()
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.info(request,'!That username is already taken.')
            return render(request,'FresherRigister.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'!That email is already taken.')
            return render(request,'FresherRigister.html')
        else:
            obj = User(first_name = firstname , last_name = lastname ,email = email , username = username ,password = password)
            obj.set_password(password)
            obj.is_student = True
            obj.save()
            # import pdb;pdb.set_trace()
            return render(request,'FresherRigister.html')
           
    return render(request,'FresherRigister.html')

def CompanyRegister(request):
    #import pdb;pdb.set_trace()
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.info(request,'!That username is already taken.')
            return render(request,'FresherRigister.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'!That email is already taken.')
            return render(request,'FresherRigister.html')
        obj = User(first_name = firstname , last_name = lastname ,email = email , username = username ,password = password)
        obj.set_password(password)
        obj.is_staff = True
        obj.save()
        return render(request,'FresherRigister.html')
def Companyprofile_data(request,User_id):
    user_context = User.objects.get(id = User_id)
    form = FunpostModel()
    url = "http://127.0.0.1:8000/RestApi/"
    headers = {'Authorization': 'Token 1e8cff8c90ebc33cf5dcc4c16ecf720f872318b3'}
    r = requests.get(url,headers=headers).json()
    url = "http://127.0.0.1:8000/Json_Status"
    headers = {'Authorization': 'Token 1e8cff8c90ebc33cf5dcc4c16ecf720f872318b3'}
    s = requests.get(url,headers=headers).json()
    #import pdb;pdb.set_trace()
    data = Funpost.objects.all()
    Posted_data = Funpost.objects.filter(Posted_users_id=User_id) 
    return render(request,'adminpage.html',{'form':form ,'user_context':user_context,'r':r,'s':s,'Posted_data':Posted_data})
def Posting(request):
    if request.method =='POST':
        user_id = request.POST.get('user_id')
        user_data = User.objects.get(id = user_id)
        #import pdb; pdb.set_trace()
        form = FunpostModel(request.POST,request.FILES)
        if form.is_valid():
            object_of_post = form.save()
            obj = Funpost.objects.get(id = object_of_post.id)
            obj.Posted_users = user_data
            user_context=obj.save()
            form = FunpostModel()
            return HttpResponseRedirect(reverse('bucketadmin:Companyprofile_data', args={user_data.id}))
def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "":
            messages.info(request,'!That username is should not be empty.')
            return render(request,'FresherRigister.html')
        elif password == "":
            messages.info(request,'!That password should not be empty.')
            return render(request,'FresherRigister.html')
        if authenticate(request,username = username , password = password):
            validation = User.objects.get(username=username)
            users = authenticate(request,username = username , password = password)
            if validation.is_staff == False:
                if users is not None:
                    login(request,users)
                    auth.login(request, users)
                    user_data = User.objects.get(username=username)
                    return HttpResponseRedirect(reverse('userfunbucket:Admin_Post', args={user_data.id}))
            else:
                    if  validation.is_staff == True:
                        if users is not None:
                            # import pdb;pdb.set_trace()
                            login(request,users)
                            auth.login(request, users)
                            user_data = User.objects.get(username=username)
                            
                            return HttpResponseRedirect(reverse('bucketadmin:Companyprofile_data', args={user_data.id}))
        else:
            messages.info(request,'Login With Valid Username and Password.')
            return render(request,'FresherRigister.html')   
def Logout(request):

    logout(request)
    return HttpResponseRedirect('FresherRigister')
def ModelViewSet(viewsets,request):
    if request.method == 'POST':
        serializer_class = FunpostSerializers
        queryset = Funpost.objects.all()
        permission_classes = (IsAuthenticated,)
        filter_backends = (SearchFilter,)
        search_fields = ('City',)
    form = FunpostModel()
    return render(request,'index.html',{'form':form})
class Json_Data(APIView):
    def get(self,request):
        Data = Funpost.objects.all()
        Serializer = FunpostSerializers(Data,many=True)
        
        return Response(Serializer.data)

class Json_Data1(viewsets.ModelViewSet):
    serializer_class = FunpostSerializers
    queryset = Funpost.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('id ',)
def like_post(request,obj="dummy"):
    user = request.user
    if request.method == 'POST':
        created =Status()
        user = request.user
        post_id = request.POST.get('post_id')
        user_id = request.POST.get('user_id')
        user_data = User.objects.get(id=user_id)
        post_post = Funpost.objects.get(id=post_id)
        #import pdb; pdb.set_trace()
        #post_post.liked.all()
        #data=post_post.liked.all()
        #print(data)
        if Status.objects.filter(Liked_users__id=user_data.id , Post__id=post_post.id).exists():
            #import pdb; pdb.set_trace()
            data=Status.objects.filter(Liked_users__id=user_data.id)
            data=data.filter(Post__id=post_post.id)
            obj=data[0]
            if user_data.id == obj.Liked_users.id:
                #import pdb; pdb.set_trace()
                if obj.value == 'Like':
                   obj.value='Unlike'
                   obj.save()
                else:
                    obj.value='Like'
                    obj.save() 
        else:
            #import pdb; pdb.set_trace()
            created.value='Like'
            created.Post=post_post
            created.Liked_users = user_data
            created.save()
    url = "http://127.0.0.1:8000/RestApi/"
    headers = {'Authorization': 'Token 1e8cff8c90ebc33cf5dcc4c16ecf720f872318b3'}
    r = requests.get(url,headers=headers).json()
    return render(request,'userpage.html',{'user_data':user_data,'created':created,'r':r,'obj':obj,'post_post':post_post})
    