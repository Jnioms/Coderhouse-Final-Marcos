from django.urls import path
from blog.views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", BlogListView.as_view(), name='blog_view'),
    path("create", BlogCreateView.as_view(), name="blog_create"),
    path("update/<slug:slug>", BlogUpdateView.as_view(), name="blog_update"),
    path("delete/<slug:slug>", BlogDeleteView.as_view(), name="blog_delete"),
    path("<slug:slug>", BlogDetailView.as_view(), name="blog_detail"),

    # path("login/", iniciar_sesion, name="iniciar_sesion"),
    # path("register/", registrar_usuario, name="registro"),
    # path("logout/", LogoutView.as_view(template_name="coder/autenticacion/logout.html"), name="logout"),
    # path("edit/", editar_usuario, name="editar_usuario"),
]