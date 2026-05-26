import os, sys, shutil
from pathlib import Path


mapping_folders ={
        "documentos": ["Documentos", "Documents", "documents"],
        "imagens": ["Imagens", "Pictures", "Images", "images", "imagens"],
        "videos" : ["Videos", "Movies", "videos"],
        "downloads": ["Downloads", "Baixados", "downloads"],
        "desktop": ["Desktop", "Área de Trabalho", "desktop"]}


mapping_files = {
                "text" : [".pdf", ".txt", ".docx", ".doc", ".csv", ".xlsx", ".xls", ".odt", ".json"],
                "image" : [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".psd"],
                "video/audio" : [".mp4", ".mp3", ".mov", ".wav", ".avi", ".mkv"],
                "zipped" : [".zip", ".rar", ".7z", ".iso"],
                "exe" : [".exe", ".bat", ".dll", ".sys", ".html", ".css", ".js", ".java", ".py", ".ipynb"]}

def folders_finder(root: Path):

    folders = {}

    try:
        for key, folder_names in mapping_folders.items():

            for folder_name in folder_names:

                initial_path = root / folder_name

                if initial_path.exists() and initial_path.is_dir():

                    folders[key] = initial_path
                    break

        print("Completed")
        return folders

    except Exception as e:
        print(f"Error: {e}")
        return {}


def mover(root: Path):
    folders = folders_finder(root)

    try:
        for file in root.iterdir():

            # Ignore directories
            if not file.is_file():
                continue

            extension = file.suffix.lower()

            destination = None

            # Decide destination folder
            for category, extensions in mapping_files.items():

                if extension in extensions:

                    match category:
                        case "text":
                            destination = folders.get("documentos")

                        case "image":
                            destination = folders.get("imagens")

                        case "video/audio":
                            destination = folders.get("videos")

                        case "zipped":
                            destination = folders.get("documentos")

                        case _:
                            destination = folders.get("documentos")

                    break

            # Move file
            if destination:
                destination_file = destination / file.name

                shutil.move(str(file), str(destination_file))

                print(f"Moved: {file.name} -> {destination}")

        print("Files moved successfully.")

    except Exception as e:
        print(f"Error moving files: {e}")


if __name__ == "__main__":

    if getattr(sys, 'frozen', False) or '__file__' not in dir():
        base = Path.cwd()
    else:
        base = Path(__file__).parent

    mover(base)

    
        
        







