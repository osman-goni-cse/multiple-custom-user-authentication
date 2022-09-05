from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .validators import validate_file_size, validate_file_extension

from .managers import ApplicantRegisterManager

# Create your models here.

class Account(AbstractBaseUser, PermissionsMixin):

  is_applicant = models.BooleanField(default=False)
  is_circular_admin = models.BooleanField(default=False)
  is_department_admin = models.BooleanField(default=False)
  is_cs_admin = models.BooleanField(default=False)
  is_super_admin = models.BooleanField(default=False)

  is_staff = models.BooleanField(default=False)
  is_admin = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)

  email = models.EmailField(unique=True)
  password = models.CharField(max_length=200)

  last_login = models.DateField(verbose_name='last login', auto_now=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = ApplicantRegisterManager()

  def __str__(self):
    return self.email

 
class ApplicantRegister(models.Model):

  user = models.OneToOneField(Account, on_delete=models.CASCADE)

  applicant_name = models.CharField(max_length=200)
  confirm_email = models.EmailField()
  confirm_password = models.CharField(max_length=200)
  is_active = models.BooleanField(default=False)

  # facebook_id = models.URLField(blank=True)

  # profile_pic = models.ImageField(upload_to='profile_pics', validators=[validate_file_size, validate_file_extension])  


  def __str__(self):
    return self.user.email


class CircularRegister(models.Model):

  user = models.OneToOneField(Account, on_delete=models.CASCADE)
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return self.user.email

class AddCircular(models.Model):
  user = models.ForeignKey(Account, on_delete=models.CASCADE)
  department_name = models.CharField(max_length=200)
  post_name = models.CharField(max_length=200)

  def __str__(self):
    return self.user.email + " " + self.department_name

