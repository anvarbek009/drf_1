from django.urls import path
from .views import ListCategoryApiView


urlpatterns = [
    path('category/',ListCategoryApiView.as_view(),name='category') 
]