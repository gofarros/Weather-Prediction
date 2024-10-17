# Weather Prediction
---

##  Objectives

Praktek konsep Machine Learning sebagai berikut:

- Memahami konsep Machine Learning secara keseluruhan.
- Mempersiapkan data untuk digunakan dalam model Supervised Learning (Classification).
- Mengimplementasikan Supervised Learning (Classification) dengan data yang dipilih.
- Melakukan Hyperparameter Tuning dan Model Improvement.
- Melakukan Model Deployment.

## Dataset
Dataset diperoleh dari kaggle pada link berikut:
https://www.kaggle.com/datasets/nikhil7280/weather-type-classification

## Conceptual Problems
1. Latar belakang adanya bagging dan cara kerja bagging !
2. Perbedaan cara kerja algoritma Random Forest dengan algoritma boosting!
3. Apa yang dimaksud dengan Cross Validation !

## Outline
   1. Perkenalan
      > Identitas, gambaran besar dataset yang digunakan, dan *objective* yang ingin dicapai.
   
   2. Import Libraries
      > Berisi semua *library* yang digunakan dalam *project*.
   
   3. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. 
   
   4. Exploratory Data Analysis (EDA)
      > Bagian ini berisi explorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.
   
   5. Feature Engineering
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-test, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.   
   
   6. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

   7. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Melakukan beberapa kali proses training yang berbeda untuk melihat hasil yang didapatkan.
   
   8. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model.

   9. Model Saving
      > Pada bagian ini, dilakukan proses penyimpanan model dan file-file lain yang terkait dengan hasil proses pembuatan model. 
   
   10. Model Inference
       > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set ataupun test-set. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled.
   
   11. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, berisi kesimpulan yang mencerminkan hasil yang didapat dengan *objective* yang sudah ditulis di bagian pengenalan.