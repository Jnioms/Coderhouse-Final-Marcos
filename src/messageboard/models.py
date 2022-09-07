from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Messages(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=255)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={'pk' : self.id})