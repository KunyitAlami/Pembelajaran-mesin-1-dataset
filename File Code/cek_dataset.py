import os
from collections import Counter

script_dir = os.path.dirname(os.path.abspath(__file__))

base_path = os.path.abspath(os.path.join(script_dir, ".."))

kelas_list = ["Kosong", "Terisi", "Penuh"]

print("\nSTATISTIK DATASET COLOKAN\n")
print("Base path yang dibaca:", base_path, "\n")

for kelas in kelas_list:
    folder_path = os.path.join(base_path, kelas)

    if not os.path.exists(folder_path):
        print(f"Folder {kelas} tidak ditemukan!")
        continue

    files = os.listdir(folder_path)
    image_files = [f for f in files if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    ekstensi = [os.path.splitext(f)[1].lower() for f in image_files]
    counter_ext = Counter(ekstensi)

    print(f"Kelas: {kelas}")
    print(f"Jumlah gambar: {len(image_files)}")
    print(f"Tipe file: {dict(counter_ext)}")
    print("-" * 40)

print("Selesai.")