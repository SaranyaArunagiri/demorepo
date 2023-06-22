import random
print("Lets play! Choose an option: 1.Rock, 2.Paper, 3.Scissor")
Humaninput= int(input("Choose an option:"))
Macinput = random.randint(1,3)
print(Macinput)
if((Humaninput==1 and Macinput==3) or (Humaninput==2 and Macinput==1) or (Humaninput==3 and Macinput==2)):
    print("Macoutput: Err you won Human")
elif((Macinput==1 and Humaninput==3) or (Macinput==2 and Humaninput==1) or (Macinput==3 and Humaninput==2)):
    print("Macoutput: Haha you suck Human")
elif(Humaninput==Macinput):
    print("Its a tie.Play again.")
 