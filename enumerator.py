import dns.resolver
import whoiscan
from colorama import *



def a_record(target):
    print(Fore.GREEN+"|--------------------A RECORD--------------------|")
    try:
        info=dns.resolver.resolve(target,'A')
    
        for ip in info:
            print(ip)
    except dns.resolver.NoAnswer:
        print(Fore.RED+"Query does not exist :")
    except dns.resolver.NXDOMAIN:
        print(Fore.RED+"Domain does not exist")
    except Exception as e:
        print(Fore.RED+f"error occured :{e}"+Fore.RESET)
        

def ipv6(target):
    
    print(Fore.GREEN+"|--------------------AAAA RECORD--------------------|")
    try:
        info=dns.resolver.resolve(target,'AAAA')
    
        for ip in info:
            print(ip)
            
    except dns.resolver.NoAnswer:
        print(Fore.RED+"Query does not exist :")
    except dns.resolver.NXDOMAIN:
        print(Fore.RED+"Domain does not exist")
    except Exception as e:
        print(Fore.RED+f"error occured :{e}"+Fore.RESET)
        
def cname(target):
        
    print(Fore.GREEN+"|--------------------CNAME RECORD--------------------|")
    try:
        cname_info=dns.resolver.resolve(target,'CNAME')
    
        for cn in cname_info:
            print(cn)
            
    except dns.resolver.NoAnswer:
        print(Fore.RED+"Query does not exist :")
    except dns.resolver.NXDOMAIN:
        print(Fore.RED+"Domain does not exist")
    except Exception as e:
        print(Fore.RED+f"error occured :{e}"+Fore.RESET)
        

def mx(target):
    
    print(Fore.GREEN+"|--------------------MX RECORD--------------------|")
    try:
        mail_info=dns.resolver.resolve(target,'MX')
    
        for mailinfo in mail_info:
            print(mailinfo)
        
    except dns.resolver.NoAnswer:
        print(Fore.RED+"Query does not exist :")
    except dns.resolver.NXDOMAIN:
        print(Fore.RED+"Domain does not exist")
    except Exception as e:
        print(Fore.RED+f"error occured :{e}"+Fore.RESET)
         
def ns(target):
    
    print(Fore.GREEN+"|--------------------NS RECORD--------------------|")
    
    try:
        ns_info=dns.resolver.resolve(target,'NS')
    
        for nameserver in ns_info:
            print(nameserver)
            
    except dns.resolver.NoAnswer:
        print(Fore.RED+"Query does not exist :")
    except dns.resolver.NXDOMAIN:
        print(Fore.RED+"Domain does not exist")
    except Exception as e:
        print(Fore.RED+f"error occured :{e}"+Fore.RESET)
        
def txt(target):
    
    
    print(Fore.GREEN+"|--------------------TXT RECORD--------------------|")
    try:
        
        txt_rec=dns.resolver.resolve(target,'TXT')
    
        for rec in txt_rec:
            print(rec)
            
    except dns.resolver.NoAnswer:
        print(Fore.RED+"Query does not exist :")
    except dns.resolver.NXDOMAIN:
        print(Fore.RED+"Domain does not exist")
    except Exception as e:
        print(Fore.RED+f"error occured :{e}"+Fore.RESET)
        

               
def soa(target):
    
    
    print(Fore.GREEN+"|--------------------SOA RECORD--------------------|")
    try:
        soa_rec=dns.resolver.resolve(target,'SOA')
        for rec in soa_rec:
            print(rec)
    except dns.resolver.NoAnswer:
        print(Fore.RED+"Query does not exist :")
    except dns.resolver.NXDOMAIN:
        print(Fore.RED+"Domain does not exist")
    except Exception as e:
        print(Fore.RED+f"error occured :{e}"+Fore.RESET)
        
def all_records(target):
    print(Fore.GREEN+"|--------------------ALL SCAN--------------------|")
    try:
        whoiscan.whois_scan(target)
        a_record(target)
        ipv6(target)
        cname(target)
        mx(target)
        ns(target)
        txt(target)
        soa(target)
    except Exception as e:
        print(Fore.RED+f"Error occurred while retrieving all records: {e}"+Fore.RESET)