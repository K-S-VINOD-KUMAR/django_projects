import random
print("Welcome to Random Number Guessing Challenge")
print("==========================================")
print("Must and should choose number between 1 to 7")
def game():
    chance = 1
    times = 2
    while(chance<=3):
        try:
            guess_number = int(input("Enter Your guess for "+str(chance)+" Chance\n"))
        except:
            print("Enter correct number")
            guess_number = int(input("Enter Your guess for "+str(chance)+" Chance\n"))
        random_number = random.randint(1,2)
        print("Expected number is "+str(random_number))
        if(guess_number==random_number):
            print("Your Guess is Correct!  You won in "+str(chance)+" chance")
            again = input("If you want to play again? Press Y/N")
            if(again.lower() == 'y'):
                print("Play again")
                game()
            elif(again.lower()=='n'):
                print("Congratulations and Come Back again........!")
                break
            else:
                print("Any way You entered wrong option \nCongratulations and Come Back again........! ")
                break
        else:
            if(chance!=3):
                print("your guess is wrong try again you left only "+str(times)+" Chances more")
                times=times-1
            if(chance==3):
                print("your guess is wrong No more chances")
                print("You lost this Challenge !")
                print("********************")
                again = input("If you want to play again? Press Y/N")
                if(again.lower() == 'y'):
                    print("Play again")
                    game()
                elif(again.lower()=='n'):
                    print("Well tried Come Back again........!")
                    break
                else:
                    print("Any way You entered wrong option \nWell tried Come Back again........! ")
                    break
            chance=chance+1
    
game()
