cookbook = {
  "sandwich": {'ingredients': 'ham, bread, cheese and tomatoes.', 'meal': 'lunch', 'prep_time': 10},
  "cake": {'ingredients': 'flour, sugar and eggs', 'meal': 'desert', "prep_time": 60},
  "salad": {'ingredients': 'avocado, arugula, tomatoes and spinach', 'meal': 'lunch', "prep_time": 15},
}

def add_recipe():
    name = input("Please enter a name for the recipe:")
    ingredients = input("Please enter the list of ingredients:")
    type_meal = input("Please enter the type of meal:")
    time_cook = input("Please enter the cook duration:")
    cookbook[name] = {'ingredients': ingredients, 'meal': type_meal, 'prep_time': time_cook}

def delete_recipe():
    name = input("Please enter a name for a recipe to delete: ")
    if name in cookbook:
        del cookbook[name]
    cookbook.update()

def print_recipe():
    name = input("Please enter the recipe's name to get its details: ")
    if name in cookbook:
        print('Ingredients list:', cookbook[name]['ingredients'])
        print('To be eaten for', cookbook[name]['meal'])
        print('Takes', cookbook[name]['prep_time'], 'minutes of cooking')
    else:
        print("This recipe isn't present in the book")

def print_cookbook():
    size = len(cookbook)
    print('number of recipes in the book:', size)
    recipes_name =  list(cookbook.keys())[:size]
    print(recipes_name)

def quit_cookbook():
    print('Exited the recipe cookbook')

def main():
    while 1:
        text = input('Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n')
        if text is '1':
            add_recipe()
        elif text is '2':
            delete_recipe()
        elif text is '3':
            print_recipe()
        elif text is '4':
            print_cookbook()
        elif text is '5':
            return quit_cookbook()
        else:
            print('>>>Incorrect option<<<')
if __name__=="__main__":
    main()