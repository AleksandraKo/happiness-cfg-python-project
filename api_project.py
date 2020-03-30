import requests
import os

# Register to get an API key https://developer.edamam.com/edamam-recipe-api
api_id = os.environ.get("edamam_api_id")
api_key = os.environ.get("edamam_api_key")


def recipe_search(mealType):
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(mealType, api_id, api_key))
    data = result.json()
    return data['hits']


def run():
    mealType = input('Do you want breakfast, lunch, dinner or do you just want a snack? ')

    if mealType in ["lunch", "Lunch", "dinner", "Dinner"]:
        print("What type of cuisine do you fancy today?")


    else:
        recipes = recipe_search(mealType)
        for recipe in recipes:
            print(recipe['recipe']['label'])
            print(recipe['recipe']['url'])
            print()


run()
