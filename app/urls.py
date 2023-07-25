from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.About, name = 'About'),
    path('services/', views.services, name ='service'),
    path('menu/', views.menu, name = 'menu'),
    path('signin/', views.Signin, name='signin'),
    path('login/', views.Login, name='login'),
    path('contact/', views.contact, name ='contact'),
    path('booking/', views.booking, name = 'booking'),
    path('testimonial/', views.testimonial, name = 'testimonial'),
    path('team/', views.team, name = 'team'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.login, name='login'),

]