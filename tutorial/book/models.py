from django.db import models

# Create your models here.
class BookModel(models.Model):
    name=models.charield(max_length=50)
    author=models.charfield(max_length=50)
    read_by=models.charfield(max_length=50)
