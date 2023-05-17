from django.conf.urls import url
from scanner_WAVES import views


urlpatterns = [

    url(r'^api/scanner/$', views)
    
    ]