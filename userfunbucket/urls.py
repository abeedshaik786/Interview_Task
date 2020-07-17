from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:User_id>/Admin_Post/',views.Admin_Post, name='Admin_Post'),
    path('Json_Status',views.Json_Status.as_view(),name='Json_Status'),
    
]

