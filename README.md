# **Sistem Rekomendasi Buku Berdasarkan Deskripsi Konten Buku Menggunakan Metode TF-IDF dan Cosine Similarity**

### Saniya Rahma Pratiwi - A11.2022.14858 - Sistem Temu Kembali Informasi

---

## Dataset

Dataset yang digunakan diambil dari dataset publik kaggle → [![Kaggle Badge](https://img.shields.io/badge/Kaggle-blue?style=flat&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data)

Atribut yang terdapat pada dataset book :
- Serial No     : nomor urut buku
- Book          : nama buku
- Author        : penulis buku
- Description   : deskripsi buku
- Genres        : genre buku
- Avg_Ratings   : rating buku bernilai 1-5
- Num_Ratings   : jumlah peringkat buku
- URL           : url buku

Dataset tersebut memiliki 8 kolom secara keseluruhan. Pada sistem rekomendasi ini digunakan beberapa kolom, antara lain: Book, Author, Genres, dan Num_Ratings

---

## Permasalahan dan Tujuan Eksperimen

Sistem rekomendasi menjadi salah satu solusi yang dapat menyelesaikan masalah dalam pencarian buku yang sesuai dengan keinginan para pembaca dan menambah referensi pengetahuan terhadap buku lain yang serupa. Dengan menggunakan algoritma TF-IDF yang digunakan sebagai metode untuk pengukuran deskripsi suatu item tekstual dalam pendekatan Content Based Filtering. Selain itu, memanfaatkan cosine similarity sebagai sistem yang dapat mengukur kemiripan pada setiap buku dengan menggunakan perhitungan antar vector. Melalui sistem rekomendasi ini, pembaca buku diharapkan dapat menambah referensi baru berdasarkan buku-buku yang diminati sebelumnya.

---

## Metode dan Tahapan Eksperimen

- Data Collection :
  Pada tahapan ini melakukan pencarian dataset yang akan digunakan. Dataset yang di dapat berupa dataset Best Books (10k) Multi-Genre Data
- Preprocessing :
  Pada tahapan ini merupakan langkah awal yang dilakukan untuk mengubah data mentah menjadi informasi yang lebih bersih dan bisa diolah untuk proses selanjutnya. Hal yang dilakukan meliputi melakukan seleksi dataset dengan memilih atribut yang akan digunakan serta melakukan normalisasi pada kolom (menyeragamkan menjadi lower, tokenisasi).
- Metode :
  - SKLearn berfungsi sebagai alat untuk melaksanakan vektorisasi dengan metode Term Frequency-Inverse Document Frequency (TF-IDF).
  - Penggunaan SKLearn tidak hanya terbatas pada proses vektorisasi, tetapi juga dapat digunakan untuk menghitung kesamaan (cosine similarity) berdasarkan matriks TF-IDF yang dihasilkan dari vektorisasi tersebut.
  - Sebagai hasilnya, pengguna akan mendapatkan keluaran berupa lima judul buku yang memiliki kesamaan deskripsi dengan judul buku yang diinputkan.
  
---

## Performa Uji

Performa uji dilakukan melalui metode K-Fold Cross-Validation, di mana penulis sebelumnya membuat beberapa sampel rekomendasi berdasarkan judul buku tertentu untuk memperoleh hasil uji. Setelah melalui proses pengujian, diperoleh Average Hit Ratio sebesar 0.224 sebagai hasil performa uji.

---

## Deployment

Sistem Rekomendasi Buku dapat digunakan pada link → [![Streamlit Badge](https://img.shields.io/badge/Streamlit-red?style=flat&logo=streamlit&logoColor=white)](https://saniyarahma-book-recommendation-app-5h5zoq.streamlit.app/)
###### Selamat Mencoba 😊💙✨
