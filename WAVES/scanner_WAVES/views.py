from django.shortcuts import render
from django.http import HttpResponse
import os
import json
import requests
import urllib.request
#from apps import technology_cpe_dictionary
from pyExploitDb import PyExploitDb


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"
NVD_apikey = os.environ['NVD_API_KEY']
NVD_urlapi = "https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName="
ExploitDB_url = "https://www.exploit-db.com/exploits/"
hdrs = {'apiKey' : '%s' % NVD_apikey}

# Logica del proyecto
def scan_target(ip, port):
    target="http://"+ip+":"+port
    return target

def scanner(request):
    return HttpResponse("WAVES Vulnerability Scanner")


def history(request):
    return HttpResponse("Report History of WAVES Vulnerability Scanner")


def reports(request):
    return HttpResponse("Reports of WAVES Vulnerability Scanner")



