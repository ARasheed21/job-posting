from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CompanyInfo(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    logo = models.URLField()

class User(AbstractUser):
    is_admin = models.BooleanField('Company Admin', default=False)
    is_regular = models.BooleanField('Regular User', default=False)
    username = models.CharField(max_length=255, null=True, unique=True)
    company_info = models.OneToOneField(CompanyInfo, on_delete=models.CASCADE, null=True, blank=True)
