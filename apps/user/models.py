from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.exclude(email__isnull=True).get(**{self.model.USERNAME_FIELD: email})

    def create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("role", "admin")

        return self.create_user(email, password, **extra_fields)


# Create your models here.
class User(AbstractBaseUser):
    id_user = models.BigAutoField(primary_key=True)
    role = models.CharField(verbose_name="user role", max_length=20, blank=True)
    first_name = models.TextField(verbose_name="first name", blank=True)
    last_name = models.TextField(verbose_name="last name", blank=True)
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    phone_number = models.CharField(verbose_name="phone number", max_length=50, blank=True)

    objects = UserManager()
    USERNAME_FIELD = "email"

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email
