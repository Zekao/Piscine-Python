from recipe import Recipe
from datetime import datetime

class Book:

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipe in self.recipes_list:
            if recipe.name == name:
                print(recipe)
                return recipe
        print("Recipe not found")
        return None
        

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for recipe in self.recipes_list:
            if recipe.recipe_type == recipe_type:
                print(recipe)

        return

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipe_type].append(recipe_type)
        self.last_update = datetime.now()
        self.creation_date = datetime.now()       
        return

    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': []
        }