from django.urls import path
from blog.views import *


urlpatterns = [
    path("", BlogListView.as_view(), name='blog_view'),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("update/<slug:slug>", BlogUpdateView.as_view(), name="blog_update"),
    path("delete/<slug:slug>", BlogDeleteView.as_view(), name="blog_delete"),
    path('blog-like/<slug:slug>', BlogLike, name="blog_like"),
    path("<slug:slug>", BlogDetailView.as_view(), name="blog_detail"),
]