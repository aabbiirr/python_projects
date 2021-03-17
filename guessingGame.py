## Guessing Game

def main():
    #RANDOM NUMBER 
    from random import randint
    secret_number = randint(1, 101)
    guess_count = 0
    guesses = []
    
    print("WE HAVE TAKEN A NUMBER AT RANDOM. GUESS IT!")
    print("--------------------------------------------")
    while True:
        guess_count += 1
        user_input = int(input("Your guess: "))
        guesses.append(user_input)
    
        #WIN CASE
        if (user_input == secret_number):
            print("CORRECT!")
            print("Number of gueesses = {}".format(guess_count))
            break
    
        #COMPARING PREV WITH PRESENT
        if len(guesses)>=2:
            if abs(secret_number-guesses[-2]) > abs(secret_number-guesses[-1]):
                print("WARMER")
            elif abs(secret_number-guesses[-2]) < abs(secret_number-guesses[-1]):
                print('COLDER')
            
        #10 DISTANCE
        if abs(secret_number-guesses[-1])<=10:
            print("WARM")
        elif abs(secret_number-guesses[-1])>10:
            print("COLD")

if __name__=="__main__":main()
