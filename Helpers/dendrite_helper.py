import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dendrite_key import DENDRITE_API_KEY
from dendrite_sdk import Dendrite

client = Dendrite(dendrite_api_key=DENDRITE_API_KEY)

def checkout(items):
    client.goto("https://www.hemkop.se")
    time.sleep(2)
    client.click("press 'avvisa alla' if it appears")
    for item in items:
#        client.fill_fields({"The search items bar": item[0]})
#        client.press(key="Enter")
        client.goto(f"https://www.hemkop.se/sok?q={item[0]}&sort=relevance")
        #client.goto(f"https://www.coop.se/handla/sok/?q={item[0]}")
        client.click(f"buy the product with the name {item[0]}")
        time.sleep(2)
        for i in range(item[1]-1):
            client.click("increase the amount of the product")
    print("---------------")
    client.press(key="Escape")
    print("Add to cart done")
    client.click("The cart icon to checkout")
    print("checkout page")
    client.click("Till kassan")

checkout([["lättmjölk", 2],["ägg", 1]])
