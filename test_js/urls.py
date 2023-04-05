from django.urls import path
from . import views

urlpatterns = [
    path('todo',views.test_todo,name='tst'),
]