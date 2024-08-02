      ##### Models with grouped data #####
library(tidyverse)
library(mosaic)

# rxntime = read.csv('../data/rxntime.csv')
# key variables here are:
# - Subject: numerical code for which Subject the timing was for
# - FarAway: whether the object in the image was far away or not
# - Littered: whether the scene in the image was cluttered with other distractors or not
# - PictureTarget.RT: reaction time to identify object in milliseconds (1000 = 1 second)


######
# Day 1: grouping variables
######

###
# Part I: Littered and FarAway effects only
###

# Basic model: is the image cluttered ("littered") or not?
# this was a British lab so they say "littered" for "cluttered"
lm0 = lm(PictureTarget.RT ~ Littered, data = rxntime)
coef(lm0)
   
507 + 87
# now adding the FarAway dummy variable
lm1 = lm(PictureTarget.RT ~ Littered + FarAway, data = rxntime)
coef(lm1)
482 + 87 + 50
482 + 50
# Intercept = 481: baseline RT when scene has Littered=0, Faraway=0
# Littered = 87: change in average RT whenever Littered=1
# FarAway = 50: change in average RT whenever FarAway=1

# Notice that the coefficient on Littered didn't change when 
# we added the FarAway variable
# This is quite a special set of circumstances!
# It's because this was a designed experiment, and they designed it
# so that the Littered and FarAway variables wouldn't be correlated with each other.
# More on this delicate topic next week.


####
# Part 2: adding subject-level dummy variables
####

# Once you understand the basic recipe for incorporating
# two categorical predictors, you can easily extend that
# recipe to build a model involving more than two. 

# For example, notice that reaction differs a lot subject by subject:
                        # subject_means = rxntime %>%
                        #   group_by(Subject) %>%
                        #   summarize(mean_RT = mean(PictureTarget.RT))

subject_means = rxntime %>%
  group_by(Subject) %>%
  summarize( mean_RT = mean(PictureTarget.RT))
# arrange the subjects by mean reaction time, from gamer to Grandma
                        # subject_means %>%
                        #   arrange(mean_RT)
subject_means %>%
  arrange(desc(mean_RT))

ggplot(rxntime) +
  geom_boxplot(aes(x = Subject, y = PictureTarget.RT))
# So we should probably include Subject-level dummy variables
# in our model of reaction time!
# But a subtle issue here is that Subject is encoded as a number,
# despite being a categorical variable.

# Notice what goes wrong when, e.g. we try a boxplot.
# we expect 12 boxplots and only get 1 -- what's wrong!?



# R has no way of knowing that this number is just a label,
# and that it isn't really a numerical variable.  We have to tell it!
# Solution: use factor to tell R that Subject is categorical, not numerical

rxntime = rxntime %>%
  mutate( Subject = factor(Subject))

# Now boxplot works as expected:



# And now we're ready to build our model.
lm2 = lm(PictureTarget.RT ~ Littered + FarAway + Subject, data = rxntime)
   
coef(lm2) %>% round(0)
   
# A lot of coefficients!  We'll interpret these below.

##Subject 8
560 -90
   
##Subject14 If the scene is littered, far away
560 + 87 + 50 - 112

## Subject 26 when the object is close but it is littered
560 - 79 + 87


# How do we know what the "baseline" subject is?
# subject 6 comes first alphabetically -- so they're the baseline
# note: count(Subject) is shorthand for group_by(Subject) %>% summarize(n = n())

   
   
# What does the coefficient on (for example) Subject 9 mean?

# this says that subject 9's reaction time is, on average,
# 136 milliseconds less than the average of subject 6 (the baseline)

# Would would we predict for Subject 13 in a scenario where Littered=0, FarAway=1?
# Answer: sum the corresponding coefficients!
# baseline + FarAway effect + Subject 13 effect

                              # 560 + 50 - 147

# Would would we predict for Subject 6 in a scenario where Littered=1, FarAway=1?
# Answer: sum the corresponding coefficients!
# baseline + Littered effect + FarAway effect
# (no subject effect because Subject 6 is the baseline)

                              # 560 + 87 + 50


######
# Day 2: interactions and ANOVA
######

####
# Part III: with an interaction
####

# let's look at jitter plot
                        # ggplot(rxntime, aes(x=factor(Littered), y=PictureTarget.RT)) + 
                        #   geom_jitter() +
                        #   facet_wrap(~FarAway) + 
                        #   stat_summary(fun='mean', color='darkorange')  # this layer adds the group means


ggplot(rxntime, aes(x = factor(Littered), y = PictureTarget.RT)) + 
  geom_jitter() +
  facet_wrap(~FarAway) +
  stat_summary(fun = "mean", color = "darkorange")
  
# compare the difference in the left panel vs. the difference in the right panel.
# looks like a higher "Littered" effect for the FarAway=1 case...
# that calls for an interaction!

# so let's fit one:
lm3 = lm(PictureTarget.RT ~ Littered + FarAway + Littered:FarAway, data = rxntime)
   coef(lm3) %>% round(0)
   
   491 + 68 + 31+ 39
# let's walk through each term and interpret it
# Intercept = 491: baseline RT when scene has Littered=0, Faraway=0
# Littered = 68: change in average RT whenever Littered=1
# FarAway = 31: change in average RT whenever FarAway=1
# Littered:FarAway  = 39: _additional change_ in average RT when both Littered=1 and FarAway=1

# So what would our prediction be for a scene that is both Littered and FarAway?
# Answer: baseline + Littered effect + FarAway effect + Interaction
# = 491 + 68 + 31 + 39 = 629

# This is what we get from mean() directly:
   
mean(PictureTarget.RT ~ FarAway + Littered, data = rxntime)

# Let's look at the coefficient confidence intervals
confint(lm3) %>% round(3)

# a better table for regression model results? get_regression_table!
library(moderndive)
get_regression_table(lm3)

####
# Part IV: Analysis of variance
####
library(effectsize)

# Let's re-introduce subject-specific dummy variables to the equation
lm4 = lm(PictureTarget.RT ~ FarAway + Littered + factor(Subject) + Littered:FarAway, data = rxntime)
coef(lm4) %>% round(0)
   
   570 + 68 + 31 - 147 + 39
   
   570 + 68 -147

# This model says that each subject has a different average reaction time 
# (think: gamer vs. Grandma)
# but that the effect of Littered and FarAway is common to all subjects

# overall r-squared of the model

   rsquared(lm4)
   
# an ANOVA table for this last model:

eta_squared(lm4, partial = FALSE)