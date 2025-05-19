# %%
import pandas as pd

# %%
# Membaca dataset
data = pd.read_csv("students.csv")

# %%
# Menampilkan 10 baris pertama
print(data.head(10))

# %%
# Menampilkan informasi dataset
data.info()

# %%
# Mengecek jumlah missing values di setiap fitur
print("\nMissing values sebelum handling:")
print(data.isna().sum())

# %%
# Mengatasi missing value pada fitur lunch dengan modus
if 'lunch' in data.columns:
    data['lunch'] = data['lunch'].fillna(data['lunch'].mode()[0])

# %%
# Mengatasi missing value pada fitur reading score dengan mean
if 'reading score' in data.columns:
    data['reading score'] = data['reading score'].fillna(data['reading score'].mean())

# %%
# Mengatasi missing value pada fitur grade dengan median
if 'grade' in data.columns:
    data['grade'] = data['grade'].fillna(data['grade'].median())

# %%
# Mengecek kembali apakah masih ada missing values
print("\nMissing values setelah handling:")
print(data.isna().sum())

# %%
# Menampilkan informasi dataset setelah handling missing values
data.info()

# %%
# Alternatif handling missing values

# Mengecek apakah kolom "nama_fitur" ada sebelum melakukan interpolasi
if 'nama_fitur' in data.columns:
    # Menggunakan teknik interpolasi
    data['nama_fitur'] = data['nama_fitur'].interpolate(method='linear')

    # Menggunakan teknik backward fill
    data['nama_fitur'] = data['nama_fitur'].fillna(method='bfill')

    # Menggunakan teknik forward fill
    data['nama_fitur'] = data['nama_fitur'].fillna(method='ffill')
else:
    print("\nKolom 'nama_fitur' tidak ditemukan dalam dataset. Melewati tahap interpolasi.")

# %%
# Menggunakan teknik dropping untuk menghapus baris dengan missing value
data = data.dropna(axis=0)

# %%
# Menggunakan teknik dropping untuk menghapus fitur dengan lebih dari 50% missing value
threshold = len(data) * 0.5
data = data.dropna(thresh=threshold, axis=1)

# %%
# Menampilkan informasi dataset setelah alternatif handling missing values
data.info()
