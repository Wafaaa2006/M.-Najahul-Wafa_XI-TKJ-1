def total_deret_ganjil(batas):
    total = 0
    for i in range(1, batas + 1):
        bilangan_ganjil = 2 * i - 1
        total += bilangan_ganjil
    return total

batas = int(input("Masukkan batas deret ganjil: "))
hasil = total_deret_ganjil(batas)
print(f"Total deret bilangan ganjil hingga batas {batas} adalah {hasil}")