import  sys
import  time

class Recipe:

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description=None, recipe_type=None, recipe=None):
        assert (type(name) == str), "Name must be a string"
        assert (type(cooking_lvl) == int or cooking_lvl in range(0, 6)), "cooking_lvl should be an integer between 1 and 5"
        assert (type(cooking_time) == int or cooking_time >= 0), "cooking_time should be an integer greater than 0"
        assert (type(ingredients) == list or len(ingredients) != 0), "ingredients should be a list not empty"
        assert (type(recipe_type) == str and recipe_type in ['starter', 'lunch', 'dessert']), "recipe_type should be a string and be in ['starter', 'lunch', 'dessert']"

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        self.recipe = recipe

    def __str__(self):
        """Return the string to print with the recipe info"""
        return_str = "Name: {}\nCooking lvl: {}\nCooking time: {}\nIngredients: {}\nDescription: {}\nRecipe type: {}\nRecipe: {}\n".format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type, self.recipe)
        return return_str