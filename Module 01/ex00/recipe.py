

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        """Return the string to print with the recipe info"""
        if (not isinstance(name, str)):
            raise ValueError("Name is not a string !")
        if (not isinstance(cooking_lvl, int) or not (1 <= cooking_lvl <= 5)):
            raise ValueError("Cooking lvl is not valid !")
        if (not isinstance(cooking_time, int) or cooking_time <= 0):
            raise ValueError("Cooking time is not valid !")
        if (not isinstance(ingredients, list) or not all([isinstance(item, str) for item in ingredients])):
            raise ValueError("Ingredients is not valid !")
        if (not isinstance(description, str)):
            raise ValueError("Description is not a string !")
        if (not isinstance(recipe_type, str) or recipe_type not in ["starter", "lunch", "dessert"]):
            raise ValueError("Recipe type is not valid !")
        if (not name or not recipe_type or not all([len(item) > 0 for item in ingredients]) or len(ingredients) == 0):
            raise ValueError("One of the argument is empty !")

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "{} is a {} star{} {}\nIt take {} minute{} of your time.\nIngredients: {}\nDescription: {}".format(
            self.name,
            self.cooking_lvl,
            "s" if self.cooking_lvl > 1 else "",
            self.recipe_type,
            self.cooking_time,
            "s" if self.cooking_time > 1 else "",
            self.ingredients,
            self.description
        )
        return txt
