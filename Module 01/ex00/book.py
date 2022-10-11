from datetime import datetime


class Book:
    def __init__(self, name):
        """Return the string to print with the recipe info"""
        if (not isinstance(name, str)):
            raise ValueError("Name is not a string !")

        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {
            "starter": {},
            "lunch": {},
            "dessert": {}
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""

        for type in self.recipes_list:
            recipe = self.recipes_list[type].get(name)
            if (recipe is not None):
                print(recipe)
                return recipe
        print("Recipe does not exist")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        [print(item) for item in self.recipes_list[recipe_type]]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        try:
            self.recipes_list[recipe.recipe_type][recipe.name] = recipe
            self.last_update = datetime.now()
        except TypeError:
            print("Recipe is not valid type !")
