import random    # when we import a module, it allows us to access it from within the code library modele'random'


count = 0     #  Count is a variable, which tells us the position of the player, as we need to define from where are we start initially, here we are starting form 0


while(count<=100): # we want the dice to roll again and again, without writing the whole code again so we take the help of the loop called "while". and we define that the loop  is valid until the count reaches 100
    
    a= input("enter r to roll the dice")  # here we take a as a variable, which is the input given by us to roll the dice as we hit R on the keyboard.
    if(a=='r'): # here we compare our input "a" to the integer 'r', this r is written in quotes because we always compare two similar things. so r made to be an integer
        r=random.randint(1,6)# this is done to randomize the value "r"  form 1 to 6
        count= count+r # this statement gives you the current position of the player; eg- if r=0, count=2, then current position=0+2=2
        print("You rolled number = ", r)#This tells the number on the dice
        print("Your position is ", count,)# this statement will tell the players position
        if count== 8: #and then we enter into the if else ladder, where we define the conditoins
            count=37
            print("WOW! you just climed the ladder")
        elif (count==11):
            count=2
            print("Bad luck! snake has bitten you :(")
        elif(count== 13):
            count=34
            print("WOW! you just climed the ladder")
        elif (count==25):
            count=4
            print("Bad luck! snake has bitten you :(")
        elif (count==38):
            count=9
            print("Bad luck! snake has bitten you :(")
        elif(count== 40):
            count=68
            print("WOW! you just climed the ladder")
        elif (count== 52):
            count=81
            print("WOW! you just climed the ladder")
            
        elif (count==65):
            count=46
            print("Bad luck! snake has bitten you :(")
            
        elif(count== 76):
            count=97
            print("WOW! you just climed the ladder")
        elif (count==89):
            count=70
            print("Bad luck! snake has bitten you :(")
        elif (count==93):
            count=64
            print("Bad luck! snake has bitten you :(")
        elif (count==100):
            print("you won")
            break
        elif(count>100):
            count=count-r
print ("Try again!, you missed 100")
