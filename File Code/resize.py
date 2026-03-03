import os
from PIL import Image

script_dir = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.abspath(os.path.join(script_dir, ".."))
output_base = os.path.join(base_path, "Dataset_224")

kelas_list = ["Kosong", "Terisi", "Penuh"]
target_size = 224

os.makedirs(output_base, exist_ok=True)

for kelas in kelas_list:
    input_folder = os.path.join(base_path, kelas)
    output_folder = os.path.join(output_base, kelas)
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)

            with Image.open(input_path) as img:
                img = img.convert("RGB")
                img = img.resize((target_size, target_size), Image.LANCZOS)
                img.save(output_path, quality=95)

print("Resize selesai.")