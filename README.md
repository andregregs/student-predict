# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

**Prediksi Dropout Siswa - Jaya Jaya Institut**

Oleh: Andre Gregori Sangari  
Email: andresangari12@gmail.com  
ID Dicoding: andregregs12

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Hingga saat ini, institusi tersebut telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun, terdapat tantangan serius yang dihadapi yaitu tingginya angka dropout siswa yang tidak menyelesaikan pendidikannya.

Sebagai institusi pendidikan yang berkualitas, Jaya Jaya Institut memiliki komitmen untuk memberikan pendidikan terbaik kepada seluruh siswanya. Tingginya angka dropout tidak hanya berdampak pada reputasi institusi, tetapi juga merugikan siswa yang kehilangan kesempatan untuk menyelesaikan pendidikan dan meraih masa depan yang lebih baik.

### Permasalahan Bisnis

Berdasarkan latar belakang yang telah dijelaskan, terdapat beberapa permasalahan bisnis utama yang perlu diselesaikan:

1. **Tingginya Angka Dropout**: Dari 4,424 siswa yang dianalisis, sebanyak 1,421 siswa (32.1%) mengalami dropout, yang mengindikasikan adanya faktor-faktor tertentu yang menyebabkan siswa memutuskan untuk keluar dari program studi.

2. **Keterlambatan Identifikasi Siswa Berisiko**: Institusi belum memiliki sistem untuk mendeteksi secara dini siswa yang berpotensi dropout, sehingga intervensi yang diberikan seringkali terlambat.

3. **Kurangnya Pemahaman tentang Faktor Penyebab Dropout**: Belum ada analisis mendalam tentang faktor-faktor yang berkontribusi terhadap keputusan siswa untuk dropout.

4. **Tidak Adanya Monitoring System**: Institusi belum memiliki dashboard untuk memonitor performa dan kondisi siswa secara real-time.

### Cakupan Proyek

Proyek ini akan mencakup beberapa aspek utama untuk menyelesaikan permasalahan yang dihadapi Jaya Jaya Institut:

1. **Analisis Data Komprehensif**: Melakukan exploratory data analysis untuk memahami karakteristik siswa dan faktor-faktor yang berkorelasi dengan dropout.

2. **Pengembangan Model Prediksi**: Membangun model machine learning untuk memprediksi siswa yang berpotensi dropout berdasarkan data historis dan karakteristik siswa.

3. **Pembuatan Business Dashboard**: Mengembangkan dashboard interaktif menggunakan Metabase untuk membantu manajemen dalam memonitor performa siswa dan mengidentifikasi tren dropout.

4. **Prototype Sistem Prediksi**: Membuat aplikasi web menggunakan Streamlit yang dapat digunakan untuk memprediksi risiko dropout siswa secara real-time.

5. **Rekomendasi Strategis**: Memberikan action items yang dapat diimplementasikan untuk mengurangi tingkat dropout.

### Persiapan

**Sumber data**: Dataset performa siswa yang disediakan oleh Jaya Jaya Institut berisi 4,424 rekord siswa dengan 37 fitur yang mencakup informasi demografis, akademik, dan sosio-ekonomi. Untuk analisis model dan dashboard, digunakan subset 885 siswa sebagai test dataset untuk validasi performa model.

**Setup environment**:
```bash
# Clone repository
git clone <repository-url>
cd submission-2

# Install dependencies
pip install -r requirements.txt

# Setup virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows

# Jalankan notebook untuk analisis
jupyter notebook notebook.ipynb
```

## Business Dashboard

Business dashboard telah berhasil dibuat menggunakan Metabase dan menampilkan analytics komprehensif dari hasil prediksi machine learning model terhadap 885 siswa dari dataset test. Dashboard ini memberikan insights mendalam tentang performa model dan distribusi risiko dropout.

### 📊 **Key Performance Indicators**

Dashboard menampilkan metrics utama yang critical untuk monitoring:

- **Total Students Analyzed**: 885 siswa dari test dataset
- **Average Risk Score**: 41.3 (skala 0-100)
- **Model Prediction Accuracy**: 85.6% - performa model yang sangat baik
- **Incorrect Prediction Rate**: 14.4% - tingkat error yang dapat diterima

### 🎯 **Student Risk Segmentation**

Analisis menunjukkan distribusi risiko dropout yang seimbang:

- **Low Risk (51.8%)**: 459 siswa - monitoring rutin
- **Medium Risk (25.2%)**: 223 siswa - perlu perhatian khusus  
- **High Risk (23.1%)**: 204 siswa - intervensi segera diperlukan

