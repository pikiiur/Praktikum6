data_mahasiswa = []

def tambah(nama, nilai):
    data_mahasiswa.append({'nama': nama, 'nilai': nilai})
    print(f"Data {nama} dengan nilai {nilai} berhasil ditambahkan.")

def tampilkan():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        print("Daftar nilai mahasiswa:")
        for idx, mahasiswa in enumerate(data_mahasiswa, 1):
            print(f"{idx}. Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")

def hapus(nama):
    global data_mahasiswa
    data_mahasiswa = [mhs for mhs in data_mahasiswa if mhs['nama'] != nama]
    print(f"Data {nama} berhasil dihapus.")

def ubah(nama, nilai_baru):
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nama'] == nama:
            mahasiswa['nilai'] = nilai_baru
            print(f"Data {nama} berhasil diubah menjadi nilai {nilai_baru}.")
            break
    else:
        print(f"Data {nama} tidak ditemukan.")

# Contoh penggunaan
tambah('Pikii', 85)
tambah('Dikii', 78)
tambah('Abimm', 90)
tampilkan()

hapus('Dikii')
tampilkan()

ubah('Pikii', 90)
tampilkan()
