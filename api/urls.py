from django.urls import path
from api import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view())
]