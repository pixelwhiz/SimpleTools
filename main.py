import random
import os
import time
import os
import requests
import pprint
import socket
from email.message import EmailMessage
import smtplib

import pyfiglet as pf

#def RegisterData():
    #os.system('cmd /c "pip install pyfiglet"')
    
def IPLocation():
    ip = input("Masukan Alamat IP : ")
    dns = socket.gethostbyname(ip) #domain to ip
    api = requests.get(f"https://ipapi.co/"+format(dns)+"/json/")  #Memanggil fungsi dari URL Server
    pprint.pprint(api.json()) #Menampilkan hasil
        
    # Penutupan
    enter = input("\nPress ENTER to continue ...") #Penutup
    if enter:
        os.system('cls')
        MenuUI()
    else:
        os.system('cls')
        MenuUI()

def SendMail():
    sender_email = input("Masukan Email Kamu : ")
    rec_email = input("Masukan Email Tujuan : ")
    password = input(str("Masukan Password Email Kamu : "))
    message = input("Isi Pesan : ")
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, password)
    print('Login succes')
    server.sendmail(sender_email, rec_email, message)
    print("Email has been sent to ", rec_email)
    
def generatePassword(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("Password will be generated In "+ timer, end="\r")
        time.sleep(1)
        t -= 1
    os.system('cls')

def PasswordUI():
    lower = 0
    upper = 0
    number = 0
    count = 0
    password = []

    length = input("Enter Password Length: ")
    length = int(length)
    
    if type(length) == int:
        while count < length:
            rand = random.randint (0,2)
            if rand == 0:
                lower += 1
                b = int(random.randint (97,123))
                password.append(b)
            elif rand == 1:
                upper += 1
                b = random.randint (65,91)
                password.append(b)
            elif rand == 2:
                number += 1
                b = random.randint (48,58)
                password.append(b)
            count += 1
        password = "".join([chr(c) for c in password])
        # function call
        generatePassword(int(5))
        print("Password: " + password + "\n")
        enter = input("Press ENTER to continue ...")
        if enter:
            os.system('cls')
            MenuUI()
        else:
            os.system('cls')
            MenuUI()
    
    elif length:
        print("must be a number")
        
def MenuUI():
    print(pf.figlet_format("Simple Tools", font="bulbhead"))
    print("    Github : github.com/MuhammadDaffaTFA\n    Instagram : @mdafftfa\n\nChoose, what do you want to do in below: \n1) Random Password Generator \n2) IP Location\n3) Email System (Beta Release)\n")
    option = int(input("Select Options: "))
    
    if type(option) == int:
        if option == 1:
            PasswordUI()
        elif option == 2:
            IPLocation()
        elif option == 3:
            SendMail()
        elif option == 0:
            Update()
        else:
            return MenuUI()
    else:
        return MenuUI()
    
    
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("You will back to Menu in "+ timer, end="\r")
        time.sleep(1)
        t -= 1
    
    os.system('cls')
    MenuUI()
    
MenuUI()