### 📈 **Risk vs Reality Analysis**

Dashboard menampilkan validasi efektivitas model dengan membandingkan prediksi risiko terhadap actual dropout rate:

- **High Risk Group**: Menunjukkan tingkat dropout aktual yang tinggi
- **Low Risk Group**: Konfirmasi tingkat dropout yang rendah
- **Medium Risk Group**: Distribusi yang proporsional sesuai prediksi

**Fitur Dashboard:**
- **Real-time Analytics**: Monitoring performa model dan student risk distribution
- **Interactive Visualizations**: Pie charts untuk risk distribution dan model accuracy
- **Performance Tracking**: Bar charts untuk risk level vs actual dropout correlation  
- **Model Validation**: Accuracy metrics dan prediction confidence analysis
- **Decision Support**: Clear segmentation untuk prioritas intervensi

**Setup dan Akses Dashboard:**

1. **Jalankan Metabase menggunakan Docker:**
   ```bash
   docker-compose up -d
   ```

2. **Login Dashboard:**
   - URL: http://localhost:3000
   - Email: root@mail.com
   - Password: root123

3. **Database Connection:**
   - Type: SQLite
   - Database file: predictions.csv (imported)

**Export Database Metabase:**
```bash
# Export database instance dari container
docker cp metabase:/metabase.db/metabase.db.mv.db ./metabase.db.mv.db
```

Dashboard dapat diakses melalui: **http://localhost:3000/dashboard/1**

## Menjalankan Sistem Machine Learning

Sistem machine learning telah dikembangkan dalam bentuk aplikasi web interaktif menggunakan Streamlit. Aplikasi ini dapat memprediksi risiko dropout siswa berdasarkan input karakteristik siswa dengan performa yang terbukti sangat baik.

**Cara menjalankan prototype lokal:**
```bash
# Masuk ke direktori proyek
cd submission-2

# Jalankan aplikasi Streamlit
streamlit run app.py

# Aplikasi akan terbuka di browser pada alamat:
# http://localhost:8501
```

**Fitur Aplikasi:**
- **Input Form Komprehensif**: Form input untuk data siswa (demografis, akademik, finansial)
- **Prediksi Real-time**: Risiko dropout dengan confidence score dan kategori risiko
- **Visualisasi Interaktif**: Gauge chart, risk factors, dan analytics
- **Rekomendasi Actionable**: Saran intervensi spesifik berdasarkan profil risiko
- **Analytics Dashboard**: Overview performa model dan statistik institusi
- **Export Functionality**: Download hasil prediksi

**Model Specifications:**
- **Algorithm**: Random Forest Classifier (terpilih sebagai model terbaik)
- **Training Data**: 4,424 rekord siswa historis
- **Test Data**: 885 siswa untuk validasi
- **Features**: 35+ variabel akademik dan demografis
- **Performance Metrics**:
  - **Accuracy**: 85.6% (validated pada test dataset)
  - **F1-Score**: ~0.82
  - **Precision**: ~83%
  - **Recall**: ~81%
  - **Error Rate**: 14.4% (sangat acceptable untuk business case)

