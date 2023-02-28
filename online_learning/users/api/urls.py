from django.urls import path
from users.api import views

urlpatterns = [

    path('create-account', views.Register_Account.as_view() , name = 'create_account'),
    
]