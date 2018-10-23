import random

question = input('Would you like to roll the dice [y/n]?\n')

while question != 'n':
 if question == 'y':
   dice1 = random.randint(1, 6)
   dice2 = random.randint(1, 6)
   dice3 = random.randint(1, 6)
   print(dice1, dice2, dice3)
   print(dice1+dice2+dice3)
   question = input('Would you like to roll the dice [y/n]?\n')
else:
 print('Invalid response. Please type "y" or "n".')
question = input('Would you like to roll the dice [y/n]?\n')

print('Good-bye!')