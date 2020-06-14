# Guess the number 

print ('Guess the number if you can !!')
import random
r = random.randint(1, 9)
i = eval(input('Enter any number in the range 1 to 9\n'))
if i < r:
    print ('Greater than this number.')
elif i > r:
    print (' Less than this nymber.')
else :
    print ('Congratulations!! you win.')
    