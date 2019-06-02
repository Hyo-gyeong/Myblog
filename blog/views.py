from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import datetime
from .forms import New
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def new(request):

    # 1. 입력된 내용 처리 : POST
    if request.method == 'POST':
        form = New(request.POST, request.FILES)
        if form.is_valid(): 
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
        return redirect('home')
            
    # 2. 빈 페이지 띄워주는 기능 : GET
    else:
        form = New()
        return render(request, 'new.html', {'form': form}) 

def delete(request, blog_id):

    blog = get_object_or_404 (Blog, pk = blog_id)
    blog.delete()

    return redirect('/')

def edit(request, blog_id):
    
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.save()

        return redirect('/blog/'+str(blog.id))

    else:

        return render(request, 'edit.html', {'blog':blog})

def detail(request, blog_id):
    
    post = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'post':post})

