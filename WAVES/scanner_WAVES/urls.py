from scanner_WAVES import views
from django.urls import path

urlpatterns = [
    path('', views.scanner, name='scan'),
    path('', views.history, name='history'),
    path('', views.reports, name='history'),
    ]   