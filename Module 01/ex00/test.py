from book import Book
from recipe import Recipe
import unittest


class TestBook(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(TypeError):
            Book()

    def test_wrong_name(self):
        with self.assertRaises(ValueError):
            Book(5)

    def test_add_recipe(self):
        print("add multiple recipe")
        book = Book("My Book")
        book.add_recipe(Recipe("test", 5, 5, ["tomato"], "tomato test", "lunch"))
        book.add_recipe(Recipe("carry", 5, 5, ["tomato"], "tomato test", "lunch"))
        book.add_recipe(Recipe("azerty", 5, 5, ["tomato"], "tomato test", "lunch"))
        book.add_recipe(Recipe("qsdf", 5, 5, ["tomato"], "tomato test", "lunch"))
        book.add_recipe(Recipe("test", 5, 5, ["tomato"], "tomato test", "lunch"))
        book.get_recipes_by_types("lunch")

    def test_get_recipe(self):
        print("find one recipe")
        book = Book("My Book")
        book.add_recipe(Recipe("test", 5, 5, ["tomato"], "tomato test", "lunch"))
        book.get_recipe_by_name("test")


if __name__ == '__main__':
    unittest.main()
