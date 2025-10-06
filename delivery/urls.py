from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('open_signIn/', views.open_signIn, name ='open_signIn'),
    path('open_signUp/',views.open_signUp, name='open_signUp'),
    path('signUp/',views.signUp, name='signUp'),
    path('signIn/',views.signIn, name = 'signIn'),
    path('signIn/open_add_restaurant/',views.open_add_restaurant, name='open_add_restaurant'),
    path('signIn/open_show_restaurant/',views.open_show_restaurant, name='open_show_restaurant'),
    path('add_restaurant/',views.add_restaurant, name="add_restaurant"),
    path('add_restaurant/open_update_restaurant/<int:restaurant_id>', views.open_update_restaurant,name="open_update_restaurant"),
    path('add_restaurant/delete_restaurant/<int:restaurant_id>', views.delete_restaurant,name="delete_restaurant"),
    path('update_restaurant/<int:restaurant_id>', views.update_restaurant,name="update_restaurant"),
    path('delete_restaurant',views.delete_restaurant,name="delete_restaurant"),
    path('open_update_menu/<int:restaurant_id>/', views.open_update_menu, name="open_update_menu"),
    path('update_menu/<int:restaurant_id>/', views.update_menu, name="update_menu"),
    #path('view_menu/<int:restaurant_id>',views.view_menu,name='view_menu'), 
    path('view_menu/<int:restaurant_id>/<str:username>/', views.view_menu, name='view_menu'),


]