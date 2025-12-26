import json
import os

def check_dataset_health(folder_path, allowed_labels):
    print(f"Starting check in: {folder_path}")
    print(f"Allowed labels: {allowed_labels}\n")

    error_found = False
    total_jsons = 0

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            total_jsons += 1
            file_path = os.path.join(folder_path, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                shapes = data.get('shapes', [])
                if not shapes:
                    print(f"[WARNING] {filename}: No shapes found (empty image).")
                    continue

                for i, shape in enumerate(shapes):
                    label = shape.get('label')
                    points = shape.get('points', [])
                    
                    # 1. Check if the label is valid
                    if label not in allowed_labels:
                        print(f"[LABEL ERROR] {filename}: Shape #{i} has unknown label '{label}'")
                        error_found = True

                    # 2. Check if the polygon is valid (3+ points)
                    if len(points) < 3:
                        print(f"[POLYGON ERROR] {filename}: Shape #{i} ('{label}') only has {len(points)} points.")
                        error_found = True
                            
            except Exception as e:
                print(f"[FILE ERROR] {filename}: Could not read file. {e}")

    if not error_found:
        print(f"\nAll {total_jsons} files passed! Labels and polygons are correct.")
    else:
        print(f"\nScan complete. Please fix the errors listed above.")

# --- CONFIGURATION ---
# Change this path to your folder
dataset_folder = r"C:\Users\tygsh\OneDrive\Desktop\KIE4002_FYP\Code\MC-UNet-main\datasets\before"

# Add all labels you use in your JSONs here (e.g., "BS")
# Based on your file, "BS" is your target label
valid_labels = ["BS"] 

check_dataset_health(dataset_folder, valid_labels)