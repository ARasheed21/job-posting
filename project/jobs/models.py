from django.db import models

# Create your models here.
from accounts.models import User, CompanyInfo

class Job(models.Model):
    title = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.CharField(default='0',max_length=100 )
    description = models.TextField()
