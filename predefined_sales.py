import json

# Manually extracted product data from the new image and translated to English

products_updated = [
    {
        "name": "Smoked Ham Deluxe",
        "price": 15.00,
        "quantity": "120g",
        "price_unit": "Unit",
        "image_url": "https://assets.axfood.se/image/upload/f_auto,t_200/07311041071748_C1N1_s02"
    },
    {
        "name": "Chorizo",
        "price": 20.00,
        "quantity": "300g",
        "price_unit": "Unit",
        "image_url": "https://assets.axfood.se/image/upload/f_auto,t_500/07340083474316_C1N1_s01"
    },
    {
        "name": "Tortilla Original Medium",
        "price": 10.00,
        "quantity": "320g",
        "price_unit": "Unit",
        "image_url": "https://assets.axfood.se/image/upload/f_auto,t_200/07311041069790_C1N1_s01"
    },
    {
        "name": "Salmon Fillet C-trim",
        "price": 159.00,
        "quantity": "ca 1.5kg",
        "price_unit": "Kg",
        "image_url": "https://d2rfo6yapuixuu.cloudfront.net/hf7/ha1/8863282626590/02369332000002.jpg_master_axfood_300"
    },
    {
        "name": "Cheese Bread 4-pack",
        "price": 12.00,
        "quantity": "200g",
        "price_unit": "Unit",
        "image_url": "https://assets.axfood.se/image/upload/f_auto,t_200/07340083485497_C1N1_s01"
    },
    {
        "name": "Carrots Class 1",
        "price": 8.00,
        "quantity": "1kg",
        "price_unit": "Unit",
        "image_url": "https://assets.axfood.se/image/upload/f_auto,t_200/07311042001546_C1N1_s02"
    },
    {
        "name": "Coca-Cola Zero Soft Drink",
        "price": 29.95,
        "quantity": "6-pack 33cl",
        "price_unit": "Unit",
        "image_url": "https://assets.axfood.se/image/upload/f_auto,t_200/05449000259127_C1N1_s01"
    },
    {
        "name": "Chicken Fillet Sweden",
        "price": 99.00,
        "quantity": "ca 925g",
        "price_unit": "Kg",
        "image_url": "https://assets.axfood.se/image/upload/f_auto,t_200/02332804000008_C1N1_s04"
    },
    {
        "name": "Tomato Baby Plum Tomatoes",
        "price": 25.00,
        "quantity": "500g",
        "price_unit": "Unit",
        "image_url": "https://assets.axfood.se/image/upload/f_auto,t_200/07311042006459_C1N1_s01"
    },
    {
        "name": "Minced Beef Low Fat",
        "price": 59.95,
        "quantity": "500g",
        "price_unit": "Unit",
        "image_url": "https://assets.axfood.se/image/upload/f_auto,t_200/07340062412568_C1N1_s01"
    },
    {
        "name": "Pizza Dough",
        "price": 15.00,
        "quantity": "400g",
        "price_unit": "Unit",
        "image_url": "https://assets.axfood.se/image/upload/f_auto,t_200/07611612141109_C1N1_s01"
    },
    {
        "name": "Feta Traditional Taste",
        "price": 22.00,
        "quantity": "150g",
        "price_unit": "Unit",
        "image_url": "https://assets.axfood.se/image/upload/f_auto,t_200/07350002402658_C1N1_s03"
    },
    {
        "name": "Roast Beef Deli Slices",
        "price": 20.00,
        "quantity": "100g",
        "price_unit": "Unit",
        "image_url": "https://assets.axfood.se/image/upload/f_auto,t_200/07340083494789_C1N1_s02"
    },
    {
        "name": "Baby Dry 5 12-17kg",
        "price": 119.00,
        "quantity": "37-pack",
        "price_unit": "Unit",
        "image_url": "https://assets.axfood.se/image/upload/f_auto,t_200/08006540711873_C1N1_s01"
    }
]

# Conversion rate from SEK to USD (example rate, can vary)
sek_to_usd = 0.09

# Update prices in USD and keep the original price with the unit
for product in products_updated:
    price_sek = product["price"]
    price_usd = round(price_sek * sek_to_usd, 2)
    product["price"] = price_usd
