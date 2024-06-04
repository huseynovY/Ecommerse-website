from django.db import models
from core.validators import validate_gmail
# Create your models here.
class Abstractmodel(models.Model):
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)

    class Meta:
        abstract = True

        
class Contact(models.Model):
    name = models.CharField('name', max_length=100, unique = True)
    email = models.EmailField('email', max_length=40, validators = [validate_gmail])
    subject = models.CharField('subject', max_length=100)
    message = models.TextField('massage', max_length=250) 


    