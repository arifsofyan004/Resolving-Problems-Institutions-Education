# Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut, sebuah institusi pendidikan yang telah beroperasi sejak tahun 2000, memiliki reputasi yang baik dalam mencetak lulusan berkualitas. Namun, institusi ini dihadapkan pada tantangan besar terkait tingginya tingkat siswa yang tidak menyelesaikan pendidikan atau dropout.

Tingginya tingkat dropout menjadi isu yang signifikan bagi Jaya Jaya Institut karena dapat berdampak negatif pada reputasi dan kualitas pendidikan institusi tersebut. Oleh karena itu, institusi ini memiliki kebutuhan mendesak untuk mengidentifikasi siswa yang berpotensi melakukan dropout sejak dini.

Dengan mendeteksi siswa-siswa potensial yang berisiko dropout, Jaya Jaya Institut berharap dapat memberikan intervensi atau bimbingan khusus yang dapat mencegah siswa untuk meninggalkan pendidikan mereka. Hal ini diharapkan dapat meningkatkan tingkat kelulusan dan memastikan kesuksesan siswa dalam menyelesaikan pendidikan mereka.

### Permasalahan Bisnis
- Menurunkan tingkat drop-out siswa dalam sistem pendidikan.
- Meningkatkan pemahaman terhadap faktor-faktor yang memengaruhi keputusan siswa untuk meninggalkan pendidikan.
- Mengidentifikasi pola-pola yang berkaitan dengan drop-out untuk pengambilan keputusan yang lebih efektif dalam manajemen pendidikan.

### Cakupan Proyek
- Analisis data untuk mengidentifikasi faktor-faktor yang berkorelasi dengan tingkat drop-out siswa.
- Visualisasi dan pemodelan data untuk pemahaman yang lebih baik tentang pola-pola drop-out.
- Pengembangan strategi atau rekomendasi berdasarkan hasil analisis untuk mengurangi tingkat drop-out.
- Pembuatan Dashboard di Tableau
- Melakukan deployment dengan membuat aplikasi prediksi drop-out di streamlit

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:
```
conda create --name DropoutPrediction python=3.9
conda activate DropoutPrediction
pip install streamlit==1.34.0 pandas==2.0.3 matplotlib==3.7.1 seaborn==0.13.1 numpy==1.25.2 scikit-learn==1.2.2 xgboost==2.0.3 joblib==1.4.2
```

## Business Dashboard
Dashboard ini dirancang untuk memberikan wawasan mendalam mengenai status dropout mahasiswa di Jaya Jaya Institut. Dashboard ini mencakup berbagai metrik dan visualisasi, termasuk total jumlah mahasiswa yang dropout, graduate, dan yang masih terdaftar. Juga ditampilkan jumlah dropout berdasarkan gender, persentase dropout berdasarkan status debitur, serta pekerjaan orang tua dari mahasiswa yang dropout. Selain itu, dashboard ini menyediakan analisis persentase dropout berdasarkan gender dan mode aplikasi, serta kinerja akademik semester pertama dan kedua dari mahasiswa yang dropout dalam mode aplikasi "Over 23 years old". Filter interaktif juga tersedia untuk memfilter data berdasarkan status debitur. Dengan memahami faktor-faktor yang berkontribusi terhadap dropout, Jaya Jaya Institut dapat mengambil langkah-langkah proaktif untuk memberikan bimbingan khusus kepada mahasiswa yang berisiko dropout, dengan tujuan mengurangi angka dropout dan meningkatkan tingkat kelulusan.

```
https://public.tableau.com/views/DashboardAnalisisDropoutJayaJayaInstitut/DropoutAnalyticsDashboard?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link
```

## Menjalankan Sistem Machine Learning

Untuk menjalankan prototipe sistem machine learning, ikuti langkah-langkah berikut untuk menganalisis data siswa dan memprediksi tingkat drop-out.

### Langkah-langkah:

1. **Download Dataset**
   - Pastikan Anda telah mengunduh dataset yang diperlukan. Anda dapat mengunduh dari link berikut:
     ```
     https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv
     ```

2. **Setup Environment**
   - Buat environment baru menggunakan Anaconda atau virtual environment. Berikut adalah contoh cara membuat environment baru menggunakan Anaconda:
     ```
     conda create --name DropoutPrediction python=3.9
     conda activate DropoutPrediction
     ```
   - Instal semua paket yang diperlukan dengan menggunakan pip:
     ```
     pip install streamlit==1.34.0 pandas==2.0.3 matplotlib==3.7.1 seaborn==0.13.1 numpy==1.25.2 scikit-learn==1.2.2 xgboost==2.0.3           joblib==1.4.2
     ```

3. **Jalankan Script**
   - Buka script yang telah diunduh menggunakan IDE atau editor kode seperti Jupyter Notebook, VSCode, atau PyCharm.
   - Pastikan dataset berada di lokasi yang benar dan sesuai dengan path yang ditentukan dalam script.
   - Jalankan script untuk memulai proses training model machine learning dan evaluasi hasilnya.

### Proses yang Dilakukan dalam Script:
- **Load Dataset**: Membaca dataset mahasiswa.
- **Preprocessing Data**: Melakukan pembersihan data dan preprocessing, encoding categorical variables, scaling dan Menggunakan Yeo-Johnson untuk transformasi data agar distribusi data menjadi lebih mendekati distribusi normal.
- **Model Training**: Melatih tiga model klasifikasi Regresi Logistik, SVM, dan Gradient Boosting, untuk menentukan algoritma terbaik.
Gradient Boosting memiliki akurasi tertinggi (0.83) dan metrik evaluasi yang lebih baik dibandingkan dengan Logistic Regression dan Support Vector Machine. Oleh karena itu, berdasarkan hasil ini, Gradient Boosting adalah pilihan terbaik di antara ketiga model yang diuji. Kemudian akan dilakukan tuning parameter lebih lanjut untuk meningkatkan kinerja model Gradient Boosting.
- **Model Evaluation**: Mengevaluasi model menggunakan metrik seperti confusion matrix dan classification report
- **Model Saving**: Menyimpan model yang terlatih menggunakan joblib untuk digunakan di masa mendatang.

### Mengakses Aplikasi Prediksi Dropout:
- Anda dapat mengakses Aplikasi Prediksi Dropout melalui link berikut:
```
https://aplikasi-prediksi-dropout.streamlit.app/
```

## Conclusion
Proyek ini memberikan wawasan yang berharga tentang faktor-faktor yang berkontribusi terhadap tingkat attrition di perusahaan. Analisis data menunjukkan bahwa variabel seperti usia, tingkat pendidikan, jenis kelamin, dan kepuasan kerja memiliki korelasi yang signifikan dengan attrition. Dari sini, dapat disimpulkan bahwa perusahaan perlu memperhatikan faktor-faktor ini dalam upaya untuk mengurangi tingkat attrition dan mempertahankan tenaga kerja yang berharga.

### Rekomendasi Action Items
- meninjau kembali kebijakan kompensasi untuk memastikan keseimbangan yang adil dan kompetitif
- evaluasi kepuasan kerja di tingkat entry-level 
- Meningkatkan program pengembangan karir untuk karyawan yang baru 
- meningkatkan program keseimbangan kerja-hidup yang fleksibel
- Pertimbangkan strategi untuk mengelola waktu dan tugas agar meminimalkan lembur yang berlebihan
- menyediakan lebih banyak kesempatan pengembangan karir untuk karyawan yang berstatus single.

## Run steamlit app
```
streamlit run prediksi_dropout_app.py
```
