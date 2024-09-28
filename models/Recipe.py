from models.Ingredient import Ingredient

class Recipe:
    name: str
    ingredients: list[Ingredient]
    instructions: str
    image_url: str

    def __init__(self, name: str, ingredients: list[Ingredient], instructions: str, image_url: str):
        self.name = name
        self.ingredients = ingredients  # List of Ingredient objects
        self.instructions = instructions  # Step-by-step instructions
        self.image_url = image_url # URL of the image of the dish

    def __str__(self):
        return f"Recipe for {self.name}:\nIngredients:\n" + \
               "\n" + ("") + \
               "\n\nInstructions:\n" + self.instructions
    
    def to_dict(self):
        return {
            "name": self.name,
            "ingredients": [ingredient.to_dict() for ingredient in self.ingredients],
            "instructions": self.instructions,
            "image_url": self.image_url
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
    
    def get_image_url(self):
        return self.image_url
    
    def set_image_url(self, new_image_url):
        self.image_url = new_image_url
    
    def get_name(self):
        return self.name

    def set_instructions(self, new_instructions):
        self.instructions = new_instructions