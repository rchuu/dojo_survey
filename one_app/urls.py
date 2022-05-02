from django.urls import path
from . import views

urlpatterns = [
    path('', views.form),
    path('process', views.process),
    path('dashboard', views.dashboard),
]
