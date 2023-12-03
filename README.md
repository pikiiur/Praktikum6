# Pertemuan 11
## Praktikum 6
Buat program sederhana dengan mengaplikasikan penggunaan fungsi
yang akan menampilkan daftar nilai mahasiswa, dengan ketentuan:
1. Fungsi tambah() untuk menambah data
2. Fungsi tapilkan() untuk menampilkan data
3. Fungsi hapus(nama) untuk menghapus data berdasarkan nama
4. Fungsi ubah(nama) untuk mengubah data berdasarkan nama
5. Buat flowchart dan penjelasan programnya pada README.md
6. Commit dan Push ke repository Github

```python
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
```

## Hasil Programnya
![](Screenshot/Tugas%20Praktikum.png)

## Latihan
Ubahlah kode dibawah ini menjadi fungsi menggunakan lambda.
