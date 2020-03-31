import requests
import os

# Register to get an API key https://developer.edamam.com/edamam-recipe-api
api_id = os.environ.get('edamam_api_id')
api_key = os.environ.get('edamam_api_key')


def recipe_search(mealType):
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(mealType, api_id, api_key))
    data = result.json()
    return data['hits']

def another_search(diet):
    output = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(diet, api_id, api_key))
    info = output.json()
    return info['hits']

def run():
    mealType = input('Do you want breakfast, lunch, dinner or do you just want a snack?').lower()

    if mealType in ['lunch','dinner']:
         diet = input('Would you like your {} to be more diet aware i.e. low-carb, high-protein, balanced?'.format(mealType))


         if diet == 'yes':
             recipes = another_search(diet) and recipe_search(mealType)
             for recipe in recipes:
                 print(recipe['recipe']['label'])
                 print(recipe['recipe']['url'])
                 print(recipe['recipe']['calories'])
                 print()
    else:
        recipes1 = recipe_search(mealType)
        for recipe in recipes1:
            print(recipe['recipe']['label'])
            print(recipe['recipe']['url'])
            print(recipe['recipe']['calories'])
            print()


run()
