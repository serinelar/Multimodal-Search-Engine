from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('item/<int:item_id>/', views.detail, name='detail'), 
]
