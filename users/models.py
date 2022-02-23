from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """유저모델 입니다 :)"""

    bio = models.TextField(default="")
