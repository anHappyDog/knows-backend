from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
import uuid


# Create your models here.
class User(models.Model):
    userid = models.UUIDField(primary_key=True, auto_created=True, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=40, null=False)
    password = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=40, null=False)
    phone = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        db_table = "user"
