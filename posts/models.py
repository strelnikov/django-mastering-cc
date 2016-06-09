from django.db import models
from accounts.models import Account


class Post(models.Model):
    author = models.ForeignKey(Account)
    # comments = models.ManyToManyField(Account)
    title = models.CharField(max_length=255)
    url = models.SlugField(max_length=255, blank=True)
    content = models.TextField(max_length=1000)

    date_created = models.DateTimeField(auto_now_add=True)

    tags = models.CharField(max_length=20, blank=True)

    file = models.FileField(upload_to='/uploads/', null=True, blank=True)

    def __str__(self):
        return self.title


