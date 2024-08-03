#variables for score and categorization
gryffindor_points = 0
hufflepuff_points = 0
ravenclaw_points = 0
slytherin_points = 0
print ('What Hogwarts house do you truly belong in?  Lets find out!')
wand = input ('You have just bought a wand at Hogwarts. What core does it have?  Choose [Phoenix Feather, Dragon Heartstring, Unicorn Hair, or Black Walnut] ')
if (wand.lower() == 'phoenix feather'):
    gryffindor_points = gryffindor_points + 1
elif (wand.lower() == 'dragon heartstring'):
    slytherin_points = slytherin_points + 1
elif (wand.lower() == 'unicorn hair'):
    ravenclaw_points = ravenclaw_points + 1
elif (wand.lower() == 'black walnut'):
    hufflepuff_points = hufflepuff_points +1
else:
    print ('Invalid Selection. Please restart and select one of the 4 responses!')
emotion = input ('Which of these words describes you the most?  Choose [Brave, Intelligent, Empathetic, Ambitious] ')
if (emotion.lower() == 'brave'):
    gryffindor_points = gryffindor_points + 1
elif (emotion.lower() == 'ambitious'):
    slytherin_points = slytherin_points + 1
elif (emotion.lower() == 'intelligent'):
    ravenclaw_points = ravenclaw_points + 1
elif (emotion.lower() == 'empathetic'):
    hufflepuff_points = hufflepuff_points + 1
else:
    print('Invalid Selection. Please restart and select one of the 4 responses!')
quidditch = input ('What role would you play in a Quidditch match?  Choose [Seeker, Chaser, Beater, or Spectator] ')
if (quidditch.lower() == 'seeker'):
    gryffindor_points = gryffindor_points + 1
elif (quidditch.lower() == 'beater'):
    slytherin_points = slytherin_points + 1
elif (quidditch.lower() == 'chaser'):
    ravenclaw_points = ravenclaw_points + 1
elif (quidditch.lower() == 'spectator'):
    hufflepuff_points = hufflepuff_points + 1
else:
    print('Invalid Selection. Please restart and select one of the 4 responses!')
pet = input ('What pet would you have at Hogwarts?  Choose[Owl, Cat, Toad, or Snake] ')
if (pet.lower() == 'owl'):
    gryffindor_points = gryffindor_points + 1
elif (pet.lower() == 'snake'):
    slytherin_points = slytherin_points + 1
elif (pet.lower() == 'toad'):
    ravenclaw_points = ravenclaw_points + 1
elif (pet.lower() == 'cat'):
    hufflepuff_points = hufflepuff_points + 1
else:
    print('Invalid Selection. Please restart and select one of the 4 responses!')
experience = input ('Which of these magical experiences would you like to experience?  Choose [The Triwizard Tournament, The Quidditch World Cup, The Yule Ball, Christmas at Hogwarts] ')
if (experience.lower() == 'the quidditch world cup'):
    gryffindor_points = gryffindor_points + 1
elif (experience.lower() == 'the triwizard tournament'):
    slytherin_points = slytherin_points + 1
elif (experience.lower() == 'christmas at hogwarts'):
    ravenclaw_points = ravenclaw_points + 1
elif (experience.lower() == 'the yule ball'):
    hufflepuff_points = hufflepuff_points + 1
else:
    print('Invalid Selection. Please restart and select one of the 4 responses!')

if(gryffindor_points > hufflepuff_points and gryffindor_points > ravenclaw_points and gryffindor_points > slytherin_points):
    print('You belong in Gryffindor! As a gryffindor you stand up for other, speak up and take action when you can, be a class clown, and have a competitive nature!')
elif(hufflepuff_points > gryffindor_points and hufflepuff_points > ravenclaw_points and hufflepuff_points > slytherin_points):
    print('You belong in Hufflepuff! As a hufflepuff you have a strong code of ethics, persistent, loyal, and have a compassionate nature!')
elif(ravenclaw_points > gryffindor_points and ravenclaw_points > hufflepuff_points and ravenclaw_points > slytherin_points):
    print('You belong in Ravenclaw! As a ravenclaw you love to analyze, be an overachiever, not afraid to be alone, and know a lot of quick facts!')
elif(slytherin_points > gryffindor_points and slytherin_points > hufflepuff_points and slytherin_points > ravenclaw_points):
    print('You belong in Slytherin! As a slytherin you enjoy dark humor, value your reputation, take care of your appearance, and never lets anyone see your soft side!')
else:
    opinion = input ('The sorting hat is still uncertain! Which house do you prefer! Choose[Gryffindor, Hufflepuff, Ravenclaw, or Slytherin] ')
    if(opinion.lower() == 'gryffindor'):
        gryffindor_points = gryffindor_points + 10
    elif(opinion.lower() == 'hufflepuff'):
        hufflepuff_points = hufflepuff_points + 10
    elif(opinion.lower() == 'ravenclaw'):
        ravenclaw_points = ravenclaw_points + 10
    elif(opinion.lower() == 'slytherin'):
        slytherin_points = slytherin_points + 10
    else:
        print('Invalid Selection. Please restart and select one of the 4 responses!')
    if(gryffindor_points > hufflepuff_points and gryffindor_points > ravenclaw_points and gryffindor_points > slytherin_points):
        print('You belong in Gryffindor! As a gryffindor you stand up for other, speak up and take action when you can, be a class clown, and have a competitive nature!')
    elif(hufflepuff_points > gryffindor_points and hufflepuff_points > ravenclaw_points and hufflepuff_points > slytherin_points):
        print('You belong in Hufflepuff! As a hufflepuff you have a strong code of ethics, persistent, loyal, and have a compassionate nature!')
    elif(ravenclaw_points > gryffindor_points and ravenclaw_points > hufflepuff_points and ravenclaw_points > slytherin_points):
        print('You belong in Ravenclaw! As a ravenclaw you love to analyze, be an overachiever, not afraid to be alone, and know a lot of quick facts!')
    elif(slytherin_points > gryffindor_points and slytherin_points > hufflepuff_points and slytherin_points > ravenclaw_points):
        print('You belong in Slytherin! As a slytherin you enjoy dark humor, value your reputation, take care of your appearance, and never lets anyone see your soft side!')        


print('Here is a breakdown of your house score:', 'Gryffindor points =', gryffindor_points, 'Hufflepuff points =', hufflepuff_points, 'Ravenclaw points =', ravenclaw_points, 'Slytherin Points =', slytherin_points, sep = '\n')
    





