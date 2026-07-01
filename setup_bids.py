import os
import json

# This assumes you run the script from inside your 001882 folder
bids_dir = "."

# 1. Generate the dataset_description.json file required to activate BIDS mode
bids_metadata = {
    "Name": "Role of Interphotoreceptor Matrix Proteoglycans in Retinal Homeostasis and Retinitis Pigmentosa",
    "BIDSVersion": "1.8.0",
    "DatasetType": "raw",
    "License": "CC0-1.0",
    "Authors": ["Yuan, Ming", "Salido, Ezequiel M."]
}

with open(os.path.join(bids_dir, "dataset_description.json"), "w") as f:
    json.dump(bids_metadata, f, indent=4)

# 2. Create the required folder hierarchy
bids_folders = [
    "sub-01/micr",    # For your microscopy OME-TIFF images
    "sourcedata",     # For your raw protocols and notes
    "derivatives"     # For your processed CSV/Excel analysis tables
]

for folder in bids_folders:
    os.makedirs(os.path.join(bids_dir, folder), exist_ok=True)

print("BIDS structure and dataset_description.json generated successfully!")