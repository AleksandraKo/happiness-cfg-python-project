#This is a recipe generator that will give out results based on your inputs i.e. key ingredient, health etc.

import requests
import os


api_id = os.environ.get('edamam_api_id')
api_key = os.environ.get('edamam_api_key')


def ingredient_search(ingredient):
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, api_id, api_key))
    data = result.json()
    return data['hits']


def mealtype_search(mealType):
    result1 = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(mealType, api_id, api_key))
    data = result1.json()
    return data['hits']


def diet_search(diet):
    output = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(diet, api_id, api_key))
    info = output.json()
    return info['hits']


def health_check(health):
    output1 = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(health, api_id, api_key))
    info = output1.json()
    return info['hits']

#The functions above are for searching recipes based on the
# categories in the brackets


#Function below incorporaes all of the functions above to generate recipes

def main():
    ingredient = input('What is the main ingredient that you want to cook with today (if you do not have one write "none"):').lower()

    mealType = input('Do you want breakfast, lunch, dinner or do you just want a snack?').lower()

    if mealType in ['lunch','dinner']:
        diet = input('Would you like your {} to be more diet aware i.e. low-carb, high-protein, balanced?'.format(mealType)).lower()

        if diet == 'yes':
            recipes = diet_search(diet) and mealtype_search(mealType) and ingredient_search(ingredient)

            for recipe in recipes:
                print(recipe['recipe']['label'])
                print(recipe['recipe']['url'])
                print('Calories (kcal):')
                print(int(recipe['recipe']['calories']))
                print()

        else:
            recipes_0 = mealtype_search(mealType) and ingredient_search(ingredient)

            for recipe0 in recipes_0:
                print(recipe0['recipe']['label'])
                print(recipe0['recipe']['url'])
                print('Calories (kcal):')
                print(int(recipe0['recipe']['calories']))
                print()

    else:
        recipes1 = mealtype_search(mealType) and ingredient_search(ingredient)

        for recipe1 in recipes1:
            print(recipe1['recipe']['label'])
            print(recipe1['recipe']['url'])
            print('Calories (kcal):')
            print(int(recipe1['recipe']['calories']))
            print()


    serves = int(input('How many people are you serving? (please enter an integer value):'))

    print('Please see the recipes which suit your other needs along with their serving sizes')


    recipes3 = mealtype_search(mealType) and ingredient_search(ingredient)

    for recipe3 in recipes3:
        serve = int(recipe3['recipe']['yield'])

        if serve == serves:
            print(recipe3['recipe']['label'])
            print(recipe3['recipe']['url'])
            print('Calories (kcal):')
            print(int(recipe3['recipe']['calories']))
            print('Servings:')
            print(int(recipe3['recipe']['yield']))
            print()


    print('No other dishes were found to meet all criteria.')


    satisfaction = input('Are you satisfied with these selections?').lower()

    if satisfaction == 'yes':
        print('Enjoy your meal!')

    else:
        health = input('Do you need to know options which are more suitable for those with dietary restrictions?').lower()

        if health == 'yes':
            recipes2 = mealtype_search(mealType) and ingredient_search(ingredient) and health_check(health)

            for recipe2 in recipes2:
                print(recipe2['recipe']['label'])
                print(recipe2['recipe']['url'])
                print('Calories (kcal):')
                print(int(recipe2['recipe']['calories']))
                print()
                print('Amazing! We hope you enjoy your meal!')

        else:
            print("Sorry we coldn't help you today! :(")


main()