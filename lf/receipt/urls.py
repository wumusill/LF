from django.urls import path
import views

urlpatterns = [
    path('urlname', views.functionname, name=''),
]