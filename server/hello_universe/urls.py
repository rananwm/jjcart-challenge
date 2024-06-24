from django.urls import path
from . import views

app_name = "hello_universe"

urlpatterns = [
    path('hello-universe/', views.HelloUniverseListView.as_view(), name='hello-universe-list'),
]
