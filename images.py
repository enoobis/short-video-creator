"""The code downloads a random landscape image from Unsplash based on a query
and saves it to the "images" folder"""

import requests
import os
from tkinter import filedialog
    
def download_image(query):
    url = 'https://api.unsplash.com/photos/random'
    params = {
        'query': query,
        'client_id': 'paste_your_access_key_here',
        'orientation': 'landscape'
    }
    response = requests.get(url, params=params)

    image_url = response.json()['urls']['regular']

    folder_path = os.path.join(os.getcwd(), "images")
    counter = len(os.listdir(folder_path)) + 1
    image_name = f'{counter}.jpg'
    image_path = os.path.join(folder_path, image_name)
    with open(image_path, 'wb') as f:
        response = requests.get(image_url)
        f.write(response.content)

    print(f'Successfully downloaded {image_name} to {folder_path}.')