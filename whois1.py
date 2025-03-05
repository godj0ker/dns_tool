import whois

global target

def whois_scan():

    print("|--------------------Whois--------------------|")
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

   