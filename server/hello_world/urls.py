from django.urls import path
from . import views

app_name = "hello_world"

urlpatterns = [
    path('hello-world/', views.HelloWorldListView.as_view(), name='hello-world-list'),
]
