import random

class Car:
  def __init__(self,name):
    #set self.name to name
    self.name = name
    #set self.speed to a random number between 60 and 100
    self.speed = int(random.uniform(60,100))
    #set self.max_distance to a random number between 450 and 550
    self.max_distance = int(random.uniform(450,550))
    
  def __str__(self):
    # return a string formatted with info for the name, speed, and max distance
    return 'Name: ' + self.name + ' ' + 'Speed: ' + str(self.speed) + ' ' + 'Distance: ' + str(self.max_distance)

class Race:
  def __init__(self):
    #set the distance to 500
    self.distance = 500
    self.racer_list = [] 

  def start_race(self,racers):
    #create a list attribute called racer_list
    #for each number from 0 up to racers (the total number of racers)
    for number in range(racers):
      my_racer = Car('Car ' + str(number))
      self.racer_list.append(my_racer)
      print(my_racer)
      #create a car named Car # (with the number)
      #add the car to the list
      #print the car details
    
  def get_winner(self):
    #create a variable called winner and set it equal to 'No winner'
    winner = 'No winner'
    #loop through all racers in the list of racers
    for my_racer in self.racer_list:
        if my_racer.max_distance > self.distance:
          if winner == 'No winner':
            winner = my_racer
          elif my_racer.speed >  winner.speed:
            winner = my_racer
        
    if winner == 'No winner':
      return winner
    else:
      return 'Winner: ' + winner.name 
    
def main():
  #create a new race indy = Race()
  indy = Race()
  #start a new race with 18 racers
  indy.start_race(18)
  #print the results of the race by calling get_winner() and printing the name
  new_winner = indy.get_winner()
  print(new_winner)
  #be sure your code still works if the result is "No winner"

if __name__=="__main__":
    main()
