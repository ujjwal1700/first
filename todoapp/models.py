from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    logger= models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    task=models.CharField(max_length=100)
    completed=models.BooleanField(default=False)


    def __str__(self):
        return self.task
