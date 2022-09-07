from book import Book
from recipe import Recipe 

def main():
    book = Book("My Book")
    recipe = Recipe("Cake", 1, 10, ["flour", "sugar", "eggs"], "Mix everything", "Bake 30 min at 180°C")
    book.add_recipe(recipe)
    book.get_recipe_by_name("Cake")
    book.get_recipes_by_types("dessert")

if __name__ == "__main__":
    main()
