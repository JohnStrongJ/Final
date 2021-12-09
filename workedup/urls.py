from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('browse/', views.browse, name='browse'),
    path('view_recipe/<int:id>', views.view_recipe, name='view_recipe'),
    path('manage_recipe/<int:id>', views.manage_recipe, name='manage_recipe'),
    path('delete_recipe/<int:id>', views.delete_recipe, name='delete_recipe'),
    path('toggle_favorite/<int:id>', views.toggle_favorite, name='toggle_favorite'),
    path('favorites', views.favorites, name='favorites'),
]
