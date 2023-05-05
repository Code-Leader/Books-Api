from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# function based view in DRF
@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)