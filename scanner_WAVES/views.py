from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Logica del proyecto

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)



