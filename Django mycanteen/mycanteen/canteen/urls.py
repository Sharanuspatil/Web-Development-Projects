from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="Canteenhome"),
    path('canteen', views.index, name="Canteenhome"),
    path('about/', views.about, name='about us'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path("canteen/products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("search/", views.search, name="Search"),
    path('login/',views.loginUser, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('signup/',views.signup, name="signup"),

]
