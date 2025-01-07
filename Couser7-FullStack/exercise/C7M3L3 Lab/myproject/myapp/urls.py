from . import views
from django.urls import path

urlpatterns = [
    path('menu', views.form_view, name="menu"),
]