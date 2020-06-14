# Guess the number 

print("Guess the number if you can !!")
import random

r = random.randint(1, 9)
i = int(input("Enter the no. between 0 to 10 that I'm thinking right now\n"))
a = 10
b = 0
if i < r:
    b = i
elif i > r:
    a = i
else:
    None
while True:
    if i < r:
        i = int(input("Enter a no. greater than %d but less than %d\n" % (i, a)))
        if i < r:
            b = i
    elif i > r:
        i = int(input("Enter a no. greater than %d but less than %d\n" % (b, i)))
        if i > r:
            a = i
    else:
        print("Hurray! you guessed the no. which was no. %d\n" % r)
        break
    