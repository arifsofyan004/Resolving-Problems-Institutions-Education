# Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut, sebuah institusi pendidikan yang telah beroperasi sejak tahun 2000, memiliki reputasi yang baik dalam mencetak lulusan berkualitas. Namun, institusi ini dihadapkan pada tantangan besar terkait tingginya tingkat siswa yang tidak menyelesaikan pendidikan atau dropout.

Tingginya tingkat dropout menjadi isu yang signifikan bagi Jaya Jaya Institut karena dapat berdampak negatif pada reputasi dan kualitas pendidikan institusi tersebut. Oleh karena itu, institusi ini memiliki kebutuhan mendesak untuk mengidentifikasi siswa yang berpotensi melakukan dropout sejak dini.

Dengan mendeteksi siswa-siswa potensial yang berisiko dropout, Jaya Jaya Institut berharap dapat memberikan intervensi atau bimbingan khusus yang dapat mencegah siswa untuk meninggalkan pendidikan mereka. Hal ini diharapkan dapat meningkatkan tingkat kelulusan dan memastikan kesuksesan siswa dalam menyelesaikan pendidikan mereka.

### Permasalahan Bisnis
- **Tingkat Drop-Out yang Tinggi**: Jaya Jaya Institusi mengalami masalah dengan banyaknya siswa yang meninggalkan sekolah sebelum menyelesaikan pendidikan mereka.
- **Kehilangan Potensi**: Setiap siswa yang drop-out mengakibatkan hilangnya potensi tenaga kerja yang berkualitas dan berdampak negatif pada masa depan siswa tersebut.
- **Dampak Finansial**: Tingginya angka drop-out mengurangi pendapatan dan dukungan finansial bagi institusi pendidikan.
- **Pentingnya Pemahaman Penyebab**: Tanpa memahami faktor-faktor penyebab drop-out, sulit bagi institusi untuk mengembangkan solusi efektif.
- **Efek Jangka Panjang**: Masalah drop-out yang tidak teratasi dapat menurunkan tingkat kelulusan, mengurangi jumlah pendaftar, dan merusak reputasi institusi.

### Cakupan Proyek
- Analisis data untuk mengidentifikasi faktor-faktor yang berkorelasi dengan tingkat drop-out siswa.
- Visualisasi dan pemodelan data untuk pemahaman yang lebih baik tentang pola-pola drop-out.
- Pengembangan strategi atau rekomendasi berdasarkan hasil analisis untuk mengurangi tingkat drop-out.
- Pembuatan Dashboard di Tableau
- Pembuatan Model Machine learning
- Melakukan deployment model ML dengan membuat aplikasi prediksi drop-out di streamlit

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:
```
conda create --name DropoutPrediction python=3.9
conda activate DropoutPrediction
pip install -r requirements.txt
```

## Business Dashboard
Dashboard ini dirancang untuk memberikan wawasan mendalam mengenai status dropout mahasiswa di Jaya Jaya Institut. Dashboard ini mencakup berbagai metrik dan visualisasi, termasuk total jumlah mahasiswa yang dropout, graduate, dan yang masih terdaftar. Juga ditampilkan jumlah dropout berdasarkan gender, persentase dropout berdasarkan status debitur, serta pekerjaan orang tua dari mahasiswa yang dropout. Selain itu, dashboard ini menyediakan analisis persentase dropout berdasarkan gender dan mode aplikasi, serta kinerja akademik semester pertama dan kedua dari mahasiswa yang dropout dalam mode aplikasi "Over 23 years old". Filter interaktif juga tersedia untuk memfilter data berdasarkan status debitur. Dengan memahami faktor-faktor yang berkontribusi terhadap dropout, Jaya Jaya Institut dapat mengambil langkah-langkah proaktif untuk memberikan bimbingan khusus kepada mahasiswa yang berisiko dropout, dengan tujuan mengurangi angka dropout dan meningkatkan tingkat kelulusan.

```
https://public.tableau.com/views/DashboardAnalisisDropoutJayaJayaInstitut/DropoutAnalyticsDashboard?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link
```

## Menjalankan Sistem Machine Learning

Untuk menjalankan prototipe sistem machine learning, ikuti langkah-langkah berikut untuk menganalisis data siswa dan memprediksi tingkat drop-out.

### Langkah-langkah:

