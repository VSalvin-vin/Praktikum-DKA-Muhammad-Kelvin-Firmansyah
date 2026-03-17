import numpy as np

print("PROGRAM INVENTARIS BARANG")

data_barang = np.array([], dtype=[
    ('NamaBarang', 'U50'),
    ('KodeBarang', 'U20'),
    ('Jumlah', 'i4'),
    ('HargaPerUnit', 'f8')
])

while True:
    print("\nMasukkan Data Barang:")
    nama = input("Nama Barang: ")
    kode = input("Kode Barang: ")
    jumlah = int(input("Jumlah: "))
    harga = float(input("Harga Per Unit: "))
    
    data_baru = np.array([(nama, kode, jumlah, harga)], dtype=data_barang.dtype)
    if len(data_barang) == 0:
        data_barang = data_baru
    else:
        data_barang = np.concatenate([data_barang, data_baru])
    
    lagi = input("\nTambah data lagi? (y/n): ")
    if lagi.lower() != 'y':
        break

print("\nDATA SELURUH BARANG")
print(f"{'No':<4} {'Nama Barang':<20} {'Kode Barang':<15} {'Jumlah':<8} {'Harga/Unit':<12} {'Total':<15}")
print("-" * 75)

for i, brg in enumerate(data_barang):
    total = brg['Jumlah'] * brg['HargaPerUnit']
    print(f"{i+1:<4} {brg['NamaBarang']:<20} {brg['KodeBarang']:<15} {brg['Jumlah']:<8} {brg['HargaPerUnit']:<12.2f} {total:<15.2f}")

total_inventaris = np.sum(data_barang['Jumlah'] * data_barang['HargaPerUnit'])
print("-" * 75)
print(f"{'TOTAL NILAI INVENTARIS':<63} {total_inventaris:.2f}")

print("\nPENCARIAN BARANG")
while True:
    keyword = input("\nMasukkan Kode Barang atau Nama Barang yang dicari: ")
    
    mask_kode = np.char.find(data_barang['KodeBarang'], keyword) >= 0
    mask_nama = np.char.find(data_barang['NamaBarang'].astype(str), keyword) >= 0
    hasil = data_barang[mask_kode | mask_nama]
    
    if len(hasil) > 0:
        print("\nHasil Pencarian:")
        print(f"{'Nama Barang':<20} {'Kode Barang':<15} {'Jumlah':<8} {'Harga/Unit':<12} {'Total':<15}")
        print("-" * 70)
        for brg in hasil:
            total = brg['Jumlah'] * brg['HargaPerUnit']
            print(f"{brg['NamaBarang']:<20} {brg['KodeBarang']:<15} {brg['Jumlah']:<8} {brg['HargaPerUnit']:<12.2f} {total:<15.2f}")
    else:
        print("Data tidak ditemukan!")
    
    cari_lagi = input("\nCari lagi? (y/n): ")
    if cari_lagi.lower() != 'y':
        break