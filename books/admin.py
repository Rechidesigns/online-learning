from django.contrib import admin

from .models import Books , Category 
# Register your models here.

@admin.register( Books )
class BooksAdmin (admin.ModelAdmin):
    list_display = ('author' , 'title', 'created_date' , 'modified_date')
    list_display_links = ('author' , 'title' )


@admin.register( Category )
class CategoryAdmin (admin.ModelAdmin):
    list_display = ('category_name', 'active')
    list_display_links = ('category_name', 'active')
