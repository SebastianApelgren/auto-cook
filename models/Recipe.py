from models.Ingredient import Ingredient

class Recipe:
    def __init__(self, name: str, ingredients: list[Ingredient], instructions: str):
        self.name = name
        self.ingredients = ingredients  # List of Ingredient objects
        self.instructions = instructions  # Step-by-step instructions

    def __str__(self):
        return f"Recipe for {self.name}:\nIngredients:\n" + \
               "\n" + ("") + \
               "\n\nInstructions:\n" + self.instructions
    
    def to_dict(self):
        return {
            "name": self.name,
            "ingredients": [ingredient.to_dict() for ingredient in self.ingredients],
            "instructions": self.instructions
        }

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)

    def get_ingredients(self):
        return self.ingredients

    def get_instructions(self):
        return self.instructions
    
    def get_name(self):
        return self.name

    def set_instructions(self, new_instructions):
        self.instructions = new_instructions