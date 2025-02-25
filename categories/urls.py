
from django.urls import path

from .views import index, detail
urlpatterns = [
    path('', index, name='ui'),
    path('category/<int:aba>', detail, name='detail'),
]