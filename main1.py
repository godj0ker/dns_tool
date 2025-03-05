import toolfun
import whois1
from pyfiglet import*


f=Figlet()

print(f.renderText("Dnstool"))
print("!!This tools is made only for testing and educational purpose !! \n \n")
print("\t \t \t \tby godjoker\n \n")


toolfun.target=input("Enter target Domain :")
whois1.target=toolfun.target

def main_window():
    
    while True:
        print('''
              [1].Whois
              [2].ipv4
              [3].1pv6
              [4].cname
              [5].mx lookup
              [6].ns lookup
              [7].txt record
              [8].All''')
              
        opt=int(input("ENTER OPTION :"))
        
        if opt==1:
            whois1.whois_scan()
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
            whois1.whois_scan()
            toolfun.a_record()
            toolfun.ipv6()
            toolfun.cname()
            toolfun.mx()
            toolfun.ns()
            toolfun.txt()
          
            
        else:
            print("invalid option")


    
    
main_window()    