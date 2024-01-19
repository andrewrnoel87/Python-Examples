import random

start_range = None
end_range = None

while True:  
    try:
        start_range = int(input("Enter the start of the range: "))
        if (start_range < 0):
            raise ValueError("This is not a vaild number.")
    except:
        print("Please enter a valid number.")
    if str(start_range).isdigit():
        break

while True:
    try:
        end_range = int(input("Enter the end of the range: "))
        if (end_range < start_range):
            raise ValueError("This is not a vaild number.")
    except:
        print("Please enter a valid number.")
    
    if str(end_range).isdigit() and (start_range <= end_range):
        break

guess_target = random.randint(start_range, end_range)

guess_current = None
guess_count = 0

while True:
    try:
        guess_current = int(input("Guess a number: "))
        guess_count += 1
       
    except:
        print("Please enter a valid number.")

    if guess_current == guess_target:
        break

if guess_count == 1:
    print("You guessed the number in 1 attempt")
        
else:
    print(f"You guessed the number in {guess_count} attempts")