import pandas as pd

data = {
    "Nama": ["Mahasiswa 1", "Mahasiswa 2", "Mahasiswa 3"],
    "Algoritma dan Struktur Data 2": [90, 50, 65],
    "Matematika Numerik": [80, 60, 70]
}

df = pd.DataFrame(data)

avg_per_subject = df.mean(numeric_only=True)

df['Rata-rata'] = df.mean(axis=1, numeric_only=True)

print("DataFrame:")
print(df)

print("\nRata-rata nilai untuk setiap mata kuliah:")
print(avg_per_subject)

print("\nRata-rata nilai untuk setiap siswa:")
for index, row in df.iterrows():
    print(f"{row['Nama']}: {row['Rata-rata']}")
