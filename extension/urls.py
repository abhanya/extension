from django.urls import path
from . import views

urlpatterns = [
    path('master',views.extension_master,name='mast'),
    path('',views.extension_home,name='home'),
    path('about',views.extension_about,name='about'),
    path('contact',views.extension_contact,name='contact'),
]