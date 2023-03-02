from rest_framework import serializers
from books.models import Books, Category

class Book_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['title', 'category', 'book_description', 'price', 'pages', 'book_image', 'book_file', 'website', 'status']


class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_option', 'id']


class List_Property_Serializer(serializers.ModelSerializer):

    category = Category_Serializer( read_only = True )

    class Meta: 
        model = Books
        fields = ['title', 'category', 'book_description', 'price', 'pages', 'book_image', 'book_file', 'website', 'status']