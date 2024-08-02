##### CLT with means, difference of proportions  ####
##### and regression models                     ####

library(tidyverse)
library(mosaic)

# Let's take the DFW store alone, using filter

kroger_dfw = filter(kroger, city == "Dallas")
  
# What's the mean weekly sales volume in this store?

ggplot(kroger_dfw) + 
  geom_histogram(aes(x = vol))

# mean, std dev, and sample size

favstats(~vol, data = kroger_dfw)

# de Moivre's equation says is that our standard error of the mean is
2353.64/sqrt(61)

# let's compare this with our bootstrapped standard error
boot_cheese = do(10000) *mean(~vol, data = resample(kroger_dfw))

# calculate bootstrapped standard error
# pretty close!
sd(~mean, data  = boot_cheese)

# 95% bootstrap confidence interval

confint(boot_cheese)
# compare with the CLT-based confidence interval:
4356.508 - 2*2353.645/sqrt(61)
4356.508 + 2*2353.645/sqrt(61)


# doing this by hand is awful.  use t.test instead:

t.test(~vol, data = kroger_dfw)

# take-home message: CLT and bootstrapping
# give nearly identical confidence intervals

####### Difference in proportions #######
# create new binary variable for volume < 5000 and >= 5000 using mutate

kroger = kroger %>%
  mutate(isvol_high = ifelse(vol>=5000, "TRUE", "FALSE"))

##if volume is greater than equal to 5000 say true else say false
# create a table of counts (xtabs) for 'isvol_high' crossed with 'disp'

xtabs(~isvol_high + disp, data = kroger)

# Let's look at high cheese volume proportions by display status...
prop(isvol_high~disp, data = kroger)
## second variable is always how you are going to group things 
# so when there was a display, high volume sales rate was .406
# when there is no display, high volume sales rate is 0.217 
# about a 19% difference
diffprop(isvol_high~disp, data = kroger)

# confidence interval for the difference:
# about 0.12 to 0.26

prop.test(isvol_high~disp, data = kroger)
# notice order of proportions when using prop.test()
# prop.test() function default is prop 1-prop 2  
# here, prop 1-prop 2 = no minus yes
# whereas the default for diffprop() is yes minus no
# check two proportions at the bottom of prop.test() output!
# this will help you get oriented for interval interpretation


# compare with bootstrapping:
boot_prop = do(10000)* diffprop(isvol_high~disp, data = resample(kroger))
  
confint(boot_prop) 

####### Regression models #######

# Look at volume as a function of price in the kroger_dfw file with scatterplot

ggplot(kroger_dfw) +
  geom_point(aes(x = price, y = vol))

# Fit a linear model to explain volume as a function of price
lm1 = lm(vol~price, data = kroger_dfw)
## y ~x
coef(lm1)

# A $1 change is too much. Create new variable "penny_price" and rerun lm
kroger_dfw = kroger_dfw %>%
  mutate(penny_price = price*100)

lm1 = lm(vol~penny_price, data = kroger_dfw)
  
coef(lm1) 

# what about conveying our uncertainty about this slope estimate?
# let's bootstrap the interval as we've done in Lesson 9... 
# then compare the bootstrap interval with the CLT-based interval
boot_lm = do(10000)*lm(vol~penny_price, data = resample(kroger_dfw))
  
confint(boot_lm)

# optional but useful code for streamlined confint() output:
confint(boot_lm) %>% 
  select(-level, -method) %>%   # don't show extraneous columns in output
  mutate_if(is.numeric, round, digits=2)    # fancy rounding
##-39.52 to -27.91
# to get the CLT-based interval, just pipe the fitted model 
# (here, named lm1) directly to the confint() function
lm1 %>%
  confint()

options(scipen = 999)  # get rid of scientific notation

# syntax options: specify the model directly in confint() 
# function for CLT-based intervals (no need to bootstrap first)
confint(lm(vol~penny_price, data=kroger_dfw))

confint(lm1) %>% round(2)
