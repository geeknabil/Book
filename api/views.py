from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.http import Http404

from api.models import Book
from api.serializers import BookSerializer

# list and create books
class Book_List(APIView):
    def get(self, request):
        books = Book.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(result_page, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BookSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )


# get specific book, update and delete
class Book_pk(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExists:
            raise Http404
    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Find book
class Book_Find(APIView):    
    def get(self, request):
        books = Book.objects.filter(
            genre__in = request.data.getlist('genre'),
        )
        serializer = BookSerializer(books, many= True)
        return Response(serializer.data)
