[bits 32]

global _start

section .text

_start:
fldz
fnstenv [esp-12]
pop ecx
sub ecx, 0x67
jmp ecx