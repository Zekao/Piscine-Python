import sys
from book import Book
from recipe import Recipe


def main():
    tourte = Recipe("Tourte", 1, 30, ["pate", "oeuf", "lardons"], "Une tourte", "lunch")
    # print(str(tourte))

    book = Book("My book")
    book.add_recipe(tourte)
    book.get_recipe_by_name(tourte.name)
    print('test')
    print(book.get_recipes_by_types(tourte.recipe_type))


if __name__ == "__main__":
    sys.exit(main())