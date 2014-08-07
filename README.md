Update 8/7/2014  

I'm going to start putting these into different categories such as Zenmap templates, firewall scans, script scans etc.  Email me if you have any creative scans to add.

Thanks

Nmap Command Line Interface
=======
nmapcli is a tool with pre defined scan templates to automate Nmap scans.  I'm going to keep adding new scan types all the time.

Usage: ./nmapcli.py

      XX*************************XX
      XX*************************XX
    **       Nmap Quick CLI        **
    **     Created By: Sheimo      **
    **         Version:1.1         **
      XX*************************XX
      XX*************************XX

Enter remote host(s) to scan in Nmap format: 192.168.1.5

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
    
What would you like to do? 
