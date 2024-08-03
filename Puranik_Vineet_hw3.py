##Print each letter of the animal on a new line
animal = input('What is your favorite animal: ')
for letter in animal:
  print(letter)
##Print each number until the user's number
number = int(input('Pick a number: '))
i = 0
while(i <= number):
  print(i, end = ' ')
  i+=1
print('\n')
##Print the user's choice only if they select an option
option = input ('Pick an option of soup, salad, or sandwich: ').lower()
while (option != 'soup' and option != 'salad' and option != 'sandwich'):
  print('Sorry that is not an option!')
  option = input ('Pick an option of soup, salad, or sandwich: ').lower()
print('Ok, you picked', option, '!')