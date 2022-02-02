import pathlib
import shutil

# Move the file image1.png to a new directory images/ inside my_folder
path = pathlib.Path().cwd() / 'ch12-file-input-and-output' / 'my_folder'
source = path / 'image1.png'
destination = path / 'images' / source.name

if not destination.parent.exists():
    destination.parent.mkdir()

source.replace(destination)


# Delete the file1.txt
file_to_delete = path / 'file1.txt'
if file_to_delete.exists():
    file_to_delete.unlink()

# Delete the my_folder/ directory
folder_to_delete = path
shutil.rmtree(folder_to_delete)
