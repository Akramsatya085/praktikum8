class Mahasiswa:
  def __init__(self, nama, nim, nilai):
    self.nama = nama
    self.nim = nim
    self.nilai = nilai

  def tampilkan_nilai(self):
    print(f'Nama: {self.nama}')
    print(f'NIM: {self.nim}')
    print(f'Nilai: {self.nilai}')

# Inisialisasi objek Mahasiswa
mahasiswa1 = Mahasiswa('Akram satya', '312210461', 85)
mahasiswa2 = Mahasiswa('aisha ramdhani', '654321', 95)

# Menampilkan nilai mahasiswa1
mahasiswa1.tampilkan_nilai()

# Menampilkan nilai mahasiswa2
mahasiswa2.tampilkan_nilai()
