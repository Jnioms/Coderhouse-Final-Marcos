from django.urls import path
from userprofile.views import *

urlpatterns = [
    path("", ProfileIndex, name='profile_index'),
    path("<pk>", UserDetail.as_view(), name='user_profile'),
    path("update/<pk>", ProfileUpdate.as_view(), name="profile_update"),
    path("signup/", Signup, name='signup'),
    path("edit/", EditUser, name='user_edit'),
]