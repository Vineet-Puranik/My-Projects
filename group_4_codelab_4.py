def max_word_length(words_list):
  #TODO: use a loop to go through all of the words in words_list and determine the longest word length
  max_word = 0
  for word in words_list:
    if len(word) > max_word:
      max_word = len(word)
  
  return max_word 

def frame_this(list_of_words):
  frame_width = max_word_length(list_of_words)+2
  for i in range(frame_width+2):
    print('*',end='')
  print()

  
  for word in list_of_words:
    print('*',end='')
    for i in range(int((frame_width-len(word))/2)):
      print(' ',end='')
    print(word,end='')
    
    if(len(word)%2==0):
      x = int((frame_width-len(word))/2)
    else:
      x = int((frame_width-len(word))/2)+1
    
    for i in range(x):
      print(' ',end='')
    print('*',end='')
    print()
    
  for i in range(frame_width+2):
    print('*',end='')

  print()
  print()

      
  #TODO: make sure the frame edges are straight, and that there is at least one space between the word and the frame edge
  #TODO: you must handle any length of word, and any number of words in the list
  #TODO: important: do NOT use .center to center the text, use a loop or concatenate
  #TODO: hint: this function DOES NOT return anything
  #TODO: replace this print statement the desired print behavior

def is_prime(num):
  if (num==1 or num==0):
    print(num, 'is not prime.')
    return
    
  if num < 2: 
    return False
  for i in range (2, num):
    if num%i==0:
      return False
  return True  #TODO: replace this return line with the correct return value

def count_primes(list_of_numbers):
  count = 0
  for number in list_of_numbers:
    if is_prime(number) == True:
      count+=1
  #TODO: count the total number of primes in the list
  #TODO: return the total count
  return count  #TODO: replace this return line with the correct return value
  
def make_list(string_of_text):
  #TODO: string_of_text will be a single string with a series of words separated by a comma
  list_of_strings = string_of_text.split(', ')
  #TODO: convert string_of_text into a list of strings (hint: use .split to separate by comma)
  #TODO: return the list of strings
  return list_of_strings
  #TODO: replace this return line with the correct return value

def main():
  #TODO: create a list of strings that contains all first names of your team members (list_of_names)
  list_of_names = ['Vineet','Kelly','Vyvy','Abyan']
  #TODO: call the frame_this function and pass your list of names
  frame_this(list_of_names)
  # -------------do not change anything below this line----------#
  words_to_split = 'one, two, three, four hundred'
  words_list = make_list(words_to_split) # should result in the list ['one','two','three','four hundred']
  frame_this(words_list)
  numbers = [1,9,0,2,3,17,6,25,4,5,11,14]
  print('The list of numbers',numbers,'has',count_primes(numbers),'primes.')
  
if __name__=="__main__":
  main()