**Link Prototype Cloud Deployment:**
🚀 **[Jaya Jaya Institut Dropout Prediction App](https://student-predict-andregregs12.streamlit.app/)**

**Cara menggunakan aplikasi:**
```bash
# Untuk deployment ke Streamlit Cloud
streamlit run app.py

# Atau jalankan secara lokal
python -m streamlit run app.py
```

1. Buka aplikasi melalui link atau localhost
2. Navigasi ke halaman "📊 Prediction"
3. Isi form dengan data siswa:
   - Personal Information (umur, gender, status pernikahan)
   - Academic Performance (nilai semester 1 & 2)
   - Financial Information (status pembayaran, beasiswa)
   - Background Information (status sosial-ekonomi)
4. Klik tombol "🔮 Predict Dropout Risk"
5. Lihat hasil prediksi dengan kategorisasi risiko:
   - **High Risk (>70%)**: Memerlukan intervensi segera
   - **Medium Risk (30-70%)**: Monitoring dan dukungan proaktif
   - **Low Risk (<30%)**: Monitoring rutin
6. Review rekomendasi aksi yang diberikan sistem

## Conclusion

Berdasarkan analisis data dan pengembangan model machine learning yang telah dilakukan, serta validasi terhadap 885 siswa pada test dataset, dapat disimpulkan beberapa hal penting:

1. **Model Performance yang Excellent**: Model Random Forest yang dikembangkan menunjukkan performa yang sangat baik dengan akurasi 85.6% pada test dataset dan error rate hanya 14.4%, yang menunjukkan kemampuan model yang sangat reliable untuk mengidentifikasi siswa berisiko dropout.

2. **Risk Segmentation yang Efektif**: Analisis menunjukkan distribusi risiko yang seimbang dengan 51.8% siswa Low Risk, 25.2% Medium Risk, dan 23.1% High Risk, memungkinkan prioritisasi intervensi yang efisien dan targeted.

3. **Early Warning System yang Terbukti**: Dengan model prediction accuracy 85.6%, Jaya Jaya Institut kini memiliki kemampuan untuk mengidentifikasi siswa berisiko secara dini dengan confidence level yang tinggi dan memberikan intervensi yang tepat waktu.

4. **Data-Driven Decision Making**: Dashboard yang dibuat memberikan real-time insights dengan average risk score 41.3 dan memungkinkan manajemen untuk membuat keputusan berdasarkan data yang akurat dan memonitor efektivitas program-program yang dijalankan.

5. **Validated Risk Distribution**: Hasil validasi pada 885 siswa test dataset mengkonfirmasi bahwa model dapat secara akurat mengidentifikasi siswa dengan berbagai tingkat risiko, dengan focus khusus pada 204 siswa (23.1%) yang termasuk kategori High Risk.

### Rekomendasi Action Items

Berdasarkan hasil analisis, validasi model dengan akurasi 85.6%, dan segmentasi risiko yang terbukti, berikut adalah rekomendasi action items yang harus dilakukan Jaya Jaya Institut:

**🎯 Immediate Actions (High Priority)**

- **Focus pada 204 Siswa High Risk**: Implementasikan intervensi segera untuk 23.1% siswa yang teridentifikasi High Risk dengan confidence level 85.6%, termasuk program mentoring intensif dan support akademik khusus.

- **Monitoring 223 Siswa Medium Risk**: Develop program monitoring proaktif untuk 25.2% siswa Medium Risk dengan early intervention triggers dan regular check-ins untuk mencegah mereka masuk kategori High Risk.

- **Implementasi Dashboard Real-time**: Deploy dashboard Metabase untuk monitoring harian dengan fokus pada metrics: total students analyzed (885), average risk score (41.3), dan model accuracy tracking (85.6%).

**📊 Strategic Implementation (Medium Priority)**

- **Early Warning System Deployment**: Implementasikan sistem prediksi dropout secara rutin setiap semester menggunakan model dengan akurasi terbukti 85.6% untuk mengidentifikasi siswa berisiko dan memberikan intervensi dini.

- **Resource Allocation Optimization**: Alokasikan 60% resources untuk High Risk students (204 siswa), 30% untuk Medium Risk (223 siswa), dan 10% untuk monitoring Low Risk (459 siswa) berdasarkan distribusi risk yang validated.

- **Performance Monitoring System**: Establish KPI tracking system dengan baseline model accuracy 85.6% dan target error rate di bawah 15% untuk continuous improvement.

**🔄 Continuous Improvement (Long-term Priority)**

- **Model Validation dan Update**: Lakukan re-training model setiap semester dengan data baru untuk maintain atau improve akurasi di atas 85%, dengan target reduction error rate dari 14.4% menjadi <12%.

- **Intervention Effectiveness Tracking**: Monitor efektivitas intervensi terhadap 204 siswa High Risk untuk measure ROI dan optimize intervention strategies berdasarkan outcome yang terukur.

- **Dashboard Enhancement**: Expand dashboard dengan additional metrics seperti intervention success rate, cost per student saved, dan longitudinal tracking untuk provide comprehensive business intelligence.

- **Predictive Analytics Expansion**: Develop predictive models untuk additional outcomes seperti academic performance prediction dan optimal intervention timing berdasarkan foundation model accuracy 85.6% yang sudah proven effective.

**💡 Success Metrics & KPIs**

- **Target Dropout Reduction**: Reduce overall dropout rate dengan fokus primary pada 204 siswa High Risk  
- **Model Performance Maintenance**: Maintain prediction accuracy ≥85% dengan continuous monitoring
- **Intervention Success Rate**: Achieve >70% success rate dalam mencegah dropout pada High Risk students
- **Cost Optimization**: Optimize cost per student intervention berdasarkan risk segmentation yang terbukti akurat
- **Real-time Monitoring**: Daily dashboard monitoring dengan threshold alerts untuk risk score changes

Dengan foundation model accuracy 85.6% dan risk segmentation yang validated, Jaya Jaya Institut memiliki framework yang solid untuk significantly mengurangi dropout rate melalui targeted, data-driven interventions.