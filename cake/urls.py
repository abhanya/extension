from django.urls import path
from . import views

urlpatterns = [
    path('cakes',views.cake_main,name="cakes"),
    path('home',views.cake_home,name="home"),
    path('cnt',views.cake_cont,name="contact"),
    path('aboutus',views.cake_abt,name="about"),
    path('graduation',views.cake_graduation,name="grad"),
    path('deserts',views.cake_desert,name="dsrt"),
    path('snacks',views.cake_snacks,name="sna"),
]
