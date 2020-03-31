import requests
import os


api_id = os.environ.get('edamam_api_id')
api_key = os.environ.get('edamam_api_key')

def ingredient_search(ingredient):
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, api_id, api_key))
    data = result.json()
    return data['hits']

def mealtype_search(mealType):
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(mealType, api_id, api_key))
    data = result.json()
    return data['hits']

def diet_search(diet):
    output = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(diet, api_id, api_key))
    info = output.json()
    return info['hits']

def health_check(health):
    output = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(health, api_id, api_key))
    info = output.json()
    return info['hits']



def run():
    ingredient = input('What is the main ingredient that you want to cook with today (if you do not have one write "none"):')
    mealType = input('Do you want breakfast, lunch, dinner or do you just want a snack?').lower()

    if mealType in ['lunch','dinner']:
        diet = input('Would you like your {} to be more diet aware i.e. low-carb, high-protein, balanced?'.format(mealType)).lower() #this question only applies to lunch and dinner just to be able to narrow it down. The original idea was to do it with cuisinetype.

        if diet == 'yes':
            recipes = diet_search(diet) and mealtype_search(mealType) and ingredient_search(ingredient)
            for recipe in recipes:
                print(recipe['recipe']['label'])
                print(recipe['recipe']['url'])
                print(recipe['recipe']['calories'])
                print()

        else:
            recipes_0=  mealtype_search(mealType) and ingredient_search(ingredient)
            for recipe0 in recipes_0:
                print(recipe0['recipe']['label'])
                print(recipe0['recipe']['url'])
                print(recipe0['recipe']['calories'])
                print()

    else:
        recipes1 = mealtype_search(mealType) and ingredient_search(ingredient)
        for recipe1 in recipes1:
            print(recipe1['recipe']['label'])
            print(recipe1['recipe']['url'])
            print(recipe1['recipe']['calories'])
            print()



    serves = int(input('How many people are you serving?'))
    print('Please see the recipes which suit your other needs along with their serving sizes')

    recipes3 = mealtype_search(mealType) and ingredient_search(ingredient)
    for recipe3 in recipes3:
        serve = int(recipe3['recipe']['yield'])
        if serve == serves:
            print(recipe3['recipe']['label'])
            print(recipe3['recipe']['url'])
            print(recipe3['recipe']['calories'])
            print(recipe3['recipe']['yield'])
            print()

        else:
            print('No dishes were found to meet all criteria.')

    satisfaction = input('Are you satisfied with these selections?'.lower())
    if satisfaction == 'yes':
        print("Enjoy your dish!")


    else:
        health = input('Do you need to know options which are more suitable for those with dietary restrictions?'.lower())
        if health == 'yes':
            recipes2 = mealtype_search(mealType) and ingredient_search(ingredient) and health_check(health)
            for recipe2 in recipes2:
                print(recipe2['recipe']['label'])
                print(recipe2['recipe']['url'])
                print(recipe2['recipe']['calories'])
                print()
    print('End of program.')





run()