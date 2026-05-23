import os
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

    try : 
        for folder, folder_names in mapping_folders.items():
            
            for folder in folder_names:
                
                initial_path = root / folder
                
                if initial_path.exists() and initial_path.is_dir():
                    folders[folder] = initial_path
                    
                    break
        print(f"Completed")     
        return folders
    except Exception as e:
        return "Error, no folders found!", e

def mover(root: Path):
    folders = folders_finder(root)
    try:
        for extension in mapping_files:
            match extension:
                case "text":
                    destination = folders["documents"]

                case "image":
                    destination = folders["images"]
                
                case "video/audio":
                    destination = folders["videos"]
                
                case "zipped":
                    destination = folders["documents"]
                    
            for file in os.listdir(root):
                text_extensions = tuple(mapping_files[extension])
                
                if file.endswith(text_extensions):
                    origin_folder = os.path.join(root, file)
                    destination_folder = os.path.join(destination, file)
                    os.rename(origin_folder, destination_folder)

            print(f"Files moved")

    except Exception as e:
        return "Error", e


if __name__ == "main":
    mover(Path(__file__).parent)

    
        
        







