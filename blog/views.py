from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
#home to handle the request
"""
IF we have a data base name post, how do we use it in the template?
posts= [json...]
def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    context = {
    'posts' = posts
    }
    return render(request,'blog/home.html')# if we want to use template.

"""
def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    context = {
    'posts' : Post.objects.all()
    }
    return render(request,'blog/home.html')# if we want to use template.
# Create your views here.
# should create templates for complecated HTML
# blog-> templates-> blog-> templates.HTML

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request,'blog/about.html')
