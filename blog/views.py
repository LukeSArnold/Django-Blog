from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Blog,Comments
from .forms import CommentForm
from django.utils import timezone
# Create your views here.

def about(request):
    template = loader.get_template('blog/about.html')
    return HttpResponse(template.render())

def techtips_with_css(request):
    template = loader.get_template('blog/techtips+css.html')
    return HttpResponse(template.render())

def techtips_without_css(request):
    template = loader.get_template('blog/techtips-css.html')
    return HttpResponse(template.render())

def plan(request):
    template = loader.get_template('blog/plan.html')
    return HttpResponse(template.render())

def blog_home(request):
    latest_blog_posts = Blog.objects.order_by('-posted')[:3]
    template = loader.get_template('blog/blog_home.html')
    context = {
            'latest_blog_posts': latest_blog_posts,
            }
    return HttpResponse(template.render(context, request))

def blog_archive(request):
    blog_posts = Blog.objects.order_by('-posted')
    template = loader.get_template('blog/blog_archive.html')
    context = {
            'blog_posts': blog_posts,
            }
    return HttpResponse(template.render(context,request))


def blog_entry(request, blog_title):
    blog_posts = Blog.objects.all()
    template = loader.get_template('blog/blog_entry.html')
    #return HttpResponse("you are looking at blog %s" % blog_title)
    context = {
            'blog_posts': blog_posts,
            'blog_title': blog_title,
            'form' : CommentForm,
            }
    return HttpResponse(template.render(context, request))




def comment(request, blog_title):
    
    if request.method == 'POST':
        user_name = request.POST['commenter_name']
        user_email = request.POST['email']
        user_content = request.POST['content']
        given_blog_title = blog_title
     
        blog_posts = Blog.objects.all()
        for iter_blog in blog_posts:
            if iter_blog.title == given_blog_title:
                iter_blog.comments_set.create(blog = iter_blog, commenter = user_name, email = user_email, content = user_content,
                        posted = timezone.now())
    return redirect('../../{}'.format(blog_title))

