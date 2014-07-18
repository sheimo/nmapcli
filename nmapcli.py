#!/usr/bin/env python


import subprocess
import sys


subprocess.call('clear', shell=True)

print "\r\n      *************************"	
print "      *   Nmap Quick CLI      *"
print "      *   By: Sheimo          *"
print "      *************************\r\n"

remoteServer = raw_input("Enter remote host(s) to scan in Nmap format: ")


ans=True
while ans:
    print ("""
    1.Intense scan (!Description of what scan does)
    2.Intense scan plus UDP (!Description of what scan does)
    3.Fast scan (!Description of what scan does)
    4.Intense scan, all TCP ports (!Description of what scan does)
    5.Intense scan, no ping (!Description of what scan does)
    6.Ping scan (!Description of what scan does)
    7.Regular scan (!Description of what scan does)
    8.Slow comprehensive scan (!Description of what scan does)
    9.Exit/Quit
    """)
    ans=raw_input("What would you like to do? ") 
    if ans=="1": 
     p1 = subprocess.Popen(['nmap', '-T4', '-A', '-v', remoteServer], stdout=subprocess.PIPE) 
     print ("Scanning %s be patient foo") % remoteServer
     output = p1.communicate()[0]
     print output
    elif ans=="2":
      p2 = subprocess.Popen(['nmap', '-sS', '-sU', '-T4', '-A', '-v', remoteServer], stdout=subprocess.PIPE)
      print ("Scanning %s be patient foo") % remoteServer
      output2 = p2.communicate()[0]
      print output2
    elif ans=="3":
      p3 = subprocess.Popen(['nmap', '-T4', '-F', remoteServer], stdout=subprocess.PIPE)
      print ("Scanning %s be patient foo") % remoteServer
      output3 = p3.communicate()[0]
      print output3 
    elif ans=="4":
      p4 = subprocess.Popen(['nmap', '-p 1-65535', '-T4', '-A', '-v', remoteServer], stdout=subprocess.PIPE)
      print ("Scanning %s be patient foo") % remoteServer
      output4 = p4.communicate()[0]
      print output4 
    elif ans=="5":
      p5 = subprocess.Popen(['nmap', '-p 1-65535', '-T4', '-A', '-v', remoteServer], stdout=subprocess.PIPE)
      print ("Scanning %s be patient foo") % remoteServer
      output5 = p5.communicate()[0]
      print output5 
    elif ans=="6":
      p6 = subprocess.Popen(['nmap', '-sn', remoteServer], stdout=subprocess.PIPE)
      print ("Scanning %s be patient foo") % remoteServer
      output6 = p6.communicate()[0]
      print output6 
    elif ans=="7":
      p7 = subprocess.Popen(['nmap', remoteServer], stdout=subprocess.PIPE)
      print ("Scanning %s be patient foo") % remoteServer
      output7 = p7.communicate()[0]
      print output7 
    elif ans=="8":
      p8 = subprocess.Popen(['nmap', '-sS', '-sU', '-T4', '-A', '-v', '-PE', '-PP', '-PS80,443', '-PA3389', '-PU40125', '-PY', '-g 53', '--script', "default or (discovery and safe)", remoteServer], stdout=subprocess.PIPE)
      print ("Scanning %s be patient foo") % remoteServer
      output8 = p8.communicate()[0]
      print output8 
    elif ans=="9":
      print("\n Goodbye") 
      sys.exit()
    elif ans !="":
      print("\n Not Valid Choice Try again") 
