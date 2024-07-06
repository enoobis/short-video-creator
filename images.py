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
    folder_path = os.path.join(os.getcwd(), "images")
    counter = len(os.listdir(folder_path)) + 1  # Get number of existing files and add 1
    image_name = f'{counter}.jpg' # Create image name
    image_path = os.path.join(folder_path, image_name) # Create image path
    with open(image_path, 'wb') as f: # Open the file in write binary mode
        response = requests.get(image_url) # Send request to image URL
        f.write(response.content) # Write image content to file

    print(f'Successfully downloaded {image_name} to {folder_path}.') # Print success message