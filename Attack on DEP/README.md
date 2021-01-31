# Attack on DEP (Data Execution Prevention)

Vulnerable program opens input.txt.

The attack writes into input.txt context that causes the program to:

>- Deactivate DEP of stack.
>
>- Change the SEH chain structure.
>
>- Cause an exception.
>
>- Run the attack code through SEH and stack.
>
>- Activate the Windows Calculator.


**Run:**

>1. Run python script (input.txt needed).
>
>2. Open the Demo1.exe in Immunity Debugger.
>
>3. Run the program in Immunity Debugger (F9).
>
>4. To skip the exception, press shift+F9 (if occured).