1. **Download Script**
   - Pastikan Anda telah mengunduh script dan dataset yang diperlukan. Anda dapat mengunduh script machine learning dari link berikut:
     ```
      https://github.com/arifsofyan004/Menyelesaikan-Permasalahan-Institusi-Pendidikan/blob/main/submission_akhir_menyelesaikan_permasalahan_institusi_pendidikan.py
     ```

2. **Setup Environment**
   - Buat environment baru menggunakan Anaconda atau virtual environment. Berikut adalah contoh cara membuat environment baru menggunakan Anaconda:
     ```
     conda create --name DropoutPrediction python=3.9
     conda activate DropoutPrediction
     ```
   - Instal semua paket yang diperlukan dengan menggunakan pip:
     ```
     pip install -r requirements.txt
     ```

3. **Jalankan Script**
   - Buka script yang telah diunduh menggunakan IDE atau editor kode seperti Jupyter Notebook, VSCode, atau PyCharm.
   - Pastikan dataset berada di lokasi yang benar dan sesuai dengan path yang ditentukan dalam script.
   - Jalankan script untuk memulai proses training model machine learning dan evaluasi hasilnya.

### Proses yang Dilakukan dalam Script:
- **Load Dataset**: Membaca dataset mahasiswa.
- **Preprocessing Data**: Melakukan pembersihan data dan preprocessing, encoding categorical variables, scaling dan Menggunakan Yeo-Johnson untuk transformasi data agar distribusi data menjadi lebih mendekati distribusi normal.
- **Model Training**: Melatih tiga model klasifikasi Regresi Logistik, SVM, dan Gradient Boosting, untuk menentukan algoritma terbaik.
Gradient Boosting memiliki akurasi tertinggi (0.83) dan metrik evaluasi yang lebih baik dibandingkan dengan Logistic Regression dan Support Vector Machine. Oleh karena itu, Gradient Boosting adalah pilihan terbaik di antara ketiga model yang diuji dalam dataset ini. Kemudian akan dilakukan tuning parameter lebih lanjut untuk meningkatkan kinerja model Gradient Boosting.
- **Model Evaluation**: Mengevaluasi model menggunakan metrik seperti confusion matrix dan classification report
- **Model Saving**: Menyimpan model yang terlatih menggunakan joblib untuk digunakan di aplikasi prediksi dropout yang akan di buat di streamlit.

### Mengakses Aplikasi Prediksi Dropout:
- Anda dapat mengakses Aplikasi Prediksi Dropout melalui link berikut:
```
https://aplikasi-prediksi-dropout.streamlit.app/
```

## Conclusion
Dari hasil analisis EDA, ditemukan bahwa terdapat korelasi yang signifikan antara beberapa fitur dengan status dropout mahasiswa. Fitur-fitur seperti usia saat pendaftaran, status debitur, gender, dan mode aplikasi memiliki korelasi tinggi dengan tingkat dropout. Analisis menunjukkan bahwa tingkat dropout cenderung meningkat pada kelompok usia 21-30 tahun, mahasiswa yang memiliki utang, mahasiswa laki-laki, dan mereka yang mendaftar dengan mode aplikasi "Over 23 years old". Selain itu, faktor ekonomi dan kinerja akademik juga mempengaruhi tingkat dropout.

### Rekomendasi Action Items
Berdasarkan temuan ini, institusi dapat mengambil beberapa tindakan untuk mengurangi tingkat dropout. Pertama, mereka dapat memperkenalkan program-program fleksibel seperti smart learning atau pembelajaran daring untuk menyesuaikan dengan jadwal kerja mahasiswa, terutama bagi mereka yang berusia 21-30 tahun. Kedua, institusi dapat menyediakan bantuan keuangan tambahan seperti beasiswa atau keringanan biaya kuliah bagi mahasiswa dengan latar belakang ekonomi yang kurang stabil bisa di lihat dari pekerjaan orang tua nya contoh nya unskiled workers dan yang merupakan debitur. Selain itu, institusi dapat mengembangkan sistem peringatan dini yang terotomatisasi atau melakukan pemantauan progres akademik secara teratur untuk mengidentifikasi mahasiswa yang memiliki nilai yang kurang baik (di bawah 10) yang berisiko dropout Sehingga bisa memberikan dukungan tambahan sesuai kebutuhan. Dengan memprioritaskan tindakan-tindakan ini, diharapkan dapat meningkatkan tingkat retensi dan kesuksesan akademik mahasiswa secara keseluruhan.

## Run steamlit app
```
streamlit run prediksi_dropout_app.py
```
