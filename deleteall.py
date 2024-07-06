import os
from shutil import rmtree

def delete_folders_content():
    base_path = os.getcwd() # Get current working directory
    folders = [ # List of folders to delete
        os.path.join(base_path, 'images'),
        os.path.join(base_path, 'text'),
        os.path.join(base_path, 'text-images'),
        os.path.join(base_path, 'video'),
        os.path.join(base_path, 'voices'),
        os.path.join(base_path, 'pre-done'),
        os.path.join(base_path, 'video-music')
    ]
    
    # Loop through each folder and delete its contents
    for folder in folders:
        for filename in os.listdir(folder): # Loop through each file in the folder
            file_path = os.path.join(folder, filename)
            try: # Try to delete the file
                if os.path.isfile(file_path) or os.path.islink(file_path): # Check if file is a file or a link
                    os.unlink(file_path)
                elif os.path.isdir(file_path): # Check if file is a directory
                    rmtree(file_path)
            except Exception as e: # Catch any exception that occurs
                print(f'Failed to delete {file_path}. Reason: {e}')