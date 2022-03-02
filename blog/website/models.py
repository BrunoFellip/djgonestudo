from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
