import dns.resolver
from colorama import *



def a_record():
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
        

def ipv6():
    
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
        
def cname():
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
        

def mx():
    
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
         
def ns():
    
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
        
def txt():
    
    
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
        

               
    