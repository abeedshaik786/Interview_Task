from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.
LIKE_CHOICES =(
    ('Like','Like'),
    ('Unlike','Unlike')

)

class Funpost(models.Model):
    Img_post = models.FileField(blank=True,null=True,upload_to='img')
    Description = models.CharField(max_length=500)
    Posted_users = models.ForeignKey(User,blank=True,on_delete=models.CASCADE,null=True,related_name='posted' )

class Status(models.Model):
    Liked_users = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Post = models.ForeignKey(Funpost,on_delete=models.CASCADE,null=True)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)


