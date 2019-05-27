import os
import shutil

EXT_AUDIO = ['.wav', '.mp3', '.raw', '.wma']
EXT_VIDEO = ['.mp4', '.m4a', '.m4v', '.f4v', '.f4a', '.m4b', '.m4r', '.f4b', '.mov', '.avi', '.wmv', '.flv']
EXT_IMAGES = ['.jpeg', '.jpg', '.png', '.svg', '.gif', '.bmp']
EXT_DOCUMENTS = ['.txt', '.pdf', '.doc', '.docx', '.odt', '.html', '.csv']
EXT_COMPRESSED = ['.zip']
EXT_EXECUTABLE = ['.exe']

print('DOWNLOADS FOLDER CLEANUP\n')
print('Current directory: {}\n'.format(os.getcwd()))

current_folder = os.getcwd().split(os.sep)[-1]
if current_folder != 'Downloads':
    print('CLEANUP FAILED: Please execute the script in "Downloads" folder.\n')
else:
    files = os.listdir()

    # Create directories if they don't exist
    DIRS = ['Audio', 'Video', 'Images', 'Documents', 'Folders', 'Other', 'Compressed', 'Executable']
    if not os.path.isdir('./Audio'):
        for d in DIRS:
            os.mkdir('./{}'.format(d))

        print('Directories created successfuly.')

    # Run main script
    for f in files:
        name, extension = os.path.splitext(f)
        
        if os.path.isdir(f):
            if f not in DIRS:
                shutil.move(f, './Folders/{}'.format(f))
        elif extension in EXT_EXECUTABLE:
            shutil.move(f, './Executable/{}'.format(f))
        elif extension in EXT_DOCUMENTS:
            shutil.move(f, './Documents/{}'.format(f))
        elif extension in EXT_IMAGES:
            shutil.move(f, './Images/{}'.format(f))
        elif extension in EXT_AUDIO:
            shutil.move(f, './Audio/{}'.format(f))
        elif extension in EXT_VIDEO:
            shutil.move(f, './Video/{}'.format(f))
        elif extension in EXT_COMPRESSED:
            shutil.move(f, './Compressed/{}'.format(f))
        else:
            if f != os.path.basename(__file__):
                shutil.move(f, './Other/{}'.format(f))

    print('CLEANUP COMPLETED\n')

input('Press ENTER to close...')
