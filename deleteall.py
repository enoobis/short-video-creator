"""the code deletes every thing """

import os
from shutil import rmtree

def delete_folders_content():
    base_path = os.getcwd() 
    folders = [
        os.path.join(base_path, 'images'),
        os.path.join(base_path, 'text'),
        os.path.join(base_path, 'text-images'),
        os.path.join(base_path, 'video'),
        os.path.join(base_path, 'voices'),
        os.path.join(base_path, 'pre-done'),
        os.path.join(base_path, 'video-music')
    ]
    
    for folder in folders:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try: 
                if os.path.isfile(file_path) or os.path.islink(file_path): 
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')