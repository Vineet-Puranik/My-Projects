def add_space_and_capitalize(word):
  #TODO: create a variable called new_word which starts as an empty string
  #TODO: write a for-loop that loops through each letter of the word passed as a parameter
    #TODO: for each letter, make it uppercase using .upper() and then add that letter to the new_word variable and add a space after it
  #TODO: return the new_word variable...do not print anything here, only return
  return '' #replace this line
  
def accrue_interest(loan_amount):
  #TODO: create a variable called loan_balance which starts with a value equal to the loan_amount parameter
  #TODO: create a variable called loan_interest which is 6% of the loan_amount (ie. multiply loan_amount by .06)
  #TODO: update the loan_balance variable by adding the loan_interest to it
  #TODO: return the loan_balance variable (do not print anything here, only return)
  return 0 #replace this line
  
def make_payment(loan_balance,payment_amount):
  #TODO: create a variable called remaining_balance which starts as 0
  #TODO: write an if-statement to check if the loan balance is less than or equal to the payment amount
    #TODO: if the loan balance is less than or equal to the payment amount that means the loan is paid off, so print "Paid Off!"
  #TODO: write an else to handle the other case (meaning the loan was not paid off)
    #TODO: inside the else, update the remaining_balance variable by setting it to the loan_balance minus the payment_amount
    #TODO: still inside the else, print "Paid $__" using .format to fill in the amount that was paid, using two decimals
  #TODO: now return the remaining_balance variable (make sure this is outside the if-else block)
  return 0 #replace this line
  
def display_balance(loan_balance):
  #TODO: print "Current Balance: $__" using .format to fill in the loan_balance with two decimals
  print() #replace this line
  
#### DO NOT CHANGE ANYTHING BELOW THIS LINE###
def main():
  big_text = 'finance'
  print(add_space_and_capitalize(big_text))
  loan = 12000
  display_balance(loan)
  loan = accrue_interest(loan)
  display_balance(loan)
  loan = make_payment(loan,2000)
  display_balance(loan)
  loan = accrue_interest(loan)
  display_balance(loan)
  loan = make_payment(loan,12000)
  display_balance(loan)
  
if(__name__=="__main__"):
  main()
