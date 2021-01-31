# Attack on ASLR (Address Space Layout Randomization) mechanism 

The attack overcomes ASLR mechanism and changes the name (headline) of the running (vulnerable) server.

* msg.bin contains the code that crashes the server.

* prog1.asm & prog2.asm change the name of the server.

* aslr_attack.py manages the whole operation.

**Run**:

>1. Run the vulnerable server via Immunity Debugger.
>
>2. When server waits for connections, run the aslr_attack.py.
