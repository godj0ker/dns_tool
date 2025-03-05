import dns.resolver


global target

def a_record():
    print("|--------------------A RECORD--------------------|")
    try:
        info=dns.resolver.resolve(target,'A')
    
        for ip in info:
            print(ip)
    except dns.resolver.NoAnswer:
        print("Query does not exist :")
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist")
    except Exception as e:
        print(f"error occured :{e}")
        

def ipv6():
    
    print("|--------------------AAAA RECORD--------------------|")
    try:
        info=dns.resolver.resolve(target,'AAAA')
    
        for ip in info:
            print(ip)
            
    except dns.resolver.NoAnswer:
        print("Query does not exist :")
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist")
    except Exception as e:
        print(f"error occured :{e}")
        
def cname():
    print("|--------------------CNAME RECORD--------------------|")
    try:
        cname_info=dns.resolver.resolve(target,'CNAME')
    
        for cn in cname_info:
            print(cn) 
            
    except dns.resolver.NoAnswer:
        print("Query does not exist :")
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist")
    except Exception as e:
        print(f"error occured :{e}")
        

def mx():
    
    print("|--------------------MX RECORD--------------------|")
    try:
        mail_info=dns.resolver.resolve(target,'MX')
    
        for mailinfo in mail_info:
            print(mailinfo)
        
    except dns.resolver.NoAnswer:
        print("Query does not exist :")
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist")
    except Exception as e:
        print(f"error occured :{e}")
         
def ns():
    
    print("|--------------------NS RECORD--------------------|")
    
    try:
        ns_info=dns.resolver.resolve(target,'NS')
    
        for nameserver in ns_info:
            print(nameserver)
            
    except dns.resolver.NoAnswer:
        print("Query does not exist :")
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist")
    except Exception as e:
        print(f"error occured :{e}")
        
def txt():
    
    
    print("|--------------------TXT RECORD--------------------|")
    try:
        
        txt_rec=dns.resolver.resolve(target,'TXT')
    
        for rec in txt_rec:
            print(rec)
        
    except dns.resolver.NoAnswer:
        print("Query does not exist :")
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist")
    except Exception as e:
        print(f"error occured :{e}")
        

               
    