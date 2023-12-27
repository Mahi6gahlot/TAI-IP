import random
def guess_number():
    secret_number=random.randint(1,10)
    tries=0

    while True:
        guess=int(input("Guess a number between 1 and 10 :"))
        tries+=1
        if guess <secret_number:
            print("Too Low")
        elif guess>secret_number:
            print("Too High")
        else:
            print("Congratulations! You guessed the number in {tries}tries!")
            break
guess_number()        
