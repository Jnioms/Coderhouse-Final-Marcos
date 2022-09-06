from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):

    username = models.ForeignKey(User, on_delete=models.CASCADE)
    userbio = models.CharField(max_length=255, blank=True, null=True )
    image = models.ImageField(upload_to="avatar/", null=True, blank=True)

    def __str__(self):
        return self.username.username

    def get_absolute_url(self):
        return reverse("user_profile", kwargs={'pk' : self.id})

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        try:
            if created:
                UserProfile.objects.create(username=instance).save()
        except Exception as err:
            print(f'Error creating user profile!\n{err}')