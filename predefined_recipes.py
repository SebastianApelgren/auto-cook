# predefined_recipes.py

from models.Ingredient import Ingredient
from models.Recipe import Recipe
from Helpers.unsplash_helper import get_unsplash_image_url

# 1. Chicken Red Curry
recipe1 = Recipe(
    name="Chicken Red Curry",
    ingredients=[
        Ingredient("Chicken Breast", "500g", 5.50),
        Ingredient("Red Curry Paste", "3 tbsp", 1.50),
        Ingredient("Coconut Milk", "400ml", 2.00),
        Ingredient("Bell Peppers", "1, sliced", 1.20),
        Ingredient("Carrot", "1, sliced", 0.50),
        Ingredient("Garlic", "2 cloves, minced", 0.20),
        Ingredient("Ginger", "1 tsp, grated", 0.30),
        Ingredient("Fish Sauce", "1 tbsp", 0.40),
        Ingredient("Brown Sugar", "1 tbsp", 0.10),
        Ingredient("Basil Leaves", "a handful", 0.50),
        Ingredient("Oil", "1 tbsp", 0.10),
        Ingredient("Salt", "to taste", 0.05),
    ],
    instructions="""
    1. Heat oil in a large pan over medium heat. Add garlic and ginger, sauté until fragrant.
    2. Add the chicken breast and cook until lightly browned.
    3. Stir in the red curry paste and cook for 1-2 minutes until aromatic.
    4. Add coconut milk, bell peppers, and carrots. Bring to a simmer.
    5. Add fish sauce, sugar, and salt. Simmer for 10 minutes or until the vegetables are tender.
    6. Stir in basil leaves before serving. Serve hot with rice.
    """,
    image_url=get_unsplash_image_url("Chicken Red Curry")  # Replace with an actual image URL from Unsplash
)

# 2. Caesar Salad
recipe2 = Recipe(
    name="Caesar Salad",
    ingredients=[
        Ingredient("Romaine Lettuce", "1 head, chopped", 1.00),
        Ingredient("Chicken Breast", "200g, cooked and sliced", 2.50),
        Ingredient("Croutons", "1 cup", 1.20),
        Ingredient("Parmesan Cheese", "30g, shaved", 0.80),
        Ingredient("Caesar Dressing", "1/4 cup", 0.90),
        Ingredient("Salt", "to taste", 0.05),
        Ingredient("Black Pepper", "to taste", 0.10),
    ],
    instructions="""
    1. In a large bowl, add the chopped romaine lettuce.
    2. Add the cooked and sliced chicken breast, croutons, and Parmesan cheese.
    3. Drizzle with Caesar dressing and toss to combine.
    4. Season with salt and pepper to taste, and serve immediately.
    """,
    image_url=get_unsplash_image_url("Caesar Salad")  # Replace with an actual image URL from Unsplash
)

# 3. Pasta Alfredo with Chicken
recipe3 = Recipe(
    name="Pasta Alfredo with Chicken",
    ingredients=[
        Ingredient("Fettuccine Pasta", "300g", 1.50),
        Ingredient("Chicken Breast", "200g, sliced", 2.50),
        Ingredient("Butter", "3 tbsp", 0.60),
        Ingredient("Garlic", "2 cloves, minced", 0.20),
        Ingredient("Heavy Cream", "1 cup", 1.20),
        Ingredient("Parmesan Cheese", "1/2 cup, grated", 1.00),
        Ingredient("Salt", "to taste", 0.05),
        Ingredient("Black Pepper", "to taste", 0.10),
        Ingredient("Parsley", "1 tbsp, chopped (optional)", 0.15),
    ],
    instructions="""
    1. Cook the fettuccine according to the package instructions until al dente.
    2. In a large skillet, melt butter over medium heat. Add garlic and sauté until fragrant.
    3. Add the sliced chicken breast and cook until fully cooked through.
    4. Stir in the heavy cream and let it simmer for 3-4 minutes.
    5. Add the grated Parmesan cheese and stir until the sauce thickens.
    6. Season with salt and pepper. Add the cooked pasta and toss to coat with the sauce.
    7. Garnish with chopped parsley before serving.
    """,
    image_url=get_unsplash_image_url("Pasta Alfredo with Chicken")  # Replace with an actual image URL from Unsplash   
)

all_recipes = [recipe1.to_dict(), recipe2.to_dict(), recipe3.to_dict()]