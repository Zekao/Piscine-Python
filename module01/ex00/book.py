from recipe import Recipe
from datetime import datetime

class Book:

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipes_type in self.recipes_list:
            for recipe in self.recipes_list[recipes_type]:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print("Recipe not found")
        return None
        

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        return_list = []
        for recipe in self.recipes_list[recipe_type]:
            return_list.append(recipe.name)
        return return_list  

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        assert (type(recipe) == Recipe), "recipe must be a Recipe instance"

        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
        return

    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': []
        }