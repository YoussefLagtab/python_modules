def check_errors(list_to_check):
    for key, item in list_to_check.items():
        value = item[0]
        var_type = item[1]
        is_valid_func = item[2]
        msg = item[3]

        error = False
        if type(value) is not var_type:
            error = True
        elif is_valid_func and not is_valid_func(value):
            error = True
        if error:
            print(f'{key}: `{value}` must be {msg}')
            exit(1)


class Recipe:
    def __init__(
            self, name, cooking_lvl, cooking_time,
            ingredients, description, recipe_type):

        recipe_types = ["starter", "lunch", "dessert"]
        check_errors({
            'name': (name, str, lambda e: len(e) != 0,  "a non empty string"),
            'cooking_lvl':
                (cooking_lvl, int, lambda e: e >= 1 and e <= 5,
                    "an int between 1 and 5"),
            'cooking_time':
                (cooking_time, int, lambda e: e > 0,
                    "an int strictly posistive"),
            'ingredients':
                (ingredients, list,
                    lambda l: all(isinstance(e, str) and len(e) for e in l),
                    "a list of non empty strings"),
            'description': (description, str, None, "a string"),
            'recipe_type':
                (recipe_type, str, lambda e: e in recipe_types,
                    f"one of {recipe_types}")
        })

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        text = f"name: {self.name}\n"
        text += f"cooking_lvl: {self.cooking_lvl}\n"
        text += f"cooking_time: {self.cooking_time}\n"
        text += f"ingredients: {self.ingredients}\n"
        text += f"description: {self.description}\n"
        text += f"recipe_type: {self.recipe_type}"
        return text
