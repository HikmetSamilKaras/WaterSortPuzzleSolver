To use this algorithm use the watersolver() method in watersolve.py 

You will have to format your water bottles as follows:
You will have to have a list of water bottles as your input to watersolver()
Every water bottle is a list with information on its spaces (top of the water bottle will correspond to list index 0)

For example:
![WhatsApp Görsel 2025-01-15 saat 20 05 05_60e14886](https://github.com/user-attachments/assets/b0e41126-1a34-4352-9a3d-2457fccab498)

must be formmatted as follows:

[[1,1,2,2],[1,1,3,2],[3,3,3,2],[0,0,0,0],[0,0,0,0]] (Notice that same colors get the same integer value and empty spaces are donated with 0's)

Your output will be a list of operations.
Each operation's first index will denote which bootle to pour and the second index will denote which bottle to pour into.

For the same example we will get:
[[0, 3], [1, 3], [1, 4], [0, 1], [2, 0], [0, 4], [1, 2]] as the solution list
