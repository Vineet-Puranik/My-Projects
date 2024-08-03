#Create  a function named 'is_prime' that takes an argument called 'num'
def is_prime(num):
#Check to see if num is less than 2
  if num < 2:
#If so, return false
      return False
#Create a variable named 'counter' and set it equal to 1 less than the value of num
  counter = num-1
#Create a while loops that runs when counter is greater than 1
  while(counter > 1):
#Create an if loops that checks if the remainder of num divided by counter is equal to 0
    if num % counter == 0:
#If it is, return false
      return False
#Set counter equal to counter minus one
    counter -= 1
#Then return true
  return True
#Create a function named "count_primes" that takes an argument called "list_with_primes"
def count_primes(list_with_primes):
#Create a variable called 'primes' and set it equal to 0 
    primes = 0
#Create a for loop that will sort through each element in list_with_primes
    for x in list_with_primes:
#Create an if loop that calls the function "is_prime" and tests the value of x
        if(is_prime(x)):
#Increase primes by 1
            primes += 1
#Return the value of primes
    return primes
#Create a function called "bubble_sort" that takes an argument called sorting_list
def bubble_sort(sorting_list):
#Create a variable called n that is equal to the length of sorting_list
  n = len(sorting_list)
#Create a for loop that sorts through the range of n minus 1
  for i in range(n-1):
#Create a for loop that sorts through the range of 0 to n - i - 1
    for j in range(0, n-i-1):
#Create an if loop that tests if the current element is greater than the next element.
      if sorting_list[j] > sorting_list[j + 1] :
#If it is, swap their positions in sorting_list
        sorting_list[j], sorting_list[j + 1] = sorting_list[j + 1], sorting_list[j]

#Create a function called get_average with an argument called list_to_average
def get_average(list_to_average):
#Create a variable called total and set it equal to 0 
  total = 0
#Create a for loop that sorts through every element in list_to_average
  for i in list_to_average:
#Set total equal to itself plus i
    total = total + i
#Return the rounded value of total divided by the length of list_to_average
  return round(total/len(list_to_average))

#Create a main function
def main():
#Create an empty list called user_list
  user_list = []
#Ask the user to enter a number and type done when they are finished
  user_num = input('Enter a number (type "Done" when finsished): ')
#Create a while loop to test when the user types done
  while(user_num.lower() != 'done'):
#Test what the error is
    try:
#Set user_num to the integer value of user_num
      user_num = int(user_num)
#Add user_num to user_list
      user_list.append(user_num)
#Test for a Value Error
    except ValueError as err:
#Print the error and tell the user that it was not a number
      print(err,'That was not a number!')
#Ask for another number and tell the user to type done when they are finished
    user_num = input('Enter another number (type "Done" when finsished): ')
#Print the user_list
  print('Your list:',user_list)
#Pass user_list through the function count_primes and print the result
  print('Your list has',count_primes(user_list),'primes')
#Pass user_list through the function count_primes and print the result
  print('Average:',get_average(user_list))
#pass user_list through bubble_sprt
  bubble_sort(user_list)
#Print the user_list
  print('Your list sorted:',user_list)

#check if this is the main module
if __name__=="__main__":
  #run the main function (which should always run first)
  main()
