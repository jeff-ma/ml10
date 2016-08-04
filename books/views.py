from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Book

class Book_list(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class Book_detail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(('GET',))
def root(request, format=None):
    return Response({
        'books': reverse('Book_list', request=request, format=format),
    })

