from django.shortcuts import render
from . import models
from django.contrib import messages

def home(request):
    blogs = models.Blogs.objects.values()
    blogs = list(blogs)
    params = {'blogs': blogs}
    return render(request , 'index.html', params)

def create(request):
    if request.method == "POST" :
        title = request.POST.get('title','')
        category = request.POST.get('category','')
        desc =  request.POST.get('desc','')
        blog = models.Blogs(title=title, category=category ,desc=desc)
        blog.save()
        messages.success(request, "Blog is created successfully.")
    return render (request, "create.html")