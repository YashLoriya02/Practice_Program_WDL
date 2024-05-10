from django.shortcuts import render
from . import models
from django.contrib import messages
from datetime import datetime

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
        date_str =  request.POST.get('date','')
        time_str = request.POST.get('time')
        
        date_time_str = f"{date_str} {time_str}"
        combined_datetime = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
        
        new_blog = models.Blogs(title=title, category=category, desc=desc, created_date=combined_datetime)
        new_blog.save()

        messages.success(request, "Blog is created successfully.")
    return render (request, "create.html")