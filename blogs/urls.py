'''定义blogs的URL模式'''
from django.urls import path
from . import views

app_name='blogs'
urlpatterns=[
    #主页
    path('',views.index,name='index'),
    #显示所有博客的页面
    path('blogs/',views.blogs,name='blogs'),
    #特定博文的详细页面
    path('blogs/<int:blog_id>/',views.blog,name='blog'),
    #用于添加新博客的网页
    path('new_blog/',views.new_blog,name='new_blog'),
    #用于添加新的博文的网页
    path('new_post/<int:blog_id>/',views.new_post,name='new_post'),
    #用于编辑现有博文的网页
    path('edit_post/<int:post_id>/',views.edit_post,name='edit_post'),
    #用于删除博客网页
    path('delete_blog/<int:blog_id>/',views.delete_blog,name='delete_blog'),
     #用于删除博文的网页
    path('delete_post/<int:post_id>/',views.delete_post,name='delete_post'),
]