from django.db import models

from django.utils.translation import gettext_lazy as _

# Custom Apps 
from helpers.common.basemodel import BaseModel
from online_learning.users.models import User


class Category (models.Model):
    name = models.CharField(
        verbose_name= _('Category_name'),
        max_length= 225,
        null= False,
        blank= False,
        help_text= _('this name belongs to the category of the book')
    )

    description = models.CharField(
        verbose_name= _('description'),
        max_length= 500,
        null= True,
        blank = True,
        help_text= _('this is the description of the category of book')
    )

    def __str__(self) -> str:
        return self.name
      
    class Meta:
        verbose_name = _("All Book Category")
        verbose_name_plural = _("All Books Category")






STATUS = (("Unpublished","Unpublished"), 
              ("Published","Published"))


class Books (BaseModel):
    """
    this model holds the properties list for the owner
    """

    books = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        verbose_name = _('Author of the book'),
        related_name = "Books_author",
        null = True,
        help_text=_(' this profile belongs to the author  who owns this book ')
    )

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        verbose_name= _(' Book Category'),
        null= False,
        blank= False,
        help_text= _(' this category name of the book')
    )

    title = models.CharField(
        verbose_name= _('Title'),
        max_length= 250,
        null = True,
        blank= True,
        help_text=_('the address one is basically the defualt address of the property')
    )

    book_description = models.TextField(
        verbose_name= _('Book Description'),
        null= True,
        blank= True,
        help_text= _('the description of what the book is all about')
    )


    price = models.CharField(
        verbose_name= _('Book Price'),
        max_length=50,
        null = True,
        blank= True,
        help_text= _('this is the amount the book is sold')
    )

    pages = models.IntegerField(
        verbose_name = _('Numbers of book pages'),
        null = True,
        blank= True,
        help_text= _('this is the number of pages of the book')
    )

    book_image = models.ImageField(
        verbose_name = _('Book Image'),
        upload_to = "photos/books_image",
        null =True,
        blank=True,
        help_text= _('Book images for the current  book, which should be in PNG, JPEG, or JPG format')
    )

    book_file = models.FileField(
        verbose_name = _('Book File'),
        upload_to = "PDF/Books_file",
        null =True,
        blank=True,
        help_text= _('Book file for the current book, which should be in PDF format')
    )

    website = models.URLField(
        verbose_name= _('Portfolio Website'),
        max_length=250,
        null= True,
        blank= True,
        help_text= _('Portfolio website for the authur of the book')
    )

    status = models.CharField(
        verbose_name= _('Status'),
        choices= STATUS,
        default= 'Unpublished',
        max_length=30,
        help_text= _('Status of the book')
    )


    def __str__(self):
        return str(self.Author)

    class Meta:
        ordering = ('-created_date',)
        verbose_name = _('All Authors Book')
        verbose_name_plural = _('All Authors Book')



