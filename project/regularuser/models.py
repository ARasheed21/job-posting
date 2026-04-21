from django.db import models
from accounts.models import User
from jobs.models import Job


class Applications(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    jobId = models.ForeignKey(Job, on_delete=models.CASCADE)
    cvlink = models.CharField(max_length=100)
    
    
