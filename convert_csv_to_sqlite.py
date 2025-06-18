import pandas as pd
import sqlite3

# Baca file CSV
df = pd.read_csv('prediction_results.csv')

# Buat koneksi ke database SQLite
conn = sqlite3.connect('jaya_jaya_dashboard.db')

# Simpan data ke dalam tabel
df.to_sql('predictions', conn, if_exists='replace', index=False)

# Tutup koneksi
conn.close()

print("Database berhasil dibuat!")
print(f"File: jaya_jaya_dashboard.db")
print(f"Tabel: predictions")
print(f"Records: {len(df)}")