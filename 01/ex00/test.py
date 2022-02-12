from recipe import Recipe
from book import Book

my_book = Book('choumicha_book')

my_book.add_recipe(Recipe('salad', 1, 15, ['maticha', 'khess'], '', 'starter'))
my_book.add_recipe(Recipe(
    'tanjiya', 1, 400, ['bzaf l7em', '3atriya'], 'ya salam', 'lunch'))
my_book.add_recipe(Recipe('zero', 1, 15, ['one', 'two'], '', 'dessert'))
my_book.add_recipe(Recipe('danon', 1, 15, ['three'], '', 'dessert'))
my_book.add_recipe(Recipe('danon', 2, 5, ["3"], '', 'dessert'))


print('# get recipe tanjiya')
print(my_book.get_recipe_by_name('tanjiya'))
print('=' * 42)

print('# get all desserts ')
all_dessert = my_book.get_recipes_by_types('dessert')
for d in all_dessert:
    print(d)
    print('-' * 13)
print('=' * 42)

print('# get recipe that does not exist')
print(my_book.get_recipe_by_name('pizza'))
