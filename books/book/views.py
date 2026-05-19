from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response




# Create your views here.
@api_view(['Get'])
def Booklist(request):
    booksobj=BookModel.objects.all()#queryset
    serializer=Bookserializer(booksobj,many=True)
    return Response(serializer.data)
#create
@api_view(['Post'])
def Post_Book(request):
    booksobj=BookModel.objects.all()#queryset
    serializer=Bookserializer(data=requset.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
#update
@api_view(['post'])
def update_Book(request,id):
    booksobj=BookModel.objects.get(id=id)#queryset
    serializer=Bookserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
#delete
@api_view(['Delete'])
def delete_Book(request):
    booksobj=BookModel.objects.get(id=id)#queryset
    booksobj.delete()
    return Response("book is deleted")