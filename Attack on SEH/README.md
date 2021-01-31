# Attack on SEH (Structured Exception Handling)

Vulnerable program opens input.txt.

The attack writes into input.txt context that causes the program to open calculator using SEH Chain. 

Prevents regular exception handling and instead opens calculator in windows.


Run:

1. Run python script (input.txt needed).

2. Open the Demo1.exe in Immunity Debugger.

3. Run the program in Immunity Debugger (F9).

4. To skip the exception, press shift+F9.