from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class  Employees(models.Model):
    name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 128)
    phone = models.CharField(max_length = 10)
    state = models.CharField(max_length = 50)
    def __str__(self):
        return self.name
    
class User(AbstractUser):
    U_id = models.IntegerField()
    U_name = models.CharField(max_length = 150)
    U_genre = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
