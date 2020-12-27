import time
import random
def hi(name):
    print("Welcome "+ name +" we're gonna play hangman game with you!")

def divide(word):
    w=list(word)
    l=len(w)
    print("Your word has: "+str(l)+" letters")
   

 
n=input("Please enter your name: \n")
hi(n)
WORDS = ("turkishaihub", "turkish", "gloabalaihub", "global", "artifical",  "intelligence")
wordd=random.choice(WORDS)
divide(wordd)

time.sleep(1)
print("I'm guessing...")
time.sleep(1)


letter_guess=""
energy=12

while energy>0:
    failed=0

    for character in wordd: 

        if character in letter_guess:
            print(character,end='')
        else:
            print(" _ ",end='')

            failed=failed+1
    if failed==0:
        print("\n You won dude!")
        break
        
    user=input("\n\nPlease only enter a letter(not number):  ")
    userr=user.lower()
    letter_guess +=userr
    
    if user not in wordd:
        energy= energy-1
        print("Wrong")
        print("You have "+str(energy)+" energy")        
        
        for i in range(energy):
            print("❤️  ",end='')
        print("\n")
        if energy==0:
            print("Game over dude")
