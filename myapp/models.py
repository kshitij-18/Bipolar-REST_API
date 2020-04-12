from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='books', null=True)
    title = models.CharField(max_length=30)
    amazon_url = models.URLField()
    author = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)

    def __str__(self):
        return self.title


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
