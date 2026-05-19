from rest_framework import serializers
from .models import *


class Bookserializer(serializers.Modelserializer):
    class Meta:
        model=BooksModel
        fields='_all_'