print ( '\t'  '\t'  "# ################### #\n")
print  ('\t'        "	#   Panel *_*     #\n")
print  ('\t' 	  "	# ################### #\n ")
print ("Welcome !")
print ("To use this script there are 3 options only\n")
print ("To countinue press enter\n")
input ("Enter to countinue =#")
print ("[+] 1 = send ping to web_site \n")
print ("[+] 2 = open apps you want\n")
print ("[+] 3 = check internat conection\n")
print  ("please insert options .. \n")
while True :
    a = input("Enter the num of option here : ")
    if a == "1":
        site = input("Enter web_site here : ")
        site = site.replace("https//", "") or ("https://", "")
        print (site)
        import os

        os.system("ping {}  ".format(site))
    elif a == "2":
        c = input("wite the app to open : ")
        import os

        os.system("start {} ".format(c))
    elif a == "3":
        import os

        os.system("ipconfig")
    else:
        print ("[!] unkonwn num")
input("enter to close")
