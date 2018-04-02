from django.urls import path
from book import views

urlpatterns = [
    path('create/', views.createBook, name='createBook'),
    path('books/', views.getAllBooks, name='getAllBooks'),
    path('update/<int:idBook>/', views.updateBook, name='updateBook'),
    path('delete/<int:idBook>/', views.deleteBook, name='deleteBook'),
    path('<int:idBook>/', views.getBook, name='getBook'),
]