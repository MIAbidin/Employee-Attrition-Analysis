#  Employee Attrition Analysis

Repository ini berisi proyek **Analisis & Prediksi Attrition (Turnover) Karyawan** menggunakan data HR dengan pendekatan **Machine Learning** dan **Dashboard Visualisasi**.

---

## Project Overview
- **Total Employees**: 1,470  
- **Data Bersih**: 1,058 (setelah menghapus missing values pada kolom `Attrition`)  
- **Jumlah Fitur Awal**: 35 kolom (demografi, pekerjaan, kepuasan, dll.)  
- **Jumlah Fitur Setelah Encoding**: 44 kolom  
- **Train/Test Split**: 80/20 (846 train, 212 test)  

**Attrition Rate (Turnover):**  
- Total attrition: **16.9%** (179 dari 1.058 karyawan)  
- Normal untuk industri, namun ada area kritis seperti **Overtime** & **Sales Department**.  

---

## Key Insights
1. **Overtime = Faktor Risiko Tertinggi**
   - Karyawan overtime → attrition **31.9%**
   - Karyawan non-overtime → attrition **10.8%**

2. **Departemen Sales = Risiko Tinggi**
   - Attrition tertinggi (**21.3%**) meskipun bukan jumlah kasus terbanyak.

3. **Perbedaan Gender**
   - Pria sedikit lebih tinggi tingkat attrition dibanding wanita.

4. **Overall Attrition**
   - Total: **16.9%**
   - Masih dalam batas normal, tetapi area tertentu butuh intervensi HR.

---

## Model Evaluation
Beberapa algoritma Machine Learning digunakan untuk prediksi attrition:

| Model                | Accuracy | ROC AUC | Precision | Recall | F1-Score |
|-----------------------|----------|---------|-----------|--------|-----------|
| Logistic Regression   | 0.7170   | 0.8046  | 0.3421    | **0.7222** | 0.4643 |
| Random Forest         | 0.8349   | 0.7977  | 0.6000    | 0.0833 | 0.1463 |
| Gradient Boosting     | **0.8585** | 0.7914  | **0.6667** | 0.3333 | 0.4444 |
| KNN                   | 0.8443   | 0.7745  | 0.6364    | 0.1944 | 0.2979 |
| SVM                   | 0.8255   | **0.8507** | 0.4902    | 0.6944 | **0.5747** |

📌 **Best Model**: **SVM** (balanced performance, ROC AUC 0.85, F1-score 0.57)  
📌 **Alternative**: Logistic Regression (recall tinggi → bagus untuk mendeteksi karyawan berisiko resign)  

---

## Conclusion
- **Overtime** terbukti sebagai faktor risiko terbesar terhadap attrition.  
- **Departemen Sales** menunjukkan tingkat turnover tertinggi yang memerlukan perhatian khusus.  
- **Gender gap** relatif kecil namun tetap penting dipantau.  
- **SVM** menjadi model prediksi terbaik yang seimbang, sedangkan Logistic Regression unggul untuk recall tinggi.  

---

## Action Items (HR Recommendations)
1. **Workload & Overtime Management**  
   - Batasi jumlah lembur dengan kebijakan yang jelas.  
   - Implementasikan sistem *shift* yang lebih sehat.  
   - Berikan pelatihan manajemen waktu untuk karyawan.  

2. **Sales Department Retention Program**  
   - Desain **program insentif** berbasis kinerja yang adil.  
   - Sediakan **dukungan mental & psikologis** untuk mengurangi stres target.  
   - Buat **career path** yang lebih jelas untuk meningkatkan motivasi.  

3. **Early Warning System dengan Machine Learning**  
   - Gunakan model **SVM** untuk mendeteksi karyawan berisiko resign.  
   - Lakukan **monitoring rutin** terhadap indikator utama (overtime, business travel, job role).  
   - Integrasikan prediksi ini ke dalam sistem HR sebagai *decision support*.  

4. **Culture & Engagement**  
   - Lakukan **survei kepuasan kerja berkala**.  
   - Fasilitasi program **employee engagement** untuk menjaga loyalitas.  
   - Tinjau ulang **perbedaan gender & struktural** yang mungkin berpengaruh pada attrition.  

---

## Dashboard
Visualisasi dibuat dalam bentuk **dashboard interaktif**:  
- **Overview**: Total attrition, income, tenure.  
- **Demografi & Personal Factors**: Gender, usia, pendidikan, marital status.  
- **Job & Work Factors**: Overtime, business travel, job role.  

[Lihat Dashboard Interaktif di Looker Studio](https://lookerstudio.google.com/reporting/fcdc2531-b7a0-4c23-a875-d0f83cf2ae06)  

---

## Running File Prediction

Sebelum menjalankan proses prediksi, pastikan semua dependensi Python sudah terpasang.

### 1. Clone Repository
```bash
git clone https://github.com/MIAbidin/Employee-Attrition-Analysis.git
cd Employee-Attrition-Analysis
```

### 2. Buat Virtual Environment (Opsional)
```bash
python -m venv venv
source venv/bin/activate   # Linux/MacOS
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
Semua library yang dibutuhkan tersedia pada file requirements.txt.
```bash
pip install -r requirements.txt
```

Jalankan script prediction.py untuk memprediksi attrition pada satu karyawan (data bisa diedit langsung di dalam script):
```bash
python prediction.py
```
Contoh output:

    ==================================================
    EMPLOYEE ATTRITION PREDICTION
    ==================================================
    Prediction Result : ATTRITION
    Probability       : 40.12
    ==================================================
