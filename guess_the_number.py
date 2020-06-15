# Guess the number 

print("Guess the number if you can !!")
import random

r = random.randint(1, 9)
i = int(input("Enter the no. between 0 to 10 that I'm thinking right now\n"))
a, b = 10, 0
while True:
    if i < r:
        b = i
        i = int(input("Enter a no. greater than %d but less than %d\n" % (i, a)))
    elif i > r:
        a = i
        i = int(input("Enter a no. greater than %d but less than %d\n" % (b, i)))
    else:
        print("Hurray! you guessed the no. which was %d\n" % r)
        break
    