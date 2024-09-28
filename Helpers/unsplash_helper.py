import requests
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unsplash_keys import ACCESS_KEY, SECRET_KEY

def get_unsplash_image_url(description):
    url = "https://api.unsplash.com/search/photos"
    headers = {
        "Accept-Version": "v1",
        "Authorization": f"Client-ID {ACCESS_KEY}"
    }
    params = {
        "query": description,
        "per_page": 1
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            image_url = data['results'][0]['urls']['regular']
            return image_url
        else:
            print("No images found for the given description.")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

# Usage
if __name__ == "__main__":
    description = "spaghetti aglio e olio"
    image_url = get_unsplash_image_url(description)
    if image_url:
        print(f"Image URL: {image_url}")