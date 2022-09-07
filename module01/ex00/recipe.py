import  sys
import  time

def valid_content(name, cooking_lvl, cooking_time, ingredients, description, recipe):
    assert (type(name) != str or name != ""), "name should be a string not empty"
    assert (type(cooking_lvl) != int or cooking_lvl in range(0, 6)), "cooking_lvl should be an integer between 1 and 5"
    assert (type(cooking_time) != int or cooking_time >= 0), "cooking_time should be an integer greater than 0"
    assert (type(ingredients) != list or len(ingredients) != 0), "ingredients should be a list not empty"
    assert (type(recipe) != list or len(recipe) == 0), "recipe should be a list not empty"
    return True
class Recipe:



    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description=None, recipe_type=None, recipe=None):
            if (valid_content(name, cooking_lvl, cooking_time, ingredients, description, recipe) is True):
                self.name = name
                self.cooking_lvl = cooking_lvl
                self.cooking_time = cooking_time
                self.ingredients = ingredients
                self.description = description
                self.recipe = recipe
                self.recipe_type = recipe_type
            else:
                print("Invalid content")
                sys.exit(0)

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "Recipe: "
        for content in self:
            txt += str(content) + ", "
        return txt