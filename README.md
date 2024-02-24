# Laporan Proyek Machine Learning - Fachri Najm Noer Kartiman

## Domain Proyek

Buah apel merupakan salah satu buah yang sangat populer dan dikonsumsi secara luas di seluruh dunia. Dalam industri buah-buahan, penting untuk memahami kualitas buah apel untuk pengemasan, distribusi, dan penjualan yang optimal. Oleh karena itu, analisis kualitas buah apel dapat memberikan wawasan berharga bagi para produsen, pedagang, dan konsumen.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Masalah ini perlu diselesaikan karena pengetahuan tentang kualitas buah apel dapat meningkatkan efisiensi dalam rantai pasokan buah-buahan.
- Referensi: [Feature based Fruit Quality Grading System using Support Vector Machine](https://ieeexplore.ieee.org/document/9012384)

## Business Understanding

Dalam bagian ini, kita akan mengklarifikasi masalah yang akan diselesaikan.

### Problem Statements

1. Bagaimana cara mengklasifikasikan kualitas buah apel berdasarkan atribut yang diberikan?
2. Apakah dimungkinkan untuk memprediksi kualitas buah apel dengan tingkat keakuratan yang tinggi?
3. Bagaimana faktor-faktor seperti ukuran, berat, manis, renyah, dan lainnya berkontribusi terhadap kualitas buah apel?

### Goals

1. Mengembangkan model klasifikasi yang dapat memprediksi kualitas buah apel dengan tingkat akurasi yang tinggi.
2. Menganalisis faktor-faktor yang memengaruhi kualitas buah apel.
3. Memberikan wawasan yang berguna bagi industri buah-buahan untuk meningkatkan efisiensi dan kualitas produk.

### Solution statements
- Menggunakan beberapa algoritma klasifikasi seperti Random Forest, Support Vector Machine, dan k-Nearest Neighbors untuk membandingkan kinerja dan memilih model terbaik.
- Melakukan penyetelan hyperparameter untuk meningkatkan performa model klasifikasi.

## Data Understanding

Dataset "apple quality" berisi informasi tentang berbagai atribut dari sejumlah buah, memberikan wawasan tentang karakteristiknya. Dataset ini mencakup detail seperti ID buah, ukuran, berat, tingkat kemanisan, kerenyahan, kelicinan, tingkat kematangan, keasaman, dan kualitas [Dataset](https://www.kaggle.com/datasets/nelgiriyewithana/apple-quality/data).

### Variabel-variabel pada dataset "apple quality" adalah sebagai berikut:
- ID: Nomor identifikasi unik untuk setiap buah
- Size: Ukuran buah dalam satuan tertentu
- Weight: Berat buah dalam satuan tertentu
- Sweetness: Tingkat kemanisan buah
- Crunchiness: Tingkat kerenyahan buah
- Juiciness: Tingkat kelicinan buah
- Ripeness: Tingkat kematangan buah
- Acidity: Tingkat keasaman buah
- Quality: Kualitas buah (Good, bad)

## Data Preparation

Proses persiapan data meliputi pembersihan data, penanganan nilai yang hilang, normalisasi atribut, dan pembagian dataset menjadi set pelatihan dan pengujian.

## Modeling

Dalam tahap pemodelan, kita akan menggunakan algoritma klasifikasi seperti Random Forest, dan k-Nearest Neighbors (k-NN) untuk membangun model kualitas buah apel. Selanjutnya, kita akan melakukan penyetelan hyperparameter untuk meningkatkan performa model yang dipilih.

## Evaluation

Metrik evaluasi yang akan digunakan adalah akurasi, presisi, recall, dan F1-score. Hasil proyek ini model k-Nearest Neighbors (k-NN) memiliki performa terbaik dari 2 model lainnya sebesar 90%

<!-- **---Ini adalah bagian akhir laporan---** -->
