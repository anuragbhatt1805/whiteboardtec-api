from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


# Manager for User
class UserManager(BaseUserManager):
    def create_user(self, password, **extra_fields):
        """Create and save a new user"""
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password, **extra_fields):
        """Create and save a new superuser"""
        user = self.create_user(password, **extra_fields)
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Model for User
class UserModel(AbstractBaseUser, PermissionsMixin):
    """
    Custome user model for staff of WhiteBoard Technologies
    """
    username = models.CharField(max_length=255, unique=True)

    # Required fields
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=255)
    phone = models.CharField(max_length=16)
    date_joined = models.DateField(auto_now_add=True)

    # Boolean fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'role', 'phone']

    def __str__(self):
        return self.username