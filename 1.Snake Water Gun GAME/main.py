import random
'''
1 For snake
0 for gun
-1 for water
'''

computer =random.choice([-1,1,0])
youstr = input("Enter your choice: ")
youdict = {"s":1,"w":-1,"g":0}
you = youdict[youstr]

reversedict = {1:"Snake",0:"Gun",-1:"Water"}
print(f"You choose {reversedict[you]}")
print(f"Computer choose {reversedict[computer]}")

if(computer== -1 and you == 1):
    print("You Win!")
elif(computer == -1 and you == 0):
    print("You Lose! ")
elif(computer == -1 and you == -1):
    print("It's Draw!")
elif(computer == 1 and you == 1):
    print("It's Draw! ")
elif(computer == 1 and you == 0):
    print(" You Win!")
elif(computer == 1 and you == -1):
    print(" You Lose!")
elif(computer == 0 and you == 1):
    print(" You Lose!")
elif(computer == 0 and you == 0):
    print("It's Draw! ")
elif(computer == 0 and you == -1):
    print("You Win! ")
else:
    print("Something went wrong!\nTry again,GOOD LUCK!")
