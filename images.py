import requests
import os
from tkinter import filedialog
    
def download_image(query):
    # Define API endpoint and parameters
    url = 'https://api.unsplash.com/photos/random'
    params = {
        'query': query,
        'client_id': 'token_unsplash',
        'orientation': 'landscape'
    }

    # Send API request
    response = requests.get(url, params=params)

    # Get image URL from API response
    image_url = response.json()['urls']['regular']

    # Download image and save to folder
    folder_path = r'C:\Users\enoobis\Desktop\video-project\images'
    counter = len(os.listdir(folder_path)) + 1  # Get number of existing files and add 1
    image_name = f'{counter}.jpg'
    image_path = os.path.join(folder_path, image_name)
    with open(image_path, 'wb') as f:
        response = requests.get(image_url)
        f.write(response.content)

    print(f'Successfully downloaded {image_name} to {folder_path}.')