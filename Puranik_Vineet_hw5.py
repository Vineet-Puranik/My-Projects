chicken_soup = ['chicken','chicken broth','carrots','celery','noodles']
lasagna = ['lasagna noodles' , 'pasta sauce', 'ricotta']
grilled_cheese = ['bread', 'butter', 'cheese']
garden_salad = ['lettuce', 'tomatoes', 'carrots', 'olives']
vineets_special = ['chicken', 'peanut oil', 'flour', 'paprika', 'cornstarch', 'egg']
recipe = input('Which recipe do you want to make: Choose[Chicken Soup, Lasagna, Grilled Cheese, Garden Salad, or Vineets special]: ').lower()
grocery_list = []
if(recipe == 'chicken soup'):
    ingredient1 = chicken_soup
    grocery_list.extend(chicken_soup)
    print('Chicken Soup: ', end = '')
elif(recipe == 'lasagna'):
    ingredient1 = lasagna
    grocery_list.extend(lasagna)  
    print('Lasagna: ', end = '')  
elif(recipe == 'grilled cheese'):
    ingredient1 = grilled_cheese
    grocery_list.extend(grilled_cheese)
    print('Grilled Cheese: ', end = '')
elif(recipe == 'garden salad'):
    ingredient1 = garden_salad
    grocery_list.extend(garden_salad)
    print('Garden Salad: ', end = '')
elif(recipe == 'vineets special'):
    ingredient1 = vineets_special
    grocery_list.extend(vineets_special)
    print('Vineet\'s Special: ', end = '')
for ingredient in ingredient1:
    if(ingredient == ingredient1[len(ingredient1) -1]):
        print(ingredient)
    else:
        print(ingredient, ',', end = '')
print(sep = '\n')
recipe2 = input('Choose another recipe you would like to make: Choose[Chicken Soup, Lasagna, Grilled Cheese, Garden Salad, or Vineets special]: ' ).lower()
if(recipe2 == 'chicken soup'):
    ingredient1 = chicken_soup
    grocery_list.extend(chicken_soup)
    print('Chicken Soup: ', end = '')
elif(recipe2 == 'lasagna'):
    ingredient1 = lasagna
    grocery_list.extend(lasagna)  
    print('Lasagna: ', end = '')  
elif(recipe2 == 'grilled cheese'):
    ingredient1 = grilled_cheese
    grocery_list.extend(grilled_cheese)
    print('Grilled Cheese: ', end = '')
elif(recipe2 == 'garden salad'):
    ingredient1 = garden_salad
    grocery_list.extend(garden_salad)
    print('Garden Salad: ', end = '')
elif(recipe2 == 'vineets special'):
    ingredient1 = vineets_special
    grocery_list.extend(vineets_special)
    print('Vineet\'s Special: ', end = '')
for ingredient in ingredient1:
    if(ingredient == ingredient1[len(ingredient1) -1]):
        print(ingredient)
    else:
        print(ingredient, ',', end = '')
print('', sep ='\n')
print('Grocery List: ', end = '' )
for ingredient in grocery_list:
    if(ingredient == grocery_list[len(grocery_list) -1]):
        print(ingredient)
    else:
        print(ingredient, ',', end = '')

item = input('What do you want on the list? ')
while(item.lower() != 'done'):
    grocery_list.append(item)
    item = input('What do you want on the list? [Type done when you are finished] ')
print('Grocery List:', end = ' ')

i = 0
while(i< len(grocery_list)-1):
    print(grocery_list[i], end = ', ')
    i+=1

print(grocery_list[len(grocery_list)-1])






