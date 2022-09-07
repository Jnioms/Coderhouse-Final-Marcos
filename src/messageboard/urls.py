from django.urls import path
from messageboard.views import *


urlpatterns = [
    path("", MessageListView.as_view(), name='message_view'),
    path("create/", MessageCreateView.as_view(), name="message_create"),
    path("update/<pk>", MessageUpdateView.as_view(), name="message_update"),
    path("delete/<pk>", MessageDeleteView.as_view(), name="message_delete"),
]