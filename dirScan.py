import os
import random
import string

def rename_pdf_files(root_folder, search_string, replacement_string):
    
    # Loop through items in the root folder
    for item in os.listdir(root_folder):
        item_path = os.path.join(root_folder, item)
        
        # If the item is a directory, recursively search it
        if os.path.isdir(item_path):
            rename_pdf_files(item_path, search_string, replacement_string)
        
        # If the item is a file with ".pdf" extension and contains the search string in its name
        elif item.lower().endswith(".pdf") and search_string in item:
            # Create the new filename by replacing the search string with the replacement string
            new_item = item.replace(search_string, replacement_string)
            new_item_path = os.path.join(root_folder, new_item)
            
            # Check if a file with the new name already exists
            counter = 1                                             # This will occur on subsequent runs if "old" files aren't moved or pruned.
            while os.path.exists(new_item_path):
                base, ext = os.path.splitext(new_item)
                new_item = f"{base}_OLD{counter}{ext}"              # Append "OLD" before the extension
                new_item_path = os.path.join(root_folder, new_item)
                counter += 1
            
            os.rename(item_path, new_item_path)
            print(f"Renamed: {item} -> {new_item}")

# Replace 'path_to_search' with the root path where you want to start the search
path_to_search = '/path/to/search'
search_string = "_OCR_221117"  # Specified search string
replacement_string = ""        # Specified replacement string

rename_pdf_files(path_to_search, search_string, replacement_string)
