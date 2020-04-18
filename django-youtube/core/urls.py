from .views import index, like,dislike,classification

from django.urls import path

urlpatterns = [
    path("",index, name='index'),
    path("like/<str:pk>",like, name='like'),
    path("dislike/<str:pk>",dislike, name='dislike'),
    path("classification/",classification, name='classification')
]