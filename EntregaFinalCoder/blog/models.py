from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from ckeditor.fields import RichTextField

def my_slugify_function(content):
    return content.replace('_', '-').replace(' ', '-').lower()

class Blog(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/')
    slug = AutoSlugField(populate_from='title', slugify_function=my_slugify_function)
    
    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})