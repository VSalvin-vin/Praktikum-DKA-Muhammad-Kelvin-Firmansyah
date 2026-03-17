import numpy as np

print("PROGRAM DATA MAHASISWA")

data_mahasiswa = np.array([], dtype=[
    ('Nama', 'U50'),
    ('NIM', 'U20'),
    ('Nilai', 'f8'),
    ('TahunMasuk', 'i4')
])

while True:
    print("\nMasukkan Data Mahasiswa:")
    nama = input("Nama: ")
    nim = input("NIM: ")
    nilai = float(input("Nilai: "))
    tahun = int(input("Tahun Masuk: "))
    
    data_baru = np.array([(nama, nim, nilai, tahun)], dtype=data_mahasiswa.dtype)
    if len(data_mahasiswa) == 0:
        data_mahasiswa = data_baru
    else:
        data_mahasiswa = np.concatenate([data_mahasiswa, data_baru])
    
    lagi = input("\nTambah data lagi? (y/n): ")
    if lagi.lower() != 'y':
        break

print("\nDATA SELURUH MAHASISWA")
print(f"{'No':<4} {'Nama':<20} {'NIM':<15} {'Nilai':<8} {'Tahun Masuk':<12}")
print("-" * 60)

for i, mhs in enumerate(data_mahasiswa):
    print(f"{i+1:<4} {mhs['Nama']:<20} {mhs['NIM']:<15} {mhs['Nilai']:<8.2f} {mhs['TahunMasuk']:<12}")

print("\nSTATISTIK NILAI")
nilai_tertinggi = np.max(data_mahasiswa['Nilai'])
nilai_terendah = np.min(data_mahasiswa['Nilai'])
nilai_rata = np.mean(data_mahasiswa['Nilai'])

print(f"Nilai Tertinggi: {nilai_tertinggi:.2f}")
print(f"Nilai Terendah: {nilai_terendah:.2f}")
print(f"Nilai Rata-rata: {nilai_rata:.2f}")

print("\nPENCARIAN MAHASISWA")
while True:
    keyword = input("\nMasukkan NIM atau Nama yang dicari: ")
    
    mask_nim = np.char.find(data_mahasiswa['NIM'], keyword) >= 0
    mask_nama = np.char.find(data_mahasiswa['Nama'].astype(str), keyword) >= 0
    hasil = data_mahasiswa[mask_nim | mask_nama]
    
    if len(hasil) > 0:
        print("\nHasil Pencarian:")
        print(f"{'Nama':<20} {'NIM':<15} {'Nilai':<8} {'Tahun Masuk':<12}")
        print("-" * 55)
        for mhs in hasil:
            print(f"{mhs['Nama']:<20} {mhs['NIM']:<15} {mhs['Nilai']:<8.2f} {mhs['TahunMasuk']:<12}")
    else:
        print("Data tidak ditemukan!")
    
    cari_lagi = input("\nCari lagi? (y/n): ")
    if cari_lagi.lower() != 'y':
        break