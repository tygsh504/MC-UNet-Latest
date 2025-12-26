import os
import numpy as np
from PIL import Image
from tqdm import tqdm

mask_folder = r"C:\Users\tygsh\OneDrive\Desktop\KIE4002_FYP\Code\MC-UNet-main\datasets\SegmentationClass"
all_unique_values = set()

print("Scanning all masks for unique pixel values...")
for mask_name in tqdm(os.listdir(mask_folder)):
    if mask_name.endswith(".png"):
        path = os.path.join(mask_folder, mask_name)
        img = np.array(Image.open(path))
        unique_in_file = np.unique(img)
        all_unique_values.update(unique_in_file)

print("-" * 30)
print(f"All unique values found in dataset: {sorted(list(all_unique_values))}")
print(f"Your num_classes is 13, so values should be between 0 and 12.")
if 255 in all_unique_values:
    print("WARNING: Value 255 detected! This will cause training issues.")