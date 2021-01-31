[bits 32]

global _start

section .text

_start:
xor		edx,edx
mov 	edx, 0x1f636553
BSWAP 	edx
inc 	edx
BSWAP 	edx
push 	edx
push	0x74666f53
mov		esi,esp
push	esi
xor		edx,edx
mov		esi,fs:[edx+0x30]
mov		esi,[esi+0xc]
mov		esi,[esi+0xc]
lodsd
mov	esi,[eax]
mov		edi,[esi+0x18]
mov		ebx,[edi+0x3c]
mov		ebx,[edi+ebx*1+0x78]
mov		esi,[edi+ebx*1+0x20]
add		esi,edi
mov		ecx,[edi+ebx*1+0x24]
add		ecx,edi
here:
inc		edx
lodsd
cmp		dword [edi+eax*1],0x43746553
jne		here
cmp		dword [edi+eax*1+0xc],0x41656c74
jne		here
movzx	edx,WORD [ecx+edx*2-0x2]
mov		esi,[edi+ebx*1+0x1c]
add		esi,edi
add		edi,[esi+edx*4]
call	edi