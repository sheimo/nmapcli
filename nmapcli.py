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
print colorgrn.format("    **         Version:2.0         **")
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
    15.Address Scan (Shows extra information about IPv6 addresses, such as embedded MAC or IPv4 addresses when available)
    16.AFP Ls Scan (Attempts to get useful information about files from AFP volumes)
    17.AFP Path Vuln Scan (Detects the Mac OS X AFP directory traversal vulnerability, CVE-2010-0533)
    18.AFP Server Information (Shows AFP server information)
    19.Banner Scan (A simple banner grabber which connects to an open TCP port and prints out anything sent by the listening service within five seconds)
    20.Broadcast DNS Service Discovery (Attempts to discover hosts' services using the DNS Service Discovery protocol)
    21.Broadcast UPNP Information (Attempts to extract system information from the UPnP service by sending a multicast query, then collecting, parsing, and displaying all responses)
    22.Citrix Server Enumeration (Extracts a list of Citrix servers from the ICA Browser service)
    23.Credentials Summary (Lists all discovered credentials (e.g. from brute force and default password checking scripts) at end of scan)
    24.DHCP Discover (DHCP request that returns useful information from a DHCP server)
    25.DNS Brute (Attempts to enumerate DNS hostnames by brute force guessing of common subdomains)
    26.DNS Check Zone (Checks DNS zone configuration against best practices, including RFC 1912)
    27.DNS Fuzz (Launches a DNS fuzzing attack against DNS servers)
    28.DNS SEC (Enumerates DNS names using the DNSSEC NSEC-walking technique)
    29.DNS SRV Enumeration (Enumerates various common service (SRV) records for a given domain name)
    30.DNS Zone Transfer (Requests a zone transfer (AXFR) from a DNS server)
    31.Duplicate (Attempts to discover multihomed systems by analysing and comparing information collected by other scripts)
    32.Firewalk (Tries to discover firewall rules using an IP TTL expiration technique known as firewalking)
    33.FTP Anonymous (Checks if an FTP server allows anonymous logins)
    34.FTP Bounce (Checks to see if an FTP server allows port scanning using the FTP bounce method)
    35.FTP Brute (Performs brute force password auditing against FTP servers)
    36.FTP ProFTP Backdoor (Tests for the presence of the ProFTPD 1.3.3c backdoor reported as OSVDB-ID 69562)
    37.FTP VsFTP Backdoor (Tests for the presence of the vsFTPd 2.3.4 backdoor reported on 2011-07-04 (CVE-2011-2523))
    38.FTP ProFTP Vuln (Checks for a stack-based buffer overflow in the ProFTPD server, version between 1.3.2rc3 and 1.3.3b)
    39.Coldfusion APSA1301 Vuln (Attempts to exploit an authentication bypass vulnerability in Adobe Coldfusion servers)
    40.HTTP Auth Finder (Spiders a web site to find web pages requiring form-based or HTTP-based authentication)
    41.HTTP Auth (Retrieves the authentication scheme and realm of a web service that requires authentication)
    42.HTTP Backup Finder (Spiders a website and attempts to identify backup copies of discovered files)
    43.HTTP Baracuda Dir Traversal (Attempts to retrieve the configuration settings from a Barracuda Networks Spam & Virus Firewall device using the directory traversal vulnerability)
    44.HTTP Brute (Performs brute force password auditing against http basic authentication)
    45.HTTP Config Backups (Checks for backups and swap files of common content management system and web server configuration files)
    46.HTTP CSRF (This script detects Cross Site Request Forgeries (CSRF) vulnerabilities)
    47.HTTP Default Accounts (Tests for access with default credentials used by a variety of web applications and devices)
    48.HTTP Development Framework (Tries to find out the technology behind the target website)
    49.HTTP Dlink Backdoor (Detects a firmware backdoor on some D-Link routers by changing the User-Agent to a "secret" value)
    50.HTTP Dom Based XSS (It looks for places where attacker-controlled information in the DOM may be used to affect JavaScript execution in certain ways)
    51.HTTP Email Harvest (Spiders a web site and collects e-mail addresses)
    52.HTTP Enumeration (Enumerates directories used by popular web applications and servers)
    53.HTTP Errors (This script crawls through the website and returns any error pages)
    54.HTTP Exif Spider (Spiders a site's images looking for interesting exif data embedded in .jpg files)
    55.HTTP Fav Icon (Gets the favicon ("favorites icon") from a web page and matches it against a database of the icons of known web applications)
    56.HTTP File Upload Exploiter (Exploits insecure file upload forms in web applications using various techniques)
    57.HTTP Form Brute (Performs brute force password auditing against http form-based authentication)
    58.HTTP Fuzz (Performs a simple form fuzzing against forms found on websites)
    59.HTTP Frontpage Login (Checks whether target machines are vulnerable to anonymous Frontpage login)
    60.HTTP Google Malware (Checks if hosts are on Google's blacklist of suspected malware and phishing servers)
    61.HTTP Head (Performs a HEAD request for the root folder ("/") of a web server and displays the HTTP headers returned)
    62.HTTP IIS Short Name Brute (Attempts to brute force the 8.3 filenames (commonly known as short names) of files and directories in the root folder of vulnerable IIS servers)
    63.HTTP IIS Webdav Vuln (Checks for a vulnerability in IIS 5.1/6.0 that allows arbitrary users to access secured WebDAV folders)
    64.HTTP Joomla Brute (Performs brute force password auditing against Joomla web CMS installations)
    65.HTTP Malware Host (Looks for signature of known server compromises)
    66.HTTP Methods (Finds out what options are supported by an HTTP server)
    67.HTTP Method Tamper (Attempts to bypass password protected resources (HTTP 401 status) by performing HTTP verb tampering)
    68.HTTP NTLM Information (This script enumerates information from remote HTTP services with NTLM authentication enabled)
    69.HTTP Open Redirect (Spiders a website and attempts to identify open redirects)
    70.HTTP Passwd (Checks if a web server is vulnerable to directory traversal by attempting to retrieve /etc/passwd or \boot.ini)
    71.HTTP PHPmyadmin (Exploits a directory traversal vulnerability in phpMyAdmin 2.6.4-pl1)
    72.HTTP PHPself XSS (Crawls a web server and attempts to find PHP files vulnerable to reflected cross site scripting via the variable $_SERVER["PHP_SELF"])
    73.HTTP PHP version (Attempts to retrieve the PHP version from a web server)
    74.HTTP Proxy Brute (Performs brute force password guessing against HTTP proxy servers)
    75.HTTP Referer Checker (Informs about cross-domain include of scripts)
    76.HTTP RFI Spider (Crawls webservers in search of RFI (remote file inclusion) vulnerabilities)
    77.HTTP Robots (Checks for disallowed entries in /robots.txt on a web server)
    78.HTTP Server Header (Uses the HTTP Server header for missing version info)
    79.HTTP Sitemap Generator (Spiders a web server and displays its directory structure along with number and types of files in each folder)
    80.HTTP Slowloris Check (Tests a web server for vulnerability to the Slowloris DoS attack without actually launching a DoS attack)
    81.HTTP SQL Injection (Spiders an HTTP server looking for URLs containing queries vulnerable to an SQL injection attack)
    82.HTTP Stored XSS (Checks for stored XSS)
    83.HTTP TPlink Dir Traversal (Exploits a directory traversal vulnerability existing in several TP-Link wireless routers)
    84.HTTP Trace (Sends an HTTP TRACE request and shows if the method TRACE is enabled)
    85.HTTP Userdir Enumeration (Attempts to enumerate valid usernames on web servers running with the mod_userdir module or similar enabled)
    86.HTTP Vhosts (Searches for web virtual hostnames by making a large number of HEAD requests against http servers using common hostnames)
    87.HTTP Vmware Path Vuln (Checks for a path-traversal vulnerability in VMWare ESX, ESXi, and Server (CVE-2009-3733))
    88.HTTP Vuln CVE-2009-3960 (Exploits cve-2009-3960 also known as Adobe XML External Entity Injection)
    89.HTTP Vuln CVE-2011-3192 (Detects a denial of service vulnerability in the way the Apache web server handles requests)
    90.HTTP Vuln CVE-2011-3368 (Tests for the CVE-2011-3368 (Reverse Proxy Bypass) vulnerability in Apache HTTP server's reverse proxy mode)
    91.HTTP Vuln CVE-2012-1823 (Detects PHP-CGI installations that are vulnerable to CVE-2012-1823)
    92.HTTP Vuln CVE-2013-0156 (Detects Ruby on Rails servers vulnerable to object injection, remote command executions and denial of service attacks)
    93.HTTP WAF Detect (Attempts to determine whether a web server is protected by an IPS, IDS or WAF )
    94.HTTP WAF Fingerprint (Tries to detect the presence of a web application firewall and its type and version)
    95.HTTP Wordpress Brute (Performs brute force password auditing against Wordpress CMS/blog installations)
    96.HTTP Wordpress Enumeration (Enumerates usernames in Wordpress blog/CMS installations by exploiting an information disclosure vulnerability)
    97.HTTP Wordpress Plugins (Tries to obtain a list of installed WordPress plugins by brute force testing for known plugins)
    98.HTTP Xssed (This script searches the xssed.com database and outputs the result)
    99.IKE Version (Obtains information (such as vendor and device type where available) from an IKE service by sending four packets to the host)
   100.IMAP Brute (Performs brute force password auditing against IMAP servers using either LOGIN, PLAIN, CRAM-MD5, DIGEST-MD5 or NTLM authentication)
   101.IMAP Capabilities (Retrieves IMAP email server capabilities)
   102.Ip Forwarding (Detects whether the remote device has ip forwarding or "Internet connection sharing" enabled)
   103.ISCSI Information (Collects and displays information from remote iSCSI targets)
   104.LDAP Brute (Attempts to brute-force LDAP authentication)
   105.MSRPC Enumeration (Queries an MSRPC endpoint mapper for a list of mapped services and displays the gathered information)
   106.MS SQL Empty Password (Attempts to authenticate to Microsoft SQL Servers using an empty password for the sysadmin (sa) account)
   107.MS SQL Information (Attempts to determine configuration and version information for Microsoft SQL Server instances)
   108.MySQL Empty Password (Checks for MySQL servers with an empty password)
   109.MySQL Enumeration (Performs valid-user enumeration against MySQL server using a bug discovered and published by Kingcope)
   110.MySQL Information (Connects to a MySQL server and prints information such as the protocol and version numbers, thread ID, status, capabilities, and the password salt)
   111.MySQL Vuln CVE-2012-2122 (Attempts to bypass authentication in MySQL and MariaDB servers by exploiting CVE2012-2122)
   112.NBStat (Attempts to retrieve the target's NetBIOS names and MAC address)
   113.NFS Ls (Attempts to get useful information about files from NFS exports)
   114.Oracle Brute (Performs brute force password auditing against Oracle servers)
   115.POP3 Brute (Tries to log into a POP3 account by guessing usernames and passwords)
   116.PPTP Version (Attempts to extract system information from the point-to-point tunneling protocol (PPTP) service)
   117.RDP Enumerate Encryption (Determines which Security layer and Encryption level is supported by the RDP service)
   118.RDP Vuln MS12-020 (Checks if a machine is vulnerable to MS12-020 RDP vulnerability)
   119.RealVNC Auth Bypass (Checks if a VNC server is vulnerable to the RealVNC authentication bypass (CVE-2006-2369))
   120.RPC Grind (Fingerprints the target RPC port to extract the target service, RPC number and version)
   121.RPC Information (Connects to portmapper and fetches a list of all registered programs)
   122.Samba Vuln CVE-2012-1182 (Checks if target machines are vulnerable to the Samba heap overflow vulnerability CVE-2012-1182)
   123.SIP Brute (Performs brute force password auditing against Session Initiation Protocol accounts)
   124.SMB Brute (Attempts to guess username/password combinations over SMB)
   125.SMB Check Vulns (Checks for vulnerabilities)
   126.SMB Enumerate Users (Attempts to enumerate the users on a remote Windows system)
   127.SMTP Brute (Performs brute force password auditing against SMTP servers)
   128.SMTP Vuln CVE-2010-4344 (Checks for and/or exploits a heap overflow within versions of Exim prior to version 4.69 (CVE-2010-4344))
   129.SMTP Vuln CVE-1011-1720 (Checks for a memory corruption in the Postfix SMTP server)
   130.SMTP Vuln CVE-2011-1764 (Checks for a format string vulnerability in the Exim SMTP server (version 4.70 through 4.75))
   131.SNMP Brute (Attempts to find an SNMP community string by brute force guessing)
   132.SNMP IOS Config (Attempts to downloads Cisco router IOS configuration files using SNMP)
   133.SSL Enumerate Ciphers (This script repeatedly initiates SSL/TLS connections and finds out what ciphers are being used)
   134.SSL Heartbleed (Detects whether a server is vulnerable to the OpenSSL Heartbleed bug (CVE-2014-0160))
   135.SSL Known Key (Checks whether the SSL certificate used by a host has a fingerprint that matches an included database of problematic keys)
   136.Telnet Brute (Performs brute-force password auditing against telnet servers)
   137.TFTP Enumeration (Enumerates TFTP filenames by testing for a list of common ones)
   138.UPNP Information (Attempts to extract system information from the UPnP service)
   140.VNC Brute (Performs brute force password auditing against VNC servers)
   141.VNC Information (Queries a VNC server for its protocol version and supported security types)
   142.X11 Access (Checks if you're allowed to connect to the X server)
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
    if ans=="15":
     xmloutput = raw_input("Save scan in XML format? [yes|no]:")
     if xmloutput == "yes":
      p15 = subprocess.Popen(['nmap', '--script=address-info.nse', 'v', '-oX', 'nmap_scan-%T-%D.xml', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Decoy Scan please be patient...") % remoteServer
      output15 = p15.communicate()[0]
      print output15 
     if xmloutput == "no":
      p15 = subprocess.Popen(['nmap', '--script=address-info.nse', '-v', remoteServer], stdout=sys.stdout, stderr=sys.stderr)
      print colorgrn.format("Scanning %s with Decoy Scan please be patient...") % remoteServer
      output15 = p15.communicate()[0]
      print output15 
    if ans=="99":
      print("\n Thanks for checking out my script!\n") 
      sys.exit()
 
