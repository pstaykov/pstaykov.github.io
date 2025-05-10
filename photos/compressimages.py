from PIL import Image
import os

input_folder = 'D:\sites\pstaykov.github.io\photos\shootshi'
output_folder = 'D:\sites\pstaykov.github.io\photos\shoots'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Settings
resize_width = 1920
quality = 70  # JPEG quality (0–100)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f'compressed{filename}')
        
        with Image.open(input_path) as img:
            # Resize while maintaining aspect ratio
            w_percent = resize_width / float(img.size[0])
            h_size = int(float(img.size[1]) * w_percent)
            img = img.resize((resize_width, h_size), Image.LANCZOS)
            
            # Save compressed image
            img.save(output_path, 'JPEG', quality=quality, optimize=True)

        print(f'✅ Compressed: {filename}')
