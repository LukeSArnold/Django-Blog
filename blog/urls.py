from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
        path('about/',views.about, name='about'),
        path('tech+css/',views.techtips_with_css, name = "tech+css"),
        path('tech-css/',views.techtips_without_css, name = "tech-css"),
        path('', views.blog_home, name = "blog"),
        path('archive', views.blog_archive, name = "archives"),
        path('comment/<str:blog_title>/', views.comment, name = "comment"),
        path('<str:blog_title>/', views.blog_entry, name = "blog_entry"),
        path('plan', views.plan, name = 'plan'),
        ]

