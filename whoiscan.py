import whois
from colorama import *

#global target

def whois_scan(target):

    print(Fore.GREEN+"|--------------------Whois--------------------|")
    
    try:
        info=whois.whois(target)

        print("DOMAIN :",info.domain_name)
        print("REGISTRAT :",info.registrar)
        print("WHOIS INFO:",info.whois_server)
        print("REFERAL URL:",info.referral_url)
        print("CREATED:",info.creation_date)
        print("UPDATED:",info.updated_date)
        print("EXPIRE:",info.expiration_date)
        print("NAME SERVER:",info.name_servers)
        print("DOMAIN STATUS:",info.status)
        print("EMAIL:",info.emails)
        print("COUNTRY:",info.country)
        print("CITY:",info.city)
        print("ZIP:",info.zipcode)
        print("STATE:",info.state)
        print("PHONE:",info.phone)
        print("FAX:",info.fax)
        print("ADDRESS:",info.address)
        print("POSTAL CODE:",info.postalcode)
        print("REGISTRAR URL:",info.registrar_url)
        print("REGISTRAR WHOIS:",info.registrar_whois_server)
        print("REGISTRAR NAME:",info.registrar_name)
        print("REGISTRAR EMAIL:",info.registrar_email)
        print("REGISTRAR PHONE:",info.registrar_phone)
        print("REGISTRAR FAX:",info.registrar_fax)
        print("REGISTRAR ADDRESS:",info.registrar_address)
        print("REGISTRAR POSTAL CODE:",info.registrar_postalcode)
        print("REGISTRAR CITY:",info.registrar_city)
        print("REGISTRAR STATE:",info.registrar_state)
        print("REGISTRAR COUNTRY:",info.registrar_country)
        print("REGISTRAR ZIP:",info.registrar_zipcode)
        print("REGISTRAR PHONE:",info.registrar_phone)      
        print(Fore.RESET)
    except Exception as e:
        print(Fore.RED+f"Error: Unable to retrieve WHOIS information. {e}"+Fore.RESET)