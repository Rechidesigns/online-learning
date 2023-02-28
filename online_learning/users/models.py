
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.conf import settings

import uuid



class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_('The given email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, **extra_fields)



class User(AbstractUser):
    """Default user for estate management system."""
    objects = UserManager()

    ACCOUNT_TYPE = (
        ('Author', _('Author')),
        ('Reader', _('Reader')),
        
    )


    id = models.UUIDField(
        default = uuid.uuid4,
        editable=False,
        primary_key=True,
        help_text=_("The unique identifier of the customer.")
    )

     #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)

    email = models.EmailField(
        max_length=150,
        null=True,
        unique=True,
        verbose_name=_("Email Address"),
        help_text=_("The email address of the customer.")
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    username = None


    first_name = models.CharField(
        verbose_name=_("First names"),
        max_length=50,
        null=True,
        help_text=_("The first names of the customer.")
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name=_("Last names"),
        null=True,
        help_text=_("The last names of the customer.")
    ) 

    contact_number = models.CharField(
        max_length=50,
        verbose_name=_("Contact Number"),
        null=True,
        help_text=_("contact number of the customer.")
    ) 

    # phone = PhoneNumberField(null=True, blank=False, unique=True)

    home_address = models.CharField(
        max_length=250,
        verbose_name=_("Home Address"),
        null=True,
        blank = True,
        help_text=_("this holds the home address of the user.")
    ) 
    
    account_type = models.CharField(
        choices=ACCOUNT_TYPE,
        verbose_name=_("Account Type"),
        max_length=50,
        null=True,
        blank=True,
        help_text = _("Account type is used to identify the account user either the landlord or the tenant.")
    )

    class Meta:
        verbose_name = _("users  Account")
        verbose_name_plural = _("users  Account")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"



