from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import  CreateAPIView, ListCreateAPIView , ListAPIView

from .serializers import Book_Serializer, Category_Serializer
from books.models import Books, Category


class Category_ViewSet ( ListCreateAPIView ):

    permission_classes = [ IsAuthenticated]
    serializer_class = Category_Serializer

    def post ( self, request , *args, **kwargs ):
        serializer = self.serializer_class( data = request.data )
        if serializer.is_valid():
            serializer.save()

            return Response( {'status':'successful', 'message':'Category has been added successfully','data':serializer.data} , status = status.HTTP_201_CREATED )

        return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)


    def get ( self, request , *args, **kwargs ):
        qs = Category.objects.all()
        serializer = Category_Serializer(qs , many = True)
        return Response( {'status':'successful', 'message':'Categories of the books has been fetched','data':serializer.data } , status=status.HTTP_201_CREATED )
   


class Book_View(ListCreateAPIView):

    permission_classes = [ IsAuthenticated ]
    serializer_class = Book_Serializer

    def post ( self, request , *args, **kwargs ):
        serializer = self.serializer_class( data = request.data )
        if serializer.is_valid():
            serializer.save( Author = request.user )

            return Response( {'status':'successful', 'message':'Book has been uploaded successful','data':serializer.data} , status = status.HTTP_201_CREATED )

        return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)


    def get ( self, request , *args, **kwargs ):
        qs = Books.objects.all()
        serializer = Book_Serializer(qs , many = True)
        return Response( {'status':'successful', 'message':'Authors books has been fetched','data':serializer.data } , status=status.HTTP_201_CREATED )
    
