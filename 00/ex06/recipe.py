cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'cake': {
        'ingredients': ['floor', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'chetomatoesse', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    },
}


def print_recipe_from_cookbook(recipe_name):
    if recipe_name not in cookbook:
        print('recipe', recipe_name, 'does not exist.')
        return
    recipe = cookbook[recipe_name]
    print(f'Recipe for {recipe_name}:')
    print('Ingredients list:', recipe['ingredients'])
    print(f"To be eaten for {recipe['meal']}.")
    print(f"Takes {recipe['prep_time']} minutes of cooking.")


def print_recipe():
    recipe = input("name: ").strip()
    print_recipe_from_cookbook(recipe)


def print_cookbook():
    if len(cookbook) == 0:
        print("cookbook is empty")
    for recipe in cookbook:
        print_recipe_from_cookbook(recipe)
        print('-'*42)


def add_recipe_to_cookbook(name, ingredients, meal, prep_time):
    cookbook[name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time
    }


def get_valid_value(prompt, is_valid, format):
    while True:
        value = input(prompt).strip()
        if is_valid(value):
            return format(value)
        print("error")


def add_recipe():
    name = get_valid_value("name: ", lambda e: len(e) > 0, lambda e: e.strip())

    ingredients = get_valid_value(
        "ingedients(separated by ','): ",
        lambda e: len(e) > 0,
        lambda e: e.split(','))
    ingredients = list(map(lambda e: e.strip(), ingredients))

    meal = get_valid_value(
        "meal type: ",
        lambda e: len(e) > 0,
        lambda e: e.strip())

    prep_time = get_valid_value(
        "preparation time in minutes: ",
        lambda e: e.isnumeric(),
        lambda e: int(e))

    add_recipe_to_cookbook(name, ingredients, meal, prep_time)
    print('recipe', name, 'added.')


def delete_recipe_from_cookbook(name):
    cookbook.pop(name, None)


def delete_recipe():
    name = input("name: ").strip()
    cookbook.pop(name, None)
    print('recipe', name, 'deleted.')


def print_options():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")


def main():
    while True:
        print_options()
        opt = input("> ")
        if not opt.isnumeric():
            continue

        opt = int(opt)
        if opt == 1:
            add_recipe()
        if opt == 2:
            delete_recipe()
        if opt == 3:
            print_recipe()
        if opt == 4:
            print_cookbook()
        if opt == 5:
            print('Thala :D')
            return
        print()


if __name__ == "__main__":
    main()
