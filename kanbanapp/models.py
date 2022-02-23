from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField
import os
from uuid import uuid4


class User(AbstractUser):
    pass

class Board(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name="boards", on_delete=models.CASCADE)

    def __str__(self):
        return self.board_name