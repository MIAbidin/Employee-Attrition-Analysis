# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

### Latar Belakang
Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000 dengan lebih dari 1.000 karyawan yang tersebar di seluruh negeri.  

Meskipun perusahaan sudah berkembang cukup besar, Jaya Jaya Maju menghadapi tantangan serius dalam mengelola karyawan, yang berdampak pada tingginya **attrition rate** (rasio jumlah karyawan yang keluar dibanding total karyawan). Saat ini, attrition rate mencapai lebih dari **10%**, sehingga dapat memengaruhi stabilitas dan produktivitas perusahaan.  

Manajer HR ingin mengetahui faktor-faktor utama penyebab attrition sekaligus memerlukan **business dashboard** untuk memantau kondisi tersebut secara real-time.

---

### Permasalahan Bisnis
- Tingginya **attrition rate (16.9%)** di perusahaan.  
- Risiko resign lebih tinggi pada **karyawan yang lembur (overtime)**.  
- Departemen **Sales** mengalami turnover tertinggi.  
- Perbedaan gender meskipun kecil tetap menunjukkan adanya potensi kesenjangan.  
- HR belum memiliki sistem prediksi maupun dashboard interaktif untuk memantau faktor-faktor ini.  

---

### Cakupan Proyek
1. **Analisis Data HR** untuk mengetahui faktor-faktor yang memengaruhi attrition.  
2. **Pembangunan Model Machine Learning** untuk memprediksi karyawan berisiko resign.  
3. **Pembuatan Business Dashboard** interaktif sebagai alat bantu monitoring HR.  

---

### Persiapan

- **Sumber Data**: Dataset HR (1.470 karyawan, 35 fitur awal → 44 fitur setelah encoding).  
- **Setup Environment**:

   ```bash
   # Clone repository
   git clone https://github.com/MIAbidin/Employee-Attrition-Analysis.git
   cd Employee-Attrition-Analysis

   # (Opsional) Buat virtual environment
   python -m venv venv
   source venv/bin/activate   # Linux/MacOS
   venv\Scripts\activate      # Windows

   # Install dependencies
   pip install -r requirements.txt

   # Jalankan file prediksi
   python prediction.py
   ```

## Business Dashboard

Dashboard interaktif dibuat untuk membantu HR memantau berbagai faktor yang memengaruhi attrition.  

**Fitur Dashboard**:  
- **Overview**: Total attrition, income, tenure.  
- **Demografi & Personal Factors**: Gender, usia, pendidikan, marital status.  
- **Job & Work Factors**: Overtime, business travel, job role.  

🔗 [Lihat Dashboard Interaktif di Looker Studio](https://lookerstudio.google.com/reporting/fcdc2531-b7a0-4c23-a875-d0f83cf2ae06)

---

## Conclusion

- **Overtime** adalah faktor risiko terbesar terhadap attrition (attrition 31.9%).  
- **Departemen Sales** memiliki tingkat turnover tertinggi (21.3%).  
- **Gender** sedikit berpengaruh, dengan pria lebih tinggi tingkat attrition dibanding wanita.  
- Dari hasil evaluasi model, **SVM** menjadi model prediksi terbaik dengan performa seimbang (ROC AUC 0.85, F1-score 0.57). Logistic Regression unggul dalam recall sehingga cocok untuk mendeteksi karyawan berisiko resign.  

---

### Rekomendasi Action Items

1. **Workload & Overtime Management**  
   - Batasi lembur dengan kebijakan yang jelas.  
   - Terapkan sistem shift yang lebih sehat.  
   - Berikan pelatihan manajemen waktu.  

2. **Retention Program untuk Departemen Sales**  
   - Berikan program insentif berbasis kinerja.  
   - Dukungan mental & psikologis bagi karyawan.  
   - Career path yang lebih jelas.  

3. **Implementasi Early Warning System**  
   - Gunakan model Machine Learning (SVM/Logistic Regression) untuk mendeteksi risiko resign.  
   - Monitoring rutin indikator utama (overtime, job role, business travel).  

4. **Culture & Engagement**  
   - Survei kepuasan kerja secara berkala.  
   - Program employee engagement untuk meningkatkan loyalitas.  
   - Tinjau ulang kebijakan terkait kesenjangan gender & struktural.  
