import pathlib

def main():
    cwd_path = pathlib.Path().cwd() / "ch12-file-input-and-output"
    images_path = cwd_path / "images"
    documents_path = cwd_path / "documents"

    # Create the new folder
    images_path.mkdir(exist_ok=True)

    # Define the extensions related to images
    image_types = ['.png', '.gif', '.jpg', '.jpeg']

    # Iterate over each 
    for path in documents_path.rglob('*'):
        if path.is_file():
            if path.suffix in image_types:
                path.replace(images_path / path.name)


if __name__ == '__main__':
    main()