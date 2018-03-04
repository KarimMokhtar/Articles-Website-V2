from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name



class Post(models.Model):
    
    title       = models.CharField(max_length = 100)
    body        = models.CharField(max_length = 400)
    created_at  = models.DateTimeField(default = datetime.now)
    updated_at  = models.DateTimeField(null = True, blank = True)
    category_id = models.IntegerField(default = 0)
    user_id     = models.IntegerField(default = 0,null = True)
    Author      = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    categor    = models.ForeignKey(Category, on_delete = models.CASCADE, null = True)
    
    def __str__(self):
        return self.title
    
    
    
class Comment(models.Model):
    
    body      = models.CharField(max_length = 200)
    post      = models.ForeignKey(Post, on_delete = models.CASCADE, null = True)
    Author    = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    def __str__(self):
        return self.body
    
    
    
class Reply(models.Model):
    
    body      = models.CharField(max_length = 200)
    comment   = models.ForeignKey(Comment, on_delete = models.CASCADE, null = True)
    Author    = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    def __str__(self):
        return self.body
    
    
    