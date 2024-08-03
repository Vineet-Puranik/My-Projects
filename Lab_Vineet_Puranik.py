import random
x = random.randint(1,6)
y = random.randint(1,6)
print('1st Dice Rolled ', x )
print('2nd Dice Rolled ', y)
if(x + y >6):
    print('You Won!')
else:
    print('You Lost!')