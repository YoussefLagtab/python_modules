from datetime import time as now
from recipe import Recipe, check_errors


class Book:
    def __init__(self, name):
        check_errors(
            {'name': (name, str, lambda e: len(e) != 0, "a non empty string")}
        )

        self.name = name
        self.last_update = now()
        self.creation_date = now()
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': []
        }

    def add_recipe(self, recipe):
        check_errors({'recipe': (recipe, Recipe, None, "a recipe object")})

        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = now()

    def get_recipe_by_name(self, name):
        all_recipes = self.recipes_list['starter']
        all_recipes += self.recipes_list['lunch']
        all_recipes += self.recipes_list['dessert']

        recipe = next((r for r in all_recipes if r.name == name), None)
        return recipe

    def get_recipes_by_types(self, recipe_type):
        return self.recipes_list[recipe_type]
