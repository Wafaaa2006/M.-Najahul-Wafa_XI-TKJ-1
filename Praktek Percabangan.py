# Nama      : M. Najahul Wafa
# Kelas     : XI TKJ 1
# No.absen  : 19

# Mengambil input total belanjaan dari pelanggan
total_belanjaan = float(input("Masukkan total belanjaan pelanggan: "))

# Inisialisasi variabel diskon
diskon = 0

# Periksa total belanjaan dan tentukan diskon
if total_belanjaan > 500000:
    diskon = 0.10  # Diskon 10%
elif 300000 <= total_belanjaan <= 500000:
    diskon = 0.05  # Diskon 5%

# Hitung jumlah diskon
jumlah_diskon = total_belanjaan * diskon

# Hitung total yang harus dibayar setelah diskon
total_setelah_diskon = total_belanjaan - jumlah_diskon

# Tampilkan hasil
print(f"Total belanjaan: {total_belanjaan} IDR")
print(f"Diskon: {diskon * 100}%")
print(f"Jumlah diskon: {jumlah_diskon} IDR")
print(f"Total yang harus dibayar setelah diskon: {total_setelah_diskon} IDR")
