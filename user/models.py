from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from main.models import Sight

class UserManager(BaseUserManager):

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Please enter your email')
        
        user = self.model(
            email = UserManager.normalize_email(email),
            name = name,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password = password,
            name = name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.CharField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    gym = models.ManyToManyField(Sight, blank=True)
    name = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
        
    @property
    def is_staff(self):
        return self.is_admin