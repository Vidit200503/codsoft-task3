#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

print("\n====Stone Paper  AND Scissor Game!!!====\n")

compScore = 0
userscore = 0
name = input("Name:- ")
Rounds = int(input("\nEnter No. of Rounds:- "))
plot = 1

lt = []
print("\nEnter S For Stone\nEnter P For Paper\nEnter X For Scissor\n")
while plot <= Rounds:
    compValue = random.choice(['S','P','X'])
    userinput = input("Enter Your Choice:- ").upper()

    if compValue == userinput:
        lt.append(f"Round {plot} - TIES")
        print(f"\nYou :- {userinput}\nComputer :- {compValue}\nRound {plot} - TIES.\n")

    elif compValue == 'P' and userinput == 'S':
        lt.append(f"Round {plot} - COMPUTER WINS!!")
        compScore += 1
        print(
            f"\nYou :- {userinput}\nComputer :- {compValue}\nRound {plot} - COMPUTER WINS!!\n")

    elif compValue == 'S' and userinput == 'P':
        lt.append(f"Round {plot} - {name} WINS")
        userscore += 1
        print(f"\nYou :- {userinput}\nComputer :- {compValue}\nRound {plot} - {name} WINS!!\n")
        
    elif compValue == 'X' and userinput == 'S':
        lt.append(f"Round {plot} - {name} WINS!!")
        userscore += 1
        print(f"\nYou :- {userinput}\nComputer Played:- {compValue}\nRound {plot} - {name} WINS!!\n")
    
    elif compValue == 'S' and userinput == 'X':
        lt.append(f"Round {plot} - COMPUTER WINS!!")
        compScore += 1
        print(f"\nYou :- {userinput}\nComputer Played:- {compValue}\nRound {plot} - COMPUTER WINS!!\n")


    elif compValue == 'X' and userinput == 'P':
        lt.append(f"Round {plot} - COMPUTER WINS!!")
        compScore += 1
        print(f"\nYou :- {userinput}\nComputer Played:- {compValue}\nRound {plot} - COMPUTER WINS!!\n")

    elif compValue == 'P' and userinput == 'X':
        lt.append(f"Round {plot} - {name} WINS!!")
        userscore += 1
        print(f"\nYou :- {userinput}\nComputer Played:- {compValue}\nRound {plot} - {name} WINS!!\n")
    
    else:

        print("ERROR")

    plot += 1

print("\nComputer Score:- ", compScore)
print(f"\n{name}'s Score:- {userscore}")
print("\nNumber of Rounds:- ", Rounds)
[print(i) for i in lt]


if userscore == compScore:
    print("\nGame TIED.")

elif userscore > compScore:
    print(f"\n{name} WINS The Game!!!")

else:
    print("\nCOMPUTER WINS The Game!!! Try hard!!")


# In[ ]:




