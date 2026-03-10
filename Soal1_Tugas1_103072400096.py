def isKabisat(tahun):
    """Fungsi untuk menentukan apakah suatu tahun merupakan tahun kabisat
    
    Parameters:
        tahun (int): Tahun yang akan diperiksa
    
    Returns:
        bool: True jika tahun kabisat, False jika bukan
    """
    if tahun % 400 == 0:
        return True
    elif tahun % 100 == 0:
        return False
    elif tahun % 4 == 0:
        return True
    else:
        return False

# Memanggil fungsi dan memeriksa hasilnya
print("Cek tahun kabisat")
daftar_tahun = [2003, 2024, 2000, 2100, 1900, 2028, 2025]

for tahun in daftar_tahun:
    hasil = isKabisat(tahun)
    if hasil:
        print(f"Tahun {tahun} adalah tahun kabisat")
    else:
        print(f"Tahun {tahun} Bukan tahun kabisat")

print("\nPengecekan manual")
try:
    tahun_input = int(input("Masukan tahun yang ingin diperiksa: "))
    if isKabisat(tahun_input):
        print(f"Tahun {tahun_input} adalah tahun kabisat")
    else:
        print(f"Tahun {tahun_input} bukan tahun kabisat")
except ValueError:
    print("Error: masukkan angka tahun yang valid")