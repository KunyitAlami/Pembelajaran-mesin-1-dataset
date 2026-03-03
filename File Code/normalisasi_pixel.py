import os
import numpy as np
from PIL import Image

script_dir = os.path.dirname(os.path.abspath(__file__))
base_path = r"D:\GHANI\Semester 6\Mata Kuliah\Pembelajaran Mesin 1\Tugas Dataset\Dataset Colokan\Dataset Ghani\Roboflow\Augmented"
output_base = os.path.join(os.path.dirname(base_path), "Augmented_Normalized")

splits = ["train", "valid", "test"]

os.makedirs(output_base, exist_ok=True)

for split in splits:
    split_path = os.path.join(base_path, split)
    output_split_path = os.path.join(output_base, split)
    os.makedirs(output_split_path, exist_ok=True)

    for root, dirs, files in os.walk(split_path):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                input_path = os.path.join(root, file)

                class_name = os.path.basename(root)
                class_output_path = os.path.join(output_split_path, class_name)
                os.makedirs(class_output_path, exist_ok=True)

                output_path = os.path.join(
                    class_output_path, file.replace(".jpg", ".npy")
                )

                with Image.open(input_path) as img:
                    img = img.convert("RGB")
                    img_array = np.array(img, dtype=np.float32)
                    img_array = img_array / 255.0
                    np.save(output_path, img_array)

print("Normalisasi selesai untuk train, valid, dan test.")