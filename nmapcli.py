#!/usr/bin/env python


import subprocess
import sys

subprocess.call('clear', shell=True)

colorgrn = "\033[1;36m{0}\033[00m"

print colorgrn.format("\r\n      XX*************************XX")
print colorgrn.format("      XX*************************XX")	
print colorgrn.format("    **       Nmap Quick CLI        **")
print colorgrn.format("    **     Created By: Sheimo      **")
print colorgrn.format("    **         Version:1.1         **")
print colorgrn.format("      XX*************************XX")
print colorgrn.format("      XX*************************XX\r\n")

remoteServer = raw_input("Enter remote host(s) to scan in Nmap format: ")
xmloutput = raw_input("Do you want to export to XML file? [yes|no]: ")
if xmloutput == "yes"


ans=True
while ans:
    print ("""
    1.Intense Scan (Scans common TCP ports with version detection)
    2.Intense Scan Plus UDP (Scans common TCP + UDP ports with version detection)
    3.Fast Scan (Scans host(s) with fewer ports than regular scan)
    4.Intense Scan, All TCP Ports (Scans all TCP ports with version detection)
    5.Intense Scan, No Ping (Scans TCP ports with version detection and does not ping host(s))
    6.Ping Scan (Scans host(s) with ping scan)
    7.Regular Scan (Default nmap scan )
    8.Slow Comprehensive Scan (A slower scan to grab more accurate information on host(s))
    9.Idle/Zombie Scan (Scans host(s) through an idle machine on the network)
    10. Vulnerability Scripts Scan (Loads all vulnerability scripts and scans host(s))
    99.Exit/Quit
    """)
    ans=raw_input("What would you like to do? ") 
    if ans=="1": 
     p1 = subprocess.Popen(['nmap', '-T4', '-A', '-v', remoteServer], stdout=sys.stdout, stderr=sys.stderr) 
     print ("Scanning %s with Intense Scan please be patient...") % remoteServer
     output = p1.communicate()[0]
     print output
    elif ans=="2":
      p2 = subprocess.Popen(['nmap', '-sS', '-sU', '-T4', '-A', '-v', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print ("Scanning %s with Intense Scan Plus UDP ports please be patient...") % remoteServer
      output2 = p2.communicate()[0]
      print output2
    elif ans=="3":
      p3 = subprocess.Popen(['nmap', '-T4', '-F', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print ("Scanning %s with Fast Scan please be patient...") % remoteServer
      output3 = p3.communicate()[0]
      print output3 
    elif ans=="4":
      p4 = subprocess.Popen(['nmap', '-p 1-65535', '-T4', '-A', '-v', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print ("Scanning %s with Intense Scan, All TCP Ports please be patient this scan can take awhile...") % remoteServer
      output4 = p4.communicate()[0]
      print output4 
    elif ans=="5":
      p5 = subprocess.Popen(['nmap', '-p 1-65535', '-T4', '-A', '-v', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print ("Scanning %s with Intense Scan, No Ping please be patient...") % remoteServer
      output5 = p5.communicate()[0]
      print output5 
    elif ans=="6":
      p6 = subprocess.Popen(['nmap', '-sn', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print ("Scanning %s with Ping Scan please be patient...") % remoteServer
      output6 = p6.communicate()[0]
      print output6 
    elif ans=="7":
      p7 = subprocess.Popen(['nmap', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print ("Scanning %s with Regular Scan please be patient...") % remoteServer
      output7 = p7.communicate()[0]
      print output7 
    elif ans=="8":
      p8 = subprocess.Popen(['nmap', '-sS', '-sU', '-T4', '-A', '-v', '-PE', '-PP', '-PS80,443', '-PA3389', '-PU40125', '-PY', '-g 53', '--script', "default or (discovery and safe)", remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print ("Scanning %s with Slow Comprehensive Scan please be patient this scan can take awhile...") % remoteServer
      output8 = p8.communicate()[0]
      print output8 
    elif ans=="9":
      zombie = raw_input("Please enter Zombie machine address:")
      p9 = subprocess.Popen(['nmap', '-Pn', '-sI', remoteServer, zombie], stdout=sys.stdout, stderr=sys.stderr)
      print ("Scanning %s with Idle/Zombie scan please be patient...") % remoteServer
      output9 = p9.communicate()[0]
      print output9
    elif ans=="10":
      p10 = subprocess.Popen(['nmap', '--script vuln', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print ("Scanning %s with Vulnerability Script Scan please be patient...") % remoteServer
      output10 = p10.communicate()[0]
      print output10 
    elif ans=="99":
      print("\n Thanks for checking out my script!") 
      sys.exit()
    elif ans !="":
      print("\n Not Valid Choice Try again") 
