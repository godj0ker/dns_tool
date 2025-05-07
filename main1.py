import toolfun
import whoiscan
import colorama
from colorama import Fore, Back, Style
from pyfiglet import*


f=Figlet()
global target

print(Fore.LIGHTBLUE_EX+f.renderText("Dnstool"))
print("!!This tools is made only for testing and educational purpose !! \n \n")
print("\t \t \t \tby godjoker\n \n"+Fore.RESET)


target=input(Fore.LIGHTCYAN_EX+"Enter target Domain :")
print(Fore.RESET)
toolfun.target=target
whoiscan.target=target

def main_window():
    
    while True:
        print(Fore.GREEN + '''
        |--------------------DNS TOOL--------------------|
              [1].Whois
              [2].ipv4
              [3].1pv6
              [4].cname
              [5].mx lookup
              [6].ns lookup
              [7].txt record
              [8].All
              [9].Exit
              ''')
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------"+Fore.RESET)
              
        opt=int(input("ENTER OPTION :"))
        
        if opt==1:
            whoiscan.whois_scan()
        elif opt==2:
            toolfun.a_record()
        elif opt==3:
            toolfun.ipv6()
        elif opt==4:
            toolfun.cname()
        elif opt==5:
            toolfun.mx()
        elif opt==6:
            toolfun.ns()
        elif opt==7:
            toolfun.txt()
        elif opt==8:
            whoiscan.whois_scan()
            toolfun.a_record()
            toolfun.ipv6()
            toolfun.cname()
            toolfun.mx()
            toolfun.ns()
            toolfun.txt()
          
        elif opt==9:
            print(Fore.RED+"Exiting the program...")
            break
        else:
            print(Fore.RED+"invalid option")
            print(Fore.RESET)
            

    
    
main_window()    