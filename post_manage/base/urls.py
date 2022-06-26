from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('create',views.createView,name = 'create'),
    path('delete/<str:pk>',views.deleteView,name = 'delete'),
    path('edit/<str:pk>',views.editView,name = 'edit'),
]