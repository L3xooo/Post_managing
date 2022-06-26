from django.db import models

# Create your models here.
class Post(models.Model):
    id       = models.IntegerField(primary_key=True)
    userId   = models.IntegerField()
    title    = models.CharField(max_length=200)
    body     = models.TextField()
