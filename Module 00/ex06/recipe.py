cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time":10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time":60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time":15
    },
}

def recipesName():
    for el in cookbook:
        print(el)


def recipe(name):
    if name in cookbook:
        print("Ingredient list: {}".format(cookbook[name]["ingredients"]))
        print("To be eaten for {}".format(cookbook[name]["meal"]))
        print("Take {} minute{} of cooking".format(cookbook[name]["prep_time"], "s" if cookbook[name]["prep_time"] > 1 else ""))
    else:
        print("Recipe does not exist.")

def delRecipe(name):
    if name in cookbook:
        del cookbook[name]
        print("Recipe deleted !")
    else:
        print("Recipe does not exist.")

def IntInput(content):
     while True:
        try:
            return(int(input(content)))
        except:
            print("That's not a valid option !")

def addRecipe():
    key = input("Enter a name: ")
    value = {
        "ingredients": input("Enter ingredients: ").split(" "),
        "meal": input("Enter a meal type: "),
        "prep_time": IntInput("Enter a preparation time: "),
    }
    cookbook[key] = value
    print("Recipe added !")

def main():
    print("Welcome to the Python Cookbook !")
    print("List of available option:\n\
            1: Add a recipe\n\
            2: Delete a recipe\n\
            3: Print a recipe\n\
            4: Print the cookbook\n\
            5: Quit"
    )
    while True:
        opt = -1
        while True:
            opt = IntInput("Please select an option: ")
            if (opt < 1 or opt > 5):
                print("That's not a valid option !")
            else:
                break
        match opt:
            case 1:
                addRecipe()
            case 2:
                delRecipe(input("Enter a recipe name: "))
            case 3:
                recipe(input("Enter a recipe name: "))
            case 4:
                recipesName()
            case 5:
                print("GoodBye")
                break

main()