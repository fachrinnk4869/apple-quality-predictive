# Laporan Proyek Machine Learning - Fachri Najm Noer Kartiman

## Domain Proyek

Analisis kualitas buah apel memainkan peran yang sangat penting dalam memastikan efisiensi dan keberhasilan rantai pasokan industri buah-buahan. Dengan pemahaman yang mendalam tentang karakteristik kualitas seperti tingkat kematangan, kekerasan, warna, dan kandungan gula, produsen dapat mengambil keputusan yang tepat terkait dengan waktu panen, penyimpanan, dan distribusi. Hal ini membantu mengurangi pemborosan dengan memungkinkan identifikasi dan pemisahan buah-buah yang tidak memenuhi standar kualitas, sehingga meminimalkan kerugian finansial dan memperpanjang umur simpan buah apel yang akan dikirim ke pasar. Selain itu, analisis kualitas juga memberikan manfaat bagi konsumen akhir dengan memastikan bahwa mereka menerima produk yang berkualitas tinggi, segar, dan memenuhi harapan mereka, yang pada gilirannya dapat meningkatkan kepuasan konsumen dan membangun loyalitas merek (Onwude, 2020).

Standarisasi kualitas buah apel juga penting dalam meningkatkan efisiensi dan daya saing industri buah-buahan secara keseluruhan. Dengan menetapkan standar kualitas yang konsisten dan terukur, industri dapat memfasilitasi perdagangan internasional dan memungkinkan produsen untuk bersaing di pasar global dengan lebih efektif. Selain itu, pemahaman yang lebih dalam tentang kualitas buah apel juga mendorong inovasi dalam teknik penanganan pasca panen, pengemasan, dan transportasi. Inovasi ini dapat menghasilkan produk-produk yang lebih inovatif dan efisien, yang pada gilirannya dapat memperkuat rantai pasokan secara keseluruhan dan meningkatkan kepuasan pelanggan serta kinerja industri secara keseluruhan (Bohdaniuk, 2019).

## Business Understanding

Implementasi wawasan yang dihasilkan dari analisis kualitas buah apel dalam industri buah-buahan memainkan peran penting dalam meningkatkan efisiensi dan kualitas produk secara keseluruhan. Pertama, dengan menyesuaikan praktik pertanian berdasarkan informasi yang diperoleh, produsen dapat meningkatkan hasil panen dengan memperhitungkan faktor-faktor yang memengaruhi kualitas buah apel seperti kondisi lingkungan dan teknik budidaya. Langkah ini dapat membantu meningkatkan konsistensi kualitas dan memastikan pasokan yang lebih stabil ke pasar.

Kedua, pengembangan teknik penanganan pasca panen yang didasarkan pada wawasan analisis kualitas buah apel dapat memperpanjang umur simpan buah, mengurangi kerugian selama penyimpanan dan distribusi, serta mempertahankan kualitas produk. Dengan menerapkan metode penyimpanan yang optimal dan teknologi pengawetan yang canggih, industri dapat memastikan bahwa buah apel tetap segar dan bermutu tinggi saat mencapai konsumen.

Terakhir, melalui pelatihan dan edukasi kepada para pemangku kepentingan industri, seperti petani, produsen, dan pedagang, tentang pentingnya kualitas buah apel dan praktik terbaik untuk meningkatkannya, industri dapat memperkuat kesadaran akan standar kualitas dan meningkatkan keberlanjutan rantai pasokan. Pembaruan standar industri juga dapat memastikan bahwa semua pelaku industri mengadopsi praktik terbaik yang diperlukan untuk menjaga kualitas buah apel selama seluruh proses produksi, distribusi, dan penjualan. Dengan demikian, implementasi wawasan analisis kualitas buah apel dapat memberikan kontribusi signifikan terhadap peningkatan efisiensi dan daya saing industri buah-buahan secara keseluruhan.

### Problem Statements

1. Bagaimana cara mengklasifikasikan kualitas buah apel berdasarkan atribut yang diberikan?
2. Apakah dimungkinkan untuk memprediksi kualitas buah apel dengan tingkat keakuratan yang tinggi?
3. Bagaimana faktor-faktor seperti ukuran, berat, manis, renyah, dan lainnya berkontribusi terhadap kualitas buah apel?

### Goals

1. Mengembangkan model klasifikasi yang dapat memprediksi kualitas buah apel dengan tingkat akurasi yang tinggi.
2. Menganalisis faktor-faktor yang memengaruhi kualitas buah apel.
3. Memberikan wawasan yang berguna bagi industri buah-buahan untuk meningkatkan efisiensi dan kualitas produk.

