def hitung_fungsi(x):
    return 2 * x**3 + 2 * x + (15 / x)

try:
    x = int(input("Masukkan bilangan bulat x: "))
    if x == 0:
        print("Error: x yang Anda masukkan bukan bilangan bulat.")
    else:
        hasil = hitung_fungsi(x)
        print(f"Hasil f({x}) = {hasil}")
except ValueError:
    print("Error: Harap masukkan bilangan bulat yang valid.")
