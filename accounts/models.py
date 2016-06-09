from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(models.Model):
    user = models.ForeignKey(User)
    full_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        if self.full_name:
            return self.full_name

        return str(self.user)
