# Dataset Klasifikasi Kondisi Stop Kontak

## 📌 Deskripsi Dataset

Dataset ini berisi kumpulan gambar stop kontak (colokan listrik) yang digunakan untuk tugas klasifikasi citra (image classification). Dataset dibuat secara mandiri dengan memperhatikan variasi sudut pengambilan, jarak, pencahayaan, dan latar belakang.

Dataset terdiri dari 3 kelas berdasarkan kondisi keterisian stop kontak:

- **Kosong** → Tidak ada steker terpasang
- **Terisi** → Sebagian lubang terpakai
- **Penuh** → Seluruh lubang terisi steker

Dataset ini dirancang untuk mendukung eksperimen computer vision dalam mendeteksi kondisi penggunaan stop kontak secara otomatis.

---

## 🎯 Tujuan Dataset

Dataset ini dibuat untuk:

- Melatih model klasifikasi gambar berbasis machine learning / deep learning
- Mendeteksi tingkat keterisian stop kontak secara otomatis
- Mendukung pengembangan sistem monitoring penggunaan listrik
- Studi awal penerapan AI dalam konsep smart home / smart environment

---

## 📊 Jumlah dan Distribusi Data

Dataset dibuat seimbang untuk menghindari bias model.

| Kelas  | Jumlah Gambar |
| ------ | ------------- |
| Kosong | 151           |
| Terisi | 151           |
| Penuh  | 151           |

**Total Dataset: 453 gambar**

---

## 📷 Proses Pengambilan Data

- **Perangkat:** Kamera smartphone
- **Lokasi:** Dalam ruangan (rumah/kamar)
- **Waktu:** Siang dan malam
- **Resolusi:** Konsisten dan tidak blur berlebihan

Pengambilan dilakukan secara manual dengan memperhatikan standar kualitas citra.

---

## 🔄 Standar Pengambilan Gambar

Dataset dikumpulkan dengan variasi berikut:

### 1️⃣ Sudut Pengambilan (Angle)

- Depan
- Samping kiri
- Samping kanan
- Dari atas
- Dari bawah

### 2️⃣ Rotasi & Orientasi

- Variasi posisi objek
- Tidak semua gambar dalam orientasi yang sama

### 3️⃣ Jarak & Skala

- Jarak dekat (close-up)
- Jarak sedang (background terlihat)

### 4️⃣ Pencahayaan

- Terang (siang hari)
- Redup (malam / indoor)

### 5️⃣ Background

- Polos
- Non-polos (keramik, tembok bermotif, area sekitar kabel)

---

## 🧪 Augmentasi Data

Augmentasi tidak digunakan dalam dataset ini karena jumlah data asli sudah mencukupi (lebih dari 100 gambar).

Seluruh gambar merupakan hasil pengambilan langsung.

---

## ⚠️ Catatan

- Gambar tidak mengandung watermark
- Tidak menggunakan filter ekstrem
- Tidak mengandung kolase
- Objek tetap terlihat jelas pada setiap gambar

---

## 👤 Pembuat Dataset

Nama: Ghani Mudzakir  
Program Studi: Teknik Informatika  
Semester: 6

---

## 📌 Kesimpulan

Dataset ini terdiri dari 378 gambar dengan distribusi seimbang pada 3 kelas. Dataset telah memenuhi standar variasi sudut, jarak, pencahayaan, dan latar belakang sehingga layak digunakan untuk eksperimen klasifikasi citra berbasis computer vision.
