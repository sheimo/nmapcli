
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
    **    RedTeam Security Labs    **
    **   redteamsecure.com/labs    **
    **         Version:1.2         **
      XX*************************XX
      XX*************************XX

Enter remote host(s) to scan in Nmap format: 192.168.1.1

[+] Zenmap Scans
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
    
What would you like to do? 
