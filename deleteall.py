import os
from shutil import rmtree

def delete_folders_content():
    folders = ['C:\\Users\\enoobis\\Desktop\\video-project\\images',
               'C:\\Users\\enoobis\\Desktop\\video-project\\text',
               'C:\\Users\\enoobis\\Desktop\\video-project\\text-images',
               'C:\\Users\\enoobis\\Desktop\\video-project\\video',
               'C:\\Users\\enoobis\\Desktop\\video-project\\voices',
               'C:\\Users\\enoobis\\Desktop\\video-project\\pre-done',
               'C:\\Users\\enoobis\\Desktop\\video-project\\video-music']
    for folder in folders:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))