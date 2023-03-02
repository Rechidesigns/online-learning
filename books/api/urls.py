from django.urls import path
from . import views 

urlpatterns = [
    path('category-options/', views.Category_ViewSet.as_view() , name = 'category_options'),
    path('books/' , views.Book_View.as_view() , name = "books_view"),
]

