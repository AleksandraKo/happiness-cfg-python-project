import requests
import os

# Register to get an API key https://developer.edamam.com/edamam-recipe-api
api_id = os.environ.get("edamam_api_id")
api_key = os.environ.get("edamam_api_key")


def recipe_search(ingredient):
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, api_id, api_key))
    data = result.json()
    return data['hits']


def run():
    ingredient = input('Enter an ingredient: ')
    recipes = recipe_search(ingredient)
    for recipe in recipes:
        print(recipe['recipe']['label'])
        print(recipe['recipe']['url'])
        print()


run()
