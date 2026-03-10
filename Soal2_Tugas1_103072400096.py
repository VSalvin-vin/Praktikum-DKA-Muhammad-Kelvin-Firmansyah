def fibonacci_ke_n(n):
    """Fungsi untuk mengembalikan angka Fibonacci ke-n
    
    Parameters:
        n (int): Posisi bilangan Fibonacci yang diinginkan
    
    Returns:
        int: Bilangan Fibonacci ke-n
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

def cetak_fibonacci(n):
    """Prosedur untuk mencetak barisan Fibonacci dari suku ke-1 hingga ke-n
    
    Parameters:
        n (int): Jumlah suku Fibonacci yang akan dicetak
    """
    if n <= 0:
        print("n harus lebih besar dari 0")
        return
    
    print(f"Barisan Fibonacci dari suku ke-1 hingga ke-{n}:")
    a, b = 0, 1
    for i in range(1, n + 1):
        if i == 1:
            print(f"Suku ke-{i}: {b}")
        else:
            a, b = b, a + b
            print(f"Suku ke-{i}: {b}")
n = 10  

print(f"\nFungsi - Fibonacci ke-{n}: {fibonacci_ke_n(n)}")

print()
cetak_fibonacci(n)

print("\nMasukan Input")
try:
    n_input = int(input("Masukkan nilai n: "))
    print(f"\nFungsi - Fibonacci ke-{n_input}: {fibonacci_ke_n(n_input)}")
    print()
    cetak_fibonacci(n_input)
except ValueError:
    print("Error: masukkan angka yang valid")