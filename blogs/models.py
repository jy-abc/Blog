from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    '''博客'''
    name=models.CharField(max_length=25)
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        '''返回模型字符串的表示'''
        return self.name

class Post(models.Model):
    '''博文'''
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        '''返回一个表示条目的简单字符串'''
        return f"{self.text[:25]}"