      ####################################
      #####  Sampling Distributions  ##### 
      #####  and Standard Errors     #####
      ####################################

library(tidyverse)
library(mosaic)

# let's load our synthetic "population" of voters 
# in synthetic_voters.csv
glimpse(synthetic_voters)

# Here's our "population" of 20000 voters represented in a table of counts 
# by the presidential preference variable: 
synthetic_voters %>%
  group_by(pres) %>%
  summarize(counts = n())

# table of proportions:
synthetic_voters %>%
  group_by(pres) %>%
  summarize(prop = n()/nrow(synthetic_voters)) %>%
  ggplot() +
  geom_col(aes(x = pres, y = prop)) +
  ggtitle ("2020 Presidential Candidate Preference")



# use the prop() function to calculate a proportion
# notice it omits Trump: that's because Biden is first alphabetically
# and the "Trump" category is redundant once you know "Biden"
prop(~pres, data= synthetic_voters)

# let's store that computation in a variable called theta_biden
theta_biden = prop(~pres, data= synthetic_voters)

# Now let's simulate take a sample of size N=10 from our population
N = 10

# sample() function randomly selects designated number of rows in a data frame
# taking a random sample of 10 voters:
my_poll = sample(synthetic_voters, size = N)
  my_poll
# let's look at the proportion of Democrat vs. Republican voters in our sample
prop(~pres, data = my_poll)
   
# let's repeat the sampling process 5 times
# notice how every sample yields a different proportion
# that's sampling error!
do(5)*prop(~pres, data = sample(synthetic_voters, size = N))
   
# Let's now repeat this 1000 times 
sim1 = do(1000) * prop(~pres, data=sample(synthetic_voters, size=N))
head(sim1) # 1000 rows of a single column called prop_Biden

# make a histogram with results of simulation as data source:
ggplot(sim1) + 
  geom_histogram(aes(x=prop_Biden), binwidth = 0.01) + 
  # set x-axis limits to range from 0 to 1
  xlim(0,1) +        
  # we also add a vertical line at the true population value
  geom_vline(xintercept = theta_biden, color='blue')  
     

# This histogram is centered on the true value (which we happen to know in
# this example because we have the entire 'population').
# Taking samples, we don't see systematic departures from the true value 
# (i.e., no sampling bias) but we do see some spread around that value 
# (i.e., nonzero sampling variability).

# let's experiment with different sample sizes:
# try N = 50, 250, 1000

N = 1000
sim2 = do(10000) * prop(~pres, data=sample(synthetic_voters, size=N))

# histogram of the sampling distribution of our estimate:
ggplot(sim2) + 
  geom_histogram(aes(x=prop_Biden), binwidth = 0.01, color = 'white') + 
  xlim(0,1) +
  geom_vline(xintercept = theta_biden, color='blue') 

      # Remember: "standard error" is a formal math term -- it always means
      #   the standard deviation of the sampling distribution.
      # Margin of error is a colloquial term with no fixed mathematical meaning.
      # the "margin of error" often comes from going out 1 or 2 standard errors
      # on either side of the sample estimate.

# calculating standard error -- use the sd() function and the simulated 
# samples as the data source:

sd(~prop_Biden,data = sim2)





# keep in mind that this standard error is a property of the sampling procedure,
# not a property of a specific sample.

   ######################################
   ##### random sampling with MEANS #####

# we can also generate sampling distributions and calculate standard errors for 
# our estimates of a population mean
# let's use the built-in data set 'starwars' 
# (with data on the population of Star Wars characters)
data(starwars)
glimpse(starwars)

# let's filter our the missing values for height variable
starwars = starwars %>% 
   filter(height != 'NA')

# what is the mean height of SW characters?
mean (~height, data = starwars)
theta_height = mean (~height, data = starwars) # save population height value

# what if we take repeated samples of size 30 from the SW character population?
sim3 = do (10000)*mean(~height, data = sample(starwars, size = 30))
head (sim3)
   
# visualize our sampling distribution in a histogram:
ggplot(sim3) + 
   geom_histogram(aes(x=mean), color = 'whitesmoke') + 
   geom_vline(xintercept = theta_height, color='red4') 

# calculating standard error for the sampling distribution of a mean:

sd(~mean, data = sim3)

