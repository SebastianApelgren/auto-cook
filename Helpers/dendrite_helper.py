from dendrite_key import DENDRITE_API_KEY
from dendrite_sdk import Dendrite

client = Dendrite(dendrite_api_key=DENDRITE_API_KEY)

def fetch_images(query):
    print("here")
    client.goto("https://www.google.com/search?q=" + query + "&tbm=isch")
    print("now here")
    image_url = client.extract("An image of the food " + query + ". Return a URL of the image.")
    print("done")
    return image_url

print(fetch_images("apple"))