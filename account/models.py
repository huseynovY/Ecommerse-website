from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from core.models import Abstractmodel
# Create your models here.

class User(AbstractUser):
    image = models.ImageField('image', upload_to='user_profile/', null=True, blank=True)
    bio = models.CharField('bio', max_length=100, null=True, blank= True)
    ips = ArrayField(models.GenericIPAddressField(), null = True, blank=True)
    

    def get_image(self):
        if self.image:
            return self.image.url
        return '/static/images/images.png'


class BlockedIps(Abstractmodel):
    ip_address = models.GenericIPAddressField()



