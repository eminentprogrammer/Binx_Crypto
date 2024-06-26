import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# def generateUserId():
#     id = str(uuid.uuid4()).replace('-','')
#     return str(id)

# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not username:
#             raise ValueError('Users must have a username')

#         user = self.model(
#             id = generateUserId(),
#             email=self.normalize_email(email),
#             username=username,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password):  
#         user = self.create_user(email, username, password=password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

# class Account(AbstractBaseUser, PermissionsMixin):
#     id          = models.UUIDField(primary_key=True, unique=True, blank=True)
#     email       = models.EmailField(verbose_name='email', max_length=60, unique=True)
#     username    = models.CharField(max_length=30, unique=True)
#     tel         = models.CharField(max_length=11, unique=True)
#     customer_id = models.CharField(max_length=500, blank=True, null=True)
    
   
#     is_admin        = models.BooleanField(default=False)
#     is_active       = models.BooleanField(default=True)
#     is_staff        = models.BooleanField(default=False)
#     is_superuser    = models.BooleanField(default=False)
    
#     date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#     objects = MyAccountManager()
    
#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_admin