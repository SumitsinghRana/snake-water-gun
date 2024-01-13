import random
list=["snake","water","gun"]
computer_Choice=random.choice(list)
print("Game Rules->\nPress 's' for snake\nPress 'w' for water\nPress 'g'for gun")
rounds=int(input("how many rounds you want to play?"))
win=0
loose=0
draw=0
i=0
while(i<rounds):
    computer_Choice=random.choice(list)
    user_Choice=input("What you want to choose(Snake,Water,Gun) ")
    if user_Choice=='s':
        if(user_Choice=='s' and computer_Choice=='gun'):
            print("You loose_computer choosed ",computer_Choice)
            loose=loose+1
        elif(user_Choice=='s' and computer_Choice=='snake'):
            print("i'ts an Draw computer also choose",computer_Choice) 
            draw=draw+1
        else:
            print("you won,computer choice was ",computer_Choice)
            win=win+1   
    elif user_Choice=='w':
        if(user_Choice=='w' and computer_Choice=='snake'):
            print("You loose_computer choosed ",computer_Choice)
            loose=loose+1
        elif(user_Choice=='w' and computer_Choice=='water'):
            print("i'ts an Draw computer also choose",computer_Choice) 
            draw=draw+1
        else:
            print("you won,computer choice was ",computer_Choice)
            win=win+1   
    elif user_Choice=='g':
         if(user_Choice=='g' and computer_Choice=='water'):
            print("You loose_computer choosed ",computer_Choice)
            loose=loose+1
         elif(user_Choice=='g' and computer_Choice=='gun'):
            print("i'ts an Draw computer also choose",computer_Choice) 
            draw=draw+1
         else:
            print("you won,computer choice was ",computer_Choice)
            win=win+1
    else:
        print("Play according to game rules!")
        i=i+1
    i=i+1  
print("You win ",win," rounds")
print("You loose ",loose," rounds")
print("Draw in ",draw," rounds")
if(win>loose):
    print("According to the stats you win against the Computer")
elif(loose>win):
    print("According to the stats you loose against Computer")
else:
    print("According to the stats the whole game was a Draw")    
