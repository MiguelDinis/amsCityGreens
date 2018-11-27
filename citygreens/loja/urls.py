from django.urls import path
from . import views

urlpatterns = [
    path('loja/', views.home, name='loja-home'),

]
