from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


# Bunda biz obyektalni ro'yhat ko'rinshda chiqramiz
# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):

    def get(self,request):
        books = Book.objects.all()
        serializer_deta = BookSerializer(books, many=True).data
        data = {
            'status': f"Returned {len(books)} books",
            'books': serializer_deta

        }
        return Response(data)


# bunda biz obyktlarni malumtini olamiz
# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApiView(APIView):

    def get(self,request, pk):
        try:

            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data

            data = {
                "status": "Successfull",
                "book": serializer_data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {"status": "False",
                 "message": "Book is not found"}, status=status.HTTP_404_NOT_FOUND
            )



# bunda biz obyektni ochirib yuborishimiz mumkun
# class BookDeleteApiView(generics.DestroyAPIView): 
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                "status": True,
                "message": "Successfull deleted"
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                            {"status": "False",
                             "message": "Book is not found"
                             }, status=status.HTTP_400_BAD_REQUEST
                        )


# bunda biz obyektni ozgaritishimiz mumkun yani edit qilshimiz mumkun
# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()

        return Response(
            {
                'status': True,
                'message': f"Book {book_saved} updated Successfully"
            }
        )




# bunda biz obiyekt yartishimiz mumkun
# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serailazer = BookSerializer(data=data)
        if serailazer.is_valid(raise_exception=True):
            books = serailazer.save()

            data = {'satus': "Books are saved to the detabase",
                    'books': data
                    }
            
            return Response(data)




# bunda biz obeyktin korishimiz hamda yarishimiz mumkun
class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# bunda biz obyektni edit qishimz hamda ochirishimiz mumkun
class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# function based view in DRF
@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)