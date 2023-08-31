from django.urls import path

from catalog.views import index

from catalog.views import catalog



urlpatterns = [
    path(' ', index),
    path('catalog/', control_2)
]