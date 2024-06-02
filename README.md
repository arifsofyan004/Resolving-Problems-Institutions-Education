# Menyelesaikan-Permasalahan-Human-Resources

## Business Understanding
Perusahaan Jaya Jaya Maju merupakan perusahaan multinasional yang beroperasi sejak 2000, memiliki lebih dari 1000 karyawan di seluruh negeri. Meskipun besar, perusahaan mengalami attrition rate yang tinggi (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%. Hal ini menunjukkan adanya masalah dalam retensi karyawan dan manajemen sumber daya manusia. Untuk menjaga pertumbuhan dan produktivitas, penting untuk memahami faktor-faktor yang memengaruhi kepuasan dan retensi karyawan.

### Permasalahan Bisnis
- Menurunkan tingkat turnover karyawan (attrition) dalam perusahaan.
- Meningkatkan pemahaman terhadap faktor-faktor yang memengaruhi keputusan karyawan untuk meninggalkan perusahaan.
- Mengidentifikasi pola-pola yang berkaitan dengan attrition untuk pengambilan keputusan yang lebih efektif dalam manajemen sumber daya manusia.

### Cakupan Proyek
- Analisis data untuk mengidentifikasi faktor-faktor yang berkorelasi dengan tingkat attrition.
- Visualisasi dan pemodelan data untuk pemahaman yang lebih baik tentang pola-pola attrition.
- Pengembangan strategi atau rekomendasi berdasarkan hasil analisis untuk mengurangi tingkat attrition.
- Pembuatan Dashboard di Power BI
- Melakukan deployment dengan membuat aplikasi prediksi attrition di streamlit

### Persiapan

Sumber data: [....](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:
```
conda create --name HumanResources python=3.9
conda activate HumanResources
pip install pandas matplotlib seaborn numpy scikit-learn xgboost plotly imbalanced-learn joblib
```

## Business Dashboard
Business dashboard yang telah dibuat memberikan gambaran lengkap tentang data karyawan perusahaan. Di dalamnya, terdapat informasi  seperti total jumlah karyawan, jumlah karyawan yang mengalami attrition, dan tingkat attrition secara keseluruhan. Selain itu, dashboard ini juga menampilkan jumlah karyawan yang aktif, jumlah karyawan dengan status "Unknown", serta berbagai plot yang menggambarkan hubungan attrition dengan berbagai faktor, seperti grup usia, jabatan, jarak tempuh, tahun bekerja, status pernikahan, lembur, dan jenis kelamin. Dengan demikian, dashboard ini memberikan pandangan menyeluruh yang dapat membantu manajemen dalam membuat keputusan strategis terkait pengelolaan sumber daya manusia perusahaan.

```
https://public.tableau.com/shared/CYH9HKZZD?:display_count=n&:origin=viz_share_link
```

## Menjalankan Sistem Machine Learning

Untuk menjalankan prototipe sistem machine learning yang telah dibuat, Anda dapat mengikuti langkah-langkah berikut. Langkah-langkah ini bertujuan untuk membantu departemen HR dalam menggunakan script tersebut untuk menganalisis data karyawan dan memprediksi tingkat attrition.

## Menjalankan Sistem Machine Learning

### Langkah-langkah:

1. **Download Script dan Dataset**
   - Pastikan Anda telah mengunduh script dan dataset yang diperlukan. Anda dapat mengunduh script machine learning dari link berikut:
   ```
   https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee
   ```

2. **Setup Environment**
   - Buat environment baru menggunakan Anaconda atau virtual environment. Berikut adalah contoh cara membuat environment baru menggunakan Anaconda:
     ```
     conda create --name HumanResources python=3.9
     conda activate HumanResources
     ```
   - Instal semua paket yang diperlukan dengan menggunakan pip:
     ```
     pip install pandas==2.0.3 matplotlib==3.7.1 seaborn==0.13.1 numpy==1.25.2 scipy==1.11.4 plotly==5.15.0 imbalanced-learn==0.10.1 scikit-learn==1.2.2 xgboost==2.0.3 joblib==1.4.2
     ```

3. **Jalankan Script**
   - Buka script yang telah diunduh menggunakan IDE atau editor kode seperti Jupyter Notebook, VSCode, atau PyCharm.
   - Pastikan dataset berada di lokasi yang benar dan sesuai dengan path yang ditentukan dalam script.
   - Jalankan script untuk memulai proses training model machine learning dan evaluasi hasilnya.

### Proses yang Dilakukan dalam Script:
- **Load Dataset**: Membaca dataset karyawan.
- **Preprocessing Data**: Melakukan pembersihan data dan preprocessing, termasuk handling missing values, encoding categorical variables, dan scaling.
- **Oversampling**: Menggunakan SMOTE untuk menangani ketidakseimbangan kelas.
- **Model Training**: Melatih model Logistic Regression dan XGBoost dengan hyperparameter tuning menggunakan GridSearchCV atau RandomizedSearchCV.
- **Model Evaluation**: Mengevaluasi model menggunakan metrik seperti confusion matrix, classification report, dan ROC-AUC score.
- **Model Saving**: Menyimpan model yang terlatih menggunakan joblib untuk digunakan di masa mendatang.

### Mengakses Aplikasi Prediksi Attrition:
- Anda dapat mengakses Aplikasi Prediksi Attrition melalui link berikut:
```
https://aplikasi-prediksi-attrition.streamlit.app/
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
streamlit run prediksi_attrition_app.py
```
