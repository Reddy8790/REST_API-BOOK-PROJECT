from django.db import models

# Create your models here.
class BookModel(models.Model):
    name=models.CharField(max_length=50)
    author=model.CharField(max_length=50)
    read_by=CharField(max_length=50)