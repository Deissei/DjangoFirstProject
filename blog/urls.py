from django.urls import path

from blog.views import list_blogs, detail_blog


urlpatterns = [
    path('blogs/', list_blogs, name="list_blog"),
    path('blogs/<int:pk>', detail_blog, name="detail_blog")
]