from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog,Post
from .forms import BlogForm,PostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages

def index(request):
    '''用户主页'''
    blogs=Blog.objects.order_by('date_added')
    context={'blogs':blogs}
    return render(request,'blogs/index.html',context)

def blogs(request):
    '''显示所有博客'''
    if request.user.is_authenticated:
        blogs=Blog.objects.filter(owner=request.user).order_by('date_added')
    else:
        blogs=Blog.objects.none()
    context={'blogs':blogs}
    return render(request,'blogs/blogs.html',context)

def blog(request,blog_id):
    '''显示单个博客及其所有博文'''
    blog=Blog.objects.get(id=blog_id)
    posts=blog.post_set.order_by('-date_added')
    context={'blog':blog,'posts':posts}
    return render(request,'blogs/blog.html',context)

@login_required
def new_blog(request):
    '''添加新博客'''
    if request.method!='POST':
        #未提交数据：创建一个新表单
        form=BlogForm()
    else:
        form=BlogForm(data=request.POST)
        if form.is_valid():
            new_blog=form.save(commit=False)
            new_blog.owner=request.user
            new_blog.save()
            return redirect('blogs:blogs')
    
    #显示空表单或指出表单数据无效
    context={'form':form}
    return render(request,'blogs/new_blog.html',context)

@login_required
def new_post(request,blog_id):
    '''在特定博客中添加新博文'''
    blog=Blog.objects.get(id=blog_id)
    if blog.owner!=request.user:
        raise Http404
    
    if request.method!='POST':
        #未提交数据：创建一个空表单
        form=PostForm()
    else:
        #POST提交数据：对数据进行处理
        form=PostForm(data=request.POST)
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.blog=blog
            new_post.save()
            return redirect('blogs:blog',blog_id=blog_id)
        
    #显示空表单或指出表单数据无效
    context={'blog':blog,'form':form}
    return render(request,'blogs/new_post.html',context)

@login_required
def edit_post(request,post_id):
    '''编辑现有博文'''
    post=Post.objects.get(id=post_id)
    blog=post.blog
    if blog.owner!=request.user:
        raise Http404
    
    if request.method!='POST':
        #初次请求:使用当前博文填充表单
        form=PostForm(instance=post)
    else:
        #POST提交的数据：对数据进行处理
        form=PostForm(instance=post,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog',blog_id=blog.id)
    context={'post':post,'blog':blog,'form':form}
    return render(request,'blogs/edit_post.html',context)

@login_required
def delete_blog(request, blog_id):
    '''删除博客'''
    blog = get_object_or_404(Blog, id=blog_id)
    
    # 检查用户权限
    if blog.owner != request.user:
        raise Http404
    
    if request.method == 'POST':
        # 确认删除
        blog.delete()
        messages.success(request, f'博客 "{blog.name}" 已成功删除。')
        return redirect('blogs:blogs')
    
    # GET请求：显示确认页面
    context = {'blog': blog}
    return render(request, 'blogs/delete_blog.html', context)

@login_required
def delete_post(request, post_id):
    '''删除博文'''
    post = get_object_or_404(Post, id=post_id)
    blog = post.blog
    
    # 检查用户权限
    if blog.owner != request.user:
        raise Http404
    
    if request.method == 'POST':
        # 确认删除
        blog_id = blog.id  # 保存blog_id用于重定向
        post.delete()
        messages.success(request, '博文已成功删除。')
        return redirect('blogs:blog', blog_id=blog_id)
    
    # GET请求：显示确认页面
    context = {'post': post, 'blog': blog}
    return render(request, 'blogs/delete_post.html', context)