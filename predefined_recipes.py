# predefined_recipes.py

from models.Ingredient import Ingredient
from models.Recipe import Recipe

# Define Ingredient objects
garlic = Ingredient(name="Garlic", quantity="4 cloves", price=0.50)
olive_oil = Ingredient(name="Olive Oil", quantity="1/4 cup", price=1.50)
spaghetti = Ingredient(name="Spaghetti", quantity="200g", price=2.00)
parsley = Ingredient(name="Fresh Parsley", quantity="2 tbsp, chopped", price=0.25)
parmesan = Ingredient(name="Parmesan Cheese", quantity="1/4 cup, grated", price=1.00)

# Recipe 1: Spaghetti Aglio e Olio
spaghetti_aglio_e_olio = Recipe(
    name="Spaghetti Aglio e Olio",
    ingredients=[garlic, olive_oil, spaghetti, parsley, parmesan],
    instructions="""
    1. Cook the spaghetti in a large pot of salted boiling water until al dente. Drain and set aside.
    2. In a large skillet, heat the olive oil over medium heat. Add the garlic and sauté until golden brown.
    3. Toss the cooked spaghetti into the skillet and mix well.
    4. Season with salt to taste and add chopped parsley. Sprinkle with Parmesan cheese before serving.
    """
)

# Recipe 2: Garlic Bread
bread = Ingredient(name="Bread", quantity="1 loaf", price=1.50)
butter = Ingredient(name="Butter", quantity="100g", price=0.75)
garlic_bread = Recipe(
    name="Garlic Bread",
    ingredients=[bread, butter, garlic, parsley],
    instructions="""
    1. Preheat the oven to 350°F (175°C).
    2. Mix butter, garlic, and parsley together.
    3. Spread the mixture on the bread and bake for 10 minutes.
    """
)

# Recipe 3: Caesar Salad
lettuce = Ingredient(name="Romaine Lettuce", quantity="1 head", price=1.00)
croutons = Ingredient(name="Croutons", quantity="1 cup", price=0.50)
caesar_salad = Recipe(
    name="Caesar Salad",
    ingredients=[lettuce, croutons, parmesan],
    instructions="""
    1. Chop the lettuce and mix with croutons and grated Parmesan.
    2. Add Caesar dressing and toss well before serving.
    """
)

# Exporting recipes
all_recipes = [spaghetti_aglio_e_olio.to_dict(), garlic_bread.to_dict(), caesar_salad.to_dict()]