# snake water gun game
'''
1 for snake
-1 for water
0 for gun
'''
while(True):
    try:
        import random
        computer = random.choice([-1,0,1])
        youstr = input("Enter your choice [s,w,g] : ")
        youdict = {"s":1,"w":-1,"g":0}
        reverseDict = {1:"Snake",-1:"Water",0:"Gun"}
        you = youdict[youstr]

        print(f"You choose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

        if(computer == you):
            print("Its a draw...\n")
        else:
            if(computer == -1 and you == 1):
                print("You win...")
            elif(computer == -1 and you == 0):
                print("You lose...!")
            elif(computer == 1 and you == 0):
                print("You win...")
            elif(computer == 1 and you == -1):
                print("You lose...!")
            elif(computer == 0 and you == -1):
                print("You win...")
            elif(computer == 0 and you == 1):
                print("You lose...!")
            print("\n")
    except:
        print("Error...! Please choose frome only [s,w,g]\n")