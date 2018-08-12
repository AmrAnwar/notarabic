from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Word(models.Model):
    user        =models.ForeignKey(User,on_delete=models.CASCADE,related_name="word_creator")
    name        = models.CharField(max_length=50,null=False)
    description = models.TextField(null=True,blank=True)
    example     = models.TextField(null=True,blank=True)
    #ToDo add image field
    up_vote     = models.IntegerField(default=0)
    down_vote   = models.IntegerField(default=0)
    created_at  = models.DateField(auto_now=True)



