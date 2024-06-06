from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/',views.about_us,name='about'),
    path('services/',views.services,name='services'),
    path('book-it/',views.book_it,name='book-it'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact/',views.contact_us,name='contact')

]