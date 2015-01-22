#!/usr/bin/env python

import subprocess
import sys
import os
import time

subprocess.call('clear', shell=True)

nmap_check="/usr/bin/nmap"
 
if ( not os.path.isfile(nmap_check)):
    print("Nmap is not installed, please visit http://nmap.org/download.html")
    sys.exit()
else:
    print("Nmap Found! Please upgrade if you have a version lower than 5.30")

subprocess.Popen(['nmap', '--version'], stdout=sys.stdout, stderr=sys.stderr)

time.sleep(5)

subprocess.call('clear', shell=True)

colorgrn = "\033[1;36m{0}\033[00m"

print colorgrn.format("\r\n      XX*************************XX")
print colorgrn.format("      XX*************************XX")	
print colorgrn.format("    **       Nmap Quick CLI        **")
print colorgrn.format("    **     Created By: Sheimo      **")
print colorgrn.format("    **    RedTeam Security Labs    **")
print colorgrn.format("    **   redteamsecure.com/labs    **")
print colorgrn.format("    **         Version:1.2         **")
print colorgrn.format("      XX*************************XX")
print colorgrn.format("      XX*************************XX\r\n")

remoteServer = raw_input("Enter remote host(s) to scan in Nmap format: ")

ans=True
while ans:
    print ("""\n[+] Zenmap Scans
    1.Intense Scan (Scans common TCP ports with version detection)
    2.Intense Scan Plus UDP (Scans common TCP + UDP ports with version detection)
    3.Fast Scan (Scans host with fewer ports than regular scan)
    4.Intense Scan, All TCP Ports (Scans all TCP ports with version detection)
    5.Intense Scan, No Ping (Scans TCP ports with version detection and does not ping host)
    6.Ping Scan (Scans host with ping scan)
    7.Regular Scan (Default nmap scan )
    8.Slow Comprehensive Scan (A slower scan to grab more accurate information on host)

[+] Firewall/Evasion Scans
    9.Idle/Zombie Scan (Scans host through an idle machine on the network)
    10.Fragment Scan (Fragment packet scan to attempt to bypass packet inspection firewalls)
    11.Append Random Data Scan (Scans host with additional data to avoid detection)
    12.MAC Address Spoof Scan (Scans host with a random MAC address)
    13.Bad Checksum Scan (Scans host with incorrect checksums)
    14.Decoy Scan (Scans host with random decoys)

[+] Nmap Scipt Scans 
    Coming Soon!
   
    99.Exit/Quit
    """)
    ans=raw_input("What would you like to do? ") 
    if ans=="1": 
     xmloutput = raw_input("Save scan in XML format? [yes|no]:")
     if xmloutput == "yes": 
      p1 = subprocess.Popen(['nmap', '-T4', '-A', '-v', '-oX', 'nmap_scan-%T-%D.xml', remoteServer], stdout=sys.stdout, stderr=sys.stderr) 
      print colorgrn.format("Scanning %s with Intense Scan please be patient...") % remoteServer
      output = p1.communicate()[0]
      print output
     if xmloutput =="no":
      p1 = subprocess.Popen(['nmap', '-T4', '-A', '-v', remoteServer], stdout=sys.stdout, stderr=sys.stderr) 
      print colorgrn.format("Scanning %s with Intense Scan please be patient...") % remoteServer
      output = p1.communicate()[0]
      print output
    if ans=="2":
     xmloutput = raw_input("Save scan in XML format? [yes|no]:")
     if xmloutput == "yes":
      p2 = subprocess.Popen(['nmap', '-sS', '-sU', '-T4', '-A', '-v', '-oX', 'nmap_scan-%T-%D.xml', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Intense Scan Plus UDP ports please be patient...") % remoteServer
      output2 = p2.communicate()[0]
      print output2
     if xmloutput == "no":
      p2 = subprocess.Popen(['nmap', '-sS', '-sU', '-T4', '-A', '-v', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Intense Scan Plus UDP ports please be patient...") % remoteServer
      output2 = p2.communicate()[0]
      print output2
    if ans=="3":
     xmloutput = raw_input("Save scan in XML format? [yes|no]:")
     if xmloutput == "yes":
      p3 = subprocess.Popen(['nmap', '-T4', '-F', '-oX', 'nmap_scan-%T-%D.xml', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Fast Scan please be patient...") % remoteServer
      output3 = p3.communicate()[0]
      print output3 
     if xmloutput == "no":
      p3 = subprocess.Popen(['nmap', '-T4', '-F', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Fast Scan please be patient...") % remoteServer
      output3 = p3.communicate()[0]
      print output3 
    if ans=="4":
     xmloutput = raw_input("Save scan in XML format? [yes|no]:")
     if xmloutput == "yes":
      p4 = subprocess.Popen(['nmap', '-p 1-65535', '-T4', '-A', '-v', '-oX', 'nmap_scan-%T-%D.xml', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Intense Scan, All TCP Ports please be patient this scan can take awhile...") % remoteServer
      output4 = p4.communicate()[0]
      print output4 
     if xmloutput == "no":
      p4 = subprocess.Popen(['nmap', '-p 1-65535', '-T4', '-A', '-v', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Intense Scan, All TCP Ports please be patient this scan can take awhile...") % remoteServer
      output4 = p4.communicate()[0]
      print output4
    if ans=="5":
     xmloutput = raw_input("Save scan in XML format? [yes|no]:")
     if xmloutput == "yes":
      p5 = subprocess.Popen(['nmap', '-p 1-65535', '-T4', '-A', '-v', '-Pn', '-oX', 'nmap_scan-%T-%D.xml', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Intense Scan, No Ping please be patient...") % remoteServer
      output5 = p5.communicate()[0]
      print output5 
     if xmloutput == "no":
      p5 = subprocess.Popen(['nmap', '-p 1-65535', '-T4', '-A', '-v', '-Pn', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Intense Scan, No Ping please be patient...") % remoteServer
      output5 = p5.communicate()[0]
      print output5 
    if ans=="6":
     xmloutput = raw_input("Save scan in XML format? [yes|no]:")
     if xmloutput == "yes":
      p6 = subprocess.Popen(['nmap', '-sn', '-oX', 'nmap_scan-%T-%D.xml', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Ping Scan please be patient...") % remoteServer
      output6 = p6.communicate()[0]
      print output6 
     if xmloutput == "no":
      p6 = subprocess.Popen(['nmap', '-sn', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Ping Scan please be patient...") % remoteServer
      output6 = p6.communicate()[0]
      print output6 
    if ans=="7":
     xmloutput = raw_input("Save scan in XML format? [yes|no]:")
     if xmloutput == "yes":
      p7 = subprocess.Popen(['nmap', '-oX', 'nmap_scan-%T-%D.xml', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Regular Scan please be patient...") % remoteServer
      output7 = p7.communicate()[0]
      print output7 
     if xmloutput == "no":
      p7 = subprocess.Popen(['nmap', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Regular Scan please be patient...") % remoteServer
      output7 = p7.communicate()[0]
      print output7 
    if ans=="8":
     xmloutput = raw_input("Save scan in XML format? [yes|no]:")
     if xmloutput == "yes":
      p8 = subprocess.Popen(['nmap', '-sS', '-sU', '-T4', '-A', '-v', '-PE', '-PP', '-PS80,443', '-PA3389', '-PU40125', '-PY', '-g 53', '--script', "default or (discovery and safe)", '-oX', 'nmap_scan-%T-%D.xml', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Slow Comprehensive Scan please be patient this scan can take awhile...") % remoteServer
      output8 = p8.communicate()[0]
      print output8 
     if xmloutput == "no":
      p8 = subprocess.Popen(['nmap', '-sS', '-sU', '-T4', '-A', '-v', '-PE', '-PP', '-PS80,443', '-PA3389', '-PU40125', '-PY', '-g 53', '--script', "default or (discovery and safe)", remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Slow Comprehensive Scan please be patient this scan can take awhile...") % remoteServer
      output8 = p8.communicate()[0]
      print output8 
    if ans=="9":
     zombie = raw_input("Please enter Zombie machine address:")
     xmloutput = raw_input("Save scan in XML format? [yes|no]:")
     if xmloutput == "yes":
      p9 = subprocess.Popen(['nmap', '-Pn', '-oX', 'nmap_scan-%T-%D.xml','-sI', zombie, remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Idle/Zombie scan please be patient...") % remoteServer
      output9 = p9.communicate()[0]
      print output9
     if xmloutput == "no":
      p9 = subprocess.Popen(['nmap', '-Pn', '-sI', zombie, remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Idle/Zombie scan please be patient...") % remoteServer
      output9 = p9.communicate()[0]
      print output9
    if ans=="10":
     xmloutput = raw_input("Save scan in XML format? [yes|no]:")
     if xmloutput == "yes":
      p10 = subprocess.Popen(['nmap', '-v', '-f' '-oX', 'nmap_scan-%T-%D.xml',  remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Fragment Scan please be patient...") % remoteServer
      output10 = p10.communicate()[0]
      print output10 
     if xmloutput == "no":
      p10 = subprocess.Popen(['nmap', '-v', '-f', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Fragment Scan please be patient...") % remoteServer
      output10 = p10.communicate()[0]
      print output10 
    if ans=="11":
     xmloutput = raw_input("Save scan in XML format? [yes|no]:")
     if xmloutput == "yes":
      p11 = subprocess.Popen(['nmap', '--data-length', '30', '-v', '-oX', 'nmap_scan-%T-%D.xml', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Append Random Data Scan please be patient...") % remoteServer
      output11 = p11.communicate()[0]
      print output11 
     if xmloutput == "no":
      p11 = subprocess.Popen(['nmap', '--data-length', '30', '-v', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Append Random Data Scan please be patient...") % remoteServer
      output11 = p11.communicate()[0]
      print output11 
    if ans=="12":
     xmloutput = raw_input("Save scan in XML format? [yes|no]:")
     if xmloutput == "yes":
      p12 = subprocess.Popen(['nmap', '--spoof-mac', '0', '-v', '-oX', 'nmap_scan-%T-%D.xml', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with MAC Address Spoof Scan please be patient...") % remoteServer
      output12 = p12.communicate()[0]
      print output12 
     if xmloutput == "no":
      p12 = subprocess.Popen(['nmap', '--spoof-mac', '0', '-v', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with MAC Address Spoof Scan please be patient...") % remoteServer
      output12 = p12.communicate()[0]
      print output12 
    if ans=="13":
     xmloutput = raw_input("Save scan in XML format? [yes|no]:")
     if xmloutput == "yes":
      p13 = subprocess.Popen(['nmap', '--badsum', '-v', '-oX', 'nmap_scan-%T-%D.xml', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Bad Checksum Scan please be patient...") % remoteServer
      output13 = p13.communicate()[0]
      print output13 
     if xmloutput == "no":
      p13 = subprocess.Popen(['nmap', '--badsum', '-v', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Bad Checksum Scan please be patient...") % remoteServer
      output13 = p13.communicate()[0]
      print output13 
    if ans=="14":
     xmloutput = raw_input("Save scan in XML format? [yes|no]:")
     if xmloutput == "yes":
      p14 = subprocess.Popen(['nmap', '-D', 'RND:10', 'v', '-oX', 'nmap_scan-%T-%D.xml', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Decoy Scan please be patient...") % remoteServer
      output14 = p14.communicate()[0]
      print output14 
     if xmloutput == "no":
      p14 = subprocess.Popen(['nmap', '-D', 'RND:10', '-v', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Decoy Scan please be patient...") % remoteServer
      output14 = p14.communicate()[0]
      print output14 
    if ans=="99":
      print("\n Thanks for checking out my script!") 
      sys.exit()
 
