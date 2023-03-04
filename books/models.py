from django.db import models

from django.utils.translation import gettext_lazy as _

# Custom Apps 
from helpers.common.basemodel import BaseModel
from online_learning.users.models import User


class Category (models.Model):
    category_name = models.CharField(
        verbose_name= _('Category_option'),
        max_length= 225,
        null= False,
        blank= False,
        help_text= _('this name belongs to the category of the book')
    )

    active = models.BooleanField(
        verbose_name=_("Active"),
        default=False,
        null=True,
        blank=True,
        help_text=_(" this indicates if the active option type is enabled or not ")
    )

    def __str__(self):
        return self.category_name
      

    class Meta:
        verbose_name = _("All Book Category")
        verbose_name_plural = _("All Books Category")



STATUS = (("Unpublished","Unpublished"), 
              ("Published","Published"))

class Books (BaseModel):
    """
    this model holds the properties list for the owner
    """

    author = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        verbose_name = _('Author of the book'),
        related_name = "Books_author",
        null = True,
        help_text=_(' this profile belongs to the author  who owns this book ')
    )

    book_category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,
        verbose_name = _('Category'),
        null= True,
        help_text =_("Category type refers to the type of the book based on the category")
    )

    title = models.CharField(
        verbose_name = _('Title'),
        max_length = 250,
        null = True,
        blank= True,
        help_text =_('this is the title of the book given  by the author')
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

    date_time_added = models.DateTimeField(
        verbose_name = _('Date & Time Added'),
        auto_now_add= True,
        null= True,
        help_text= _('Date and time'),
    )

    # def __str__(self):
    #     return str(self.author)

    def __str__(self):
        return f"{self.author} {self.title} ({self.book_category})"

    class Meta:
        ordering = ('-created_date',)
        verbose_name = _('All Authors Book')
        verbose_name_plural = _('All Authors Book')



