from django.contrib.auth.models import AbstractBaseUser
from django.db import models


# Create your models here.
class User(AbstractBaseUser):
    id_user = models.BigAutoField(primary_key=True)
    role = models.CharField(verbose_name="user role", max_length=20, blank=True)
    first_name = models.TextField(verbose_name="first name", blank=True)
    last_name = models.TextField(verbose_name="last name", blank=True)
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    phone_number = models.CharField(verbose_name="phone number", max_length=50, blank=True)

    USERNAME_FIELD = "email"

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email
