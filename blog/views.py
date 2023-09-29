from django.shortcuts import render
from blog.models import Blog


def list_blogs(request):
    blogs = Blog.objects.all() # ORM 
    context = {
        "blogs": blogs,
    }
    return render(request, "blog-list.html", context)


def detail_blog(request, pk):
    blog = Blog.objects.get(id=pk) # ORM 
    context = {
        "blog": blog,
    }
    return render(request, "blog-detail.html", context)
