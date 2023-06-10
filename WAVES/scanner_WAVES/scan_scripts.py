import os
import re
import ssl
import json
import requests
import urllib.request
from urllib.request import Request
from cpedictionary import technology_cpe_dictionary
from pyExploitDb import PyExploitDb

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"
NVD_apikey = os.environ['NVD_API_KEY']
NVD_urlapi = "https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName="
ExploitDB_url = "https://www.exploit-db.com/exploits/"
hdrs = {'apiKey' : '%s' % NVD_apikey}
pEdb = PyExploitDb()
pEdb.debug = False
pEdb.openFile()
# Target Information

ip = "10.10.215.11"
port = "80"
target = "http://"+ip+":"+port



#def ip_or_domain():
#    

def web_server_grabbing():
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', USER_AGENT)]
        #urllib.request.install_opener(opener)
        #gcontext = ssl.SSLContext()
        #response = urllib.request.urlopen(target, context=gcontext)
        response = urllib.request.urlopen(target)
        print("Web Application Information")
        print("----------------------------")
        print("Scanning IP: " + ip + " on port: " + port)
        print("----------------------------")
        for header, value in response.getheaders(): # For getting web headers
            if header == ("Server" or "server"):
                webserver = ""
                webserver = value
                print("Web Server: " + webserver)
                cpe_webserver = technology_cpe_dictionary[webserver]
                print("CPE Detected: " + cpe_webserver)
                print("----------------------------")
                response = requests.get(NVD_urlapi+cpe_webserver, headers=hdrs)
                data = json.loads(response.text)

                results = data["resultsPerPage"] # Total of CVEs detected

                for n in range(0, int(results)): # For getting eache CVE
                    cve = data["vulnerabilities"][n]["cve"]["id"]
                    print(cve)
                    exploit = pEdb.searchCve(cve)
                    #print(exploit)
                    if exploit != []:
                        print("Available exploit detected! : " +exploit["description"])
                        print("Check the following link: " + ExploitDB_url+exploit["id"])
                    else:
                        print("Exploit not available yet")
                    print(data["vulnerabilities"][n]["cve"]["descriptions"][0]["value"])
                    if "cvssMetricV2" in data["vulnerabilities"][n]["cve"]["metrics"]:
                        print("CVSS v2 Score: " + str(data["vulnerabilities"][n]["cve"]["metrics"]["cvssMetricV2"][0]["impactScore"]))
                    else:
                        print("CVSS v3.1 Score: " + str(data["vulnerabilities"][n]["cve"]["metrics"]["cvssMetricV31"][0]["impactScore"]))
                    print("----------------------------")

            if header == ("X-Powered-By" or "X-Generator"):
                webframework = ""
                webframework = value
                print("Web Framework: " + webframework)
                cpe_webframework = technology_cpe_dictionary[webframework]
                print("CPE Detected:" + cpe_webframework)
                print("----------------------------")
                response = requests.get(NVD_urlapi+cpe_webframework, headers=hdrs)
                data = json.loads(response.text)

                results = data["resultsPerPage"]

                for n in range(0, int(results)):
                    cve = data["vulnerabilities"][n]["cve"]["id"]
                    print(cve)
                    exploit = pEdb.searchCve(cve)
                    #print(exploit)
                    if exploit != []:
                        print("Available exploit detected! : " +exploit["description"])
                        print("Check the following link: " + ExploitDB_url+exploit["id"])
                    else:
                        print("Exploit not available yet")
                    print(data["vulnerabilities"][n]["cve"]["descriptions"][0]["value"])
                    if "cvssMetricV2" in data["vulnerabilities"][n]["cve"]["metrics"]:
                        print("CVSS v2 Score: " + str(data["vulnerabilities"][n]["cve"]["metrics"]["cvssMetricV2"][0]["impactScore"]))
                    else:
                        print("CVSS v3.1 Score: " + str(data["vulnerabilities"][n]["cve"]["metrics"]["cvssMetricV31"][0]["impactScore"]))
                    print("----------------------------")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    web_server_grabbing()
