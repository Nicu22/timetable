from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=20, default="John")
    join_date = models.DateField(auto_now=True)
    is_admin = models.BooleanField(default=False)

