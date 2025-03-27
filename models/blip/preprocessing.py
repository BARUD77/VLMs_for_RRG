import pandas as pd
import os

# === CONFIG === (Replace with our own paths)
metadata_csv = r"C:\Users\Natnael\Desktop\mimic-cxr-2.0.0-metadata\mimic-cxr-2.0.0-metadata.csv"
output_csv = "graph_report.csv"

image_base = r"C:\Users\Natnael\Desktop\Chest Radiology\M_CXR\files"  # Base folder for .jpg images
report_base = r"C:\Users\Natnael\Desktop\mimic-cxr-reports\files"  # Base folder for .txt reports

# === LOAD METADATA ===
metadata = pd.read_csv(metadata_csv)

# Filter to only subject_ids starting with 10–13
metadata = metadata[metadata["subject_id"].astype(str).str.startswith(("10", '11', '12', '13','14','15','16'',17','18','19'))]

# Only keep PA or AP views
metadata = metadata[metadata["ViewPosition"].isin(["PA", "AP"])]

# Prefer PA if both PA and AP exist for the same study
metadata['is_PA'] = metadata['ViewPosition'] == 'PA'
metadata.sort_values(by=['study_id', 'is_PA'], ascending=[True, False], inplace=True)

# Keep only one image per study
metadata = metadata.drop_duplicates(subset="study_id", keep="first")

rows = []

for _, row in metadata.iterrows():
    subject_id = str(row["subject_id"]).zfill(8)
    study_id = str(row["study_id"])
    dicom_id = row["dicom_id"]
    study_folder = f"s{study_id}"

    # Construct paths
    jpg_path = os.path.join(image_base, f"p{subject_id[:2]}", f"p{subject_id}", study_folder, f"{dicom_id}.jpg")
    txt_path = os.path.join(report_base, f"p{subject_id[:2]}", f"p{subject_id}", f"{study_folder}.txt")

    if os.path.exists(jpg_path) and os.path.exists(txt_path):
        rows.append({
            "radiograph_path": jpg_path,
            "radio_report_path": txt_path,
        })

# Save CSV
pd.DataFrame(rows).to_csv(output_csv, index=False)
print(f"✅ CSV saved to {output_csv} with {len(rows)} samples.")