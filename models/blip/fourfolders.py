import zipfile
import os

# === USER INPUTS ===
zip_path = r"C:\Users\Natnael\Downloads\mimic-cxr-reports.zip"  # Path to the .zip file
output_dir = r"C:\Users\Natnael\Desktop\Chest Radiology\Reports"  # Destination directory
target_subfolders = ["files/p10", "files/p11", "files/p12", "files/p13"]  # Update here!

# ====================

def extract_selected(zip_path, output_dir, subfolders):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        files_to_extract = [f for f in zip_ref.namelist()
                            if any(f.startswith(folder) for folder in subfolders) and not f.endswith('/')]
        
        print(f"Found {len(files_to_extract)} files to extract from selected folders...")
        
        for f in files_to_extract:
            dest_path = os.path.join(output_dir, f)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
            with zip_ref.open(f) as source, open(dest_path, 'wb') as target:
                target.write(source.read())


        print("Extraction complete!")

if __name__ == "__main__":
    extract_selected(zip_path, output_dir, target_subfolders)