### Solution statements
- Menggunakan beberapa algoritma klasifikasi seperti *Random Forest*, *Support Vector Machine*, dan *k-Nearest Neighbors* untuk membandingkan kinerja dan memilih model terbaik.
- Melakukan penyetelan hyperparameter untuk meningkatkan performa model klasifikasi.

## Data Understanding

Dataset "apple quality" berisi informasi tentang berbagai atribut dari sejumlah buah, memberikan wawasan tentang karakteristiknya. Dataset ini mencakup detail seperti ID buah, ukuran, berat, tingkat kemanisan, kerenyahan, kelicinan, tingkat kematangan, keasaman, dan kualitas [Dataset](https://www.kaggle.com/datasets/nelgiriyewithana/apple-quality/data).


![image](https://github.com/fachrinnk4869/apple-quality-predictive/assets/92314386/13d54392-d5a1-4204-97b5-69dd6f3508f4)

Gambar 1. Univariative Analysis

Hasil univariative analysis menunjukkan bahwa semua fitur numerik memiliki penyebaran yang mirip dengan kurva lonceng atau bell curve. Kurva lonceng atau distribusi normal adalah distribusi yang simetris di sekitar nilai tengah, di mana sebagian besar data berkumpul di sekitar nilai tengah dan kemudian menyebar secara merata ke arah kedua ujung. Ini menunjukkan bahwa data cenderung terdistribusi normal, yang merupakan asumsi penting dalam beberapa teknik analisis statistik dan pembelajaran mesin.

![image](https://github.com/fachrinnk4869/apple-quality-predictive/assets/92314386/b26dee8d-87aa-46dd-a833-ccf6a2ab084a)

Gambar 2. Multivative Analysis

Hasil multivariative analysis menunjukkan bahwa setiap fitur yang berbeda dalam dataset tidak memiliki korelasi yang kuat satu sama lain. Korelasi maksimal yang teramati antara dua fitur adalah sebesar 0.25, sedangkan korelasi minimal adalah -0.26. Korelasi yang rendah ini menunjukkan bahwa tidak ada hubungan linear yang kuat antara dua fitur tertentu.

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

1. **Proporsi Pembagian Data**: Dalam kode di atas, data dibagi menjadi data pelatihan (train) dan data pengujian (test) dengan proporsi 90% untuk data pelatihan dan 10% untuk data pengujian. Hal ini dilakukan dengan menggunakan fungsi `train_test_split` dari library scikit-learn. Proporsi ini ditentukan oleh argumen `test_size=0.1` yang menunjukkan bahwa 10% dari total data akan dialokasikan sebagai data pengujian.

2. **Penanganan Outlier**: Outlier ditangani dengan menggunakan metode IQR (Interquartile Range). Pertama, kuartil pertama (Q1) dan kuartil ketiga (Q3) dari data dihitung. Selanjutnya, kisaran IQR dihitung sebagai selisih antara Q3 dan Q1. Data yang terletak di luar rentang (Q1 - 1.5 * IQR) dan (Q3 + 1.5 * IQR) dianggap sebagai outlier dan dihapus dari dataset menggunakan operasi slicing pada DataFrame. Ini dilakukan dengan menggunakan pernyataan `diamonds = diamonds[~((diamonds<(Q1-1.5*IQR))|(diamonds>(Q3+1.5*IQR))).any(axis=1)]`.

3. **Penanganan Missing Value**: Dalam kode yang diberikan, tidak ada langkah yang secara khusus menangani missing value. Namun, jika ada missing value dalam dataset, langkah-langkah seperti imputasi atau penghapusan baris/kolom dengan missing value dapat dilakukan sebelum proses pembagian data dan pemrosesan lebih lanjut.

4. **Library yang Digunakan**: Dalam proses ini, digunakan library scikit-learn untuk pembagian data dan pemrosesan skala fitur (train_test_split, StandardScaler), serta untuk menangani outlier (pada tahap tertentu). Library pandas juga digunakan untuk manipulasi data, seperti pembacaan data, penghapusan outlier, dan penanganan missing value.

## Modeling

Library scikit-learn digunakan untuk mengimplementasikan algoritma machine learning.

1. *K-Nearest Neighbors (KNN)*:
- Model KNN diinisialisasi tanpa menentukan nilai parameter tertentu. Dalam kasus ini, model menggunakan nilai defaultnya.
- Langkah selanjutnya adalah melatih model KNN menggunakan data pelatihan (X_train, y_train) dengan memanggil metode .fit().
- Setelah dilatih, model digunakan untuk membuat prediksi terhadap data pengujian (X_test) dengan memanggil metode .predict().
- Model KNN tidak menggunakan parameter yang disesuaikan dalam contoh ini, sehingga tidak ada parameter yang diatur secara eksplisit.

2. *Random Forest*:
- Model Random Forest diinisialisasi dengan menentukan nilai parameter n_estimators=200. Parameter ini mengatur jumlah pohon dalam ensemble.
- Setelah inisialisasi, model dilatih menggunakan data pelatihan yang sama seperti KNN.
- Setelah pelatihan selesai, model digunakan untuk memprediksi kelas target pada data pengujian.
- Dalam contoh ini, nilai parameter n_estimators diatur menjadi 200, dan random_state=123 digunakan untuk membuat hasil yang dapat direproduksi.

3. *AdaBoost (Adaptive Boosting)*:
- Model AdaBoost diinisialisasi dengan menentukan nilai parameter learning_rate=0.001 dan random_state=55.
- Setelah inisialisasi, model dilatih menggunakan data pelatihan yang sama.
- Kemudian, model digunakan untuk memprediksi kelas target pada data pengujian.
- Parameter learning_rate=0.001 digunakan untuk mengontrol kontribusi setiap model pelatihan terhadap keseluruhan prediksi, sedangkan random_state=55 digunakan untuk membuat hasil yang dapat direproduksi.

Hasil prediksi setiap model kemudian dievaluasi menggunakan metrik akurasi, confusion matrix, dan classification report.

## Evaluation

Metrik evaluasi yang digunakan adalah akurasi, presisi, recall, dan F1-score.

- Akurasi: Merupakan rasio prediksi yang benar secara keseluruhan terhadap total jumlah data. Akurasi mengukur seberapa baik model dalam melakukan prediksi secara keseluruhan.
- Presisi: Merupakan rasio antara jumlah kelas positif yang benar diprediksi oleh model dengan total jumlah prediksi positif yang dilakukan oleh model. Presisi mengukur seberapa akurat model dalam memprediksi kelas positif.
- Recall: Merupakan rasio antara jumlah kelas positif yang benar diprediksi oleh model dengan total jumlah data yang benar kelas positif. Recall mengukur seberapa baik model dalam menemukan semua contoh positif.
- F1-score: Merupakan rata-rata harmonis dari presisi dan recall. F1-score memberikan keseimbangan antara presisi dan recall, dan sering digunakan sebagai metrik evaluasi jika terdapat ketidakseimbangan antara kelas-kelas dalam data.

Dengan menggunakan metrik evaluasi ini, dievaluasi kinerja model secara holistik, mempertimbangkan trade-off antara presisi dan recall. Sebagai contoh, meskipun model memiliki akurasi tinggi, presisi dan recall yang rendah dapat menunjukkan bahwa model tidak cukup baik dalam mengidentifikasi kelas tertentu dengan benar.

Dalam proyek ini, model k-Nearest Neighbors (k-NN) memiliki performa terbaik dengan akurasi sebesar 90%. Ini menunjukkan bahwa model k-NN mampu memprediksi kelas dengan tingkat keberhasilan yang tinggi dibandingkan dengan model lainnya. Namun, untuk mendapatkan pemahaman yang lebih holistik, perlu juga mempertimbangkan presisi, recall, dan F1-score untuk memastikan bahwa model mampu melakukan prediksi dengan baik untuk semua kelas dan tidak hanya mengandalkan akurasi saja.

![image](https://github.com/fachrinnk4869/apple-quality-predictive/assets/92314386/f3eecbde-d891-454d-965b-353c7c3dc04d)

Gambar 3. Prediksi hasil *KNN Classifer*

![image](https://github.com/fachrinnk4869/apple-quality-predictive/assets/92314386/cecf3601-fa34-407b-b848-61dc54894a15)

Gambar 4. Prediksi hasil *Random Forest Classifer*

![image](https://github.com/fachrinnk4869/apple-quality-predictive/assets/92314386/9db6b6ec-1bcf-46a9-9d47-df6f8776ece6)

Gambar 5. Prediksi hasil *Adaboost Classifer*

![image](https://github.com/fachrinnk4869/apple-quality-predictive/assets/92314386/453a4905-cddc-42b3-9731-62270cf03e22)

Gambar 6. Perbandingan akurasi setiap model

## Daftar Pustaka

Onwude, D. I., Chen, G., Eke-Emezie, N., Kabutey, A., Khaled, A. Y., & Sturm, B. (2020). Recent advances in reducing food losses in the supply chain of fresh agricultural produce. Processes, 8(11), 1431.

Bohdaniuk, O., Buriak, R., & Savchuk, V. (2019). Competitiveness of horticultural products as a precondition of industry development. Entrepreneurship and Sustainability Issues, 6(4), 1587.

