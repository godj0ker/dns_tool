from colorama import *
def help():
    print(Fore.LIGHTRED_EX+"Usage: dnslookup -d <domain> -l <option>")
    print(Fore.LIGHTRED_EX+"Example: dnslookup -d example.com -l all")
    print(Fore.LIGHTRED_EX+"! Type dnslookup -c or --commands for available commands and options !"+ Fore.RESET)
    return
    
def commands():
    print(Fore.LIGHTGREEN_EX+"Available commands:\n\n")
    print(Fore.GREEN+"-h or --help: Show help information")
    print(Fore.GREEN+"-d or --domain: Specify the target domain")
    print(Fore.GREEN+"-l or --lookup: Specify the enumeration option (a,4a, mx, ns, txt, soa, cname,all)")
    print(Fore.GREEN+"-c or --commands: Show available commands and options")
    print(Fore.GREEN+"-q or --exit: Exit the program"+Fore.RESET)
    print("\n\n")
    
    print(Fore.LIGHTGREEN_EX+"Available enumeration options:")
    options=('''
    
    lookup options:      
    
    whois   : Whois record
    a       : IPV4 record
    4a    : IPV6 record
    cname   : CNAME record
    mx      : MX record
    ns      : NS record
    txt     : TXT record
    soa     : SOA record
    all     : All records''' )
    
    print(Fore.YELLOW+options+Fore.RESET)
    
    