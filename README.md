


Nmap Command Line Interface
=======
nmapcli is a tool written in Python with pre-defined scan templates to automate Nmap scans.

Usage: ./nmapcli.py


      XX*************************XX
      XX*************************XX
    **       Nmap Quick CLI        **
    **     Created By: Sheimo      **
    **                             **
    **         Version:2.1         **
      XX*************************XX
      XX*************************XX

Enter remote host(s) to scan in Nmap format: 192.168.1.143

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

[+] Script Category Scans
    15.Auth (These scripts deal with authentication credentials (or bypassing them) on the target system)
    16.Broadcast (Scripts in this category typically do discovery of hosts not listed on the command line by broadcasting on the local network)
    17.Brute (These scripts use brute force attacks to guess authentication credentials of a remote server)
    18.Default (These scripts are the default set and are run when using the -sC or -A options rather than listing scripts with --script)
    19.Discovery (These scripts try to actively discover more about the network by querying public registries, SNMP-enabled devices, directory services, and the like)
    20.Dos (Scripts in this category may cause a denial of service)
    21.Exploit (These scripts aim to actively exploit some vulnerability)
    22.External (Scripts in this category may send data to a third-party database or other network resource)
    23.Fuzzer (This category contains scripts which are designed to send server software unexpected or randomized fields in each packet)
    24.Intrusive (These are scripts that cannot be classified in the safe category because the risks are too high that they will crash the target system)
    25.Malware (These scripts test whether the target platform is infected by malware or backdoors)
    26.Safe (Scripts which weren't designed to crash services, use large amounts of network bandwidth or other resources, or exploit security holes are categorized as safe)
    27.Version (The scripts in this special category are an extension to the version detection feature and cannot be selected explicitly)
    28.Vuln (These scripts check for specific known vulnerabilities and generally only report results if they are found)

    99. Exit/Quit
    
What would you like to do? 
