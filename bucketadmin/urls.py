from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Json_Data1 

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('RestApi',Json_Data1, basename='RestApi')



urlpatterns = [
    
    path('', include(router.urls)),
    path('',views.FresherRegister,name="FresherRigister"),
    path('FresherRigister',views.FresherRegister,name="FresherRegister"),
    path('CompanyRegister',views.CompanyRegister,name="CompanyRegister"),
    path('like_post', views.like_post, name='like_post'),
    path('Posting',views.Posting,name='Posting'),
    path('<int:User_id>/Companyprofile_data/',views.Companyprofile_data,name='Companyprofile_data'),
    path('Json_Data',views.Json_Data.as_view(),name='Json_Data'),
    path('Login',views.Login,name='Login'),
    path('check_out',views.Logout,name='Logout'),
    # path('Api',PostListView.as_view(), name='Api')
    
]