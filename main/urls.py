from django.urls import path
from .views import data, index

urlpatterns = [
	path('data/', data),
	path('', index)
]