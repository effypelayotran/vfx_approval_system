from PIL import Image
import os

input_folder = '/Users/effypelayo/Downloads/new_guy_frames'
output_folder = '/Users/effypelayo/Downloads/vfx_approval_system/assets/edited'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Sort the files for consistent ordering
tif_files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith(('.tif', '.tiff'))])

# Loop through and convert
for index, filename in enumerate(tif_files, start=1):
    # Open image
    tif_path = os.path.join(input_folder, filename)
    img = Image.open(tif_path)

    # Convert to RGB
    img = img.convert('RGB')

    # New filename: frame1_original.jpg, frame2_original.jpg, etc.
    jpg_filename = f'frame{index}_edited.jpg'
    jpg_path = os.path.join(output_folder, jpg_filename)

    # Save image
    img.save(jpg_path, 'JPEG')
    print(f"Converted: {filename} → {jpg_filename}")
