import json
import os

def validate_labelme_jsons(folder_path):
    invalid_files = []
    total_files = 0

    print(f"Scanning folder: {folder_path}\n")

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            total_files += 1
            file_path = os.path.join(folder_path, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Check each shape in the JSON
                for i, shape in enumerate(data.get('shapes', [])):
                    points = shape.get('points', [])
                    shape_type = shape.get('shape_type', 'polygon')
                    
                    # Only polygons require 3+ points; points/lines differ
                    if shape_type == 'polygon' and len(points) < 3:
                        print(f"[INVALID] {filename}: Shape #{i} has only {len(points)} points.")
                        if filename not in invalid_files:
                            invalid_files.append(filename)
                            
            except Exception as e:
                print(f"[ERROR] Could not read {filename}: {e}")

    print(f"\nScan Complete.")
    print(f"Total JSONs checked: {total_files}")
    print(f"Total invalid files found: {len(invalid_files)}")
    return invalid_files

# Change this to your actual folder path
folder_to_check = r"C:\Users\tygsh\OneDrive\Desktop\KIE4002_FYP\Code\MC-UNet-main\datasets\before"
validate_labelme_jsons(folder_to_check)