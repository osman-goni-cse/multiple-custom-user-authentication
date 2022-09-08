from django.db import models
from registration_app.models import Account

# Create your models here.

class Memorandum(models.Model):
  memorandum_with_date = models.CharField(max_length=200, unique=True)

  def __str__(self):
    return self.memorandum_with_date

class JobPost(models.Model):
  post = models.CharField(max_length=200, unique=True)

  def __str__(self):
    return self.post

class NewCircular(models.Model):
  user = models.ForeignKey(Account, on_delete=models.CASCADE)
  memorandum_with_date = models.ForeignKey(Memorandum, on_delete=models.CASCADE)
  post = models.ForeignKey(JobPost, on_delete=models.CASCADE)

  def __str__(self):
    return self.user.email + " " + self.post.post
