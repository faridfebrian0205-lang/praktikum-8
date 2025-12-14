# praktikum-8

**--Program kalkalkulator aman--**

 <img width="169" height="24" alt="image" src="https://github.com/user-attachments/assets/0d207ba7-bc9e-4558-bf69-b6c69c08e0ee" />
 
Perulangan ini membuat program berjalan terus-menerus sampai pengguna memilih untuk keluar.

 <img width="150" height="20" alt="image" src="https://github.com/user-attachments/assets/c1fc8d23-d89f-4ab7-8021-43774bacc9de" />

Digunakan untuk membungkus kode yang berpotensi menimbulkan error, seperti input yang salah atau pembagian dengan nol.

 <img width="449" height="55" alt="image" src="https://github.com/user-attachments/assets/28d18505-e6e8-4b5f-9606-d50b804703f4" />

 - float() mengubah input menjadi angka desimal.
 - Jika pengguna memasukkan huruf, akan muncul ValueError.

 <img width="498" height="149" alt="Screenshot 2025-12-14 122515" src="https://github.com/user-attachments/assets/5ba8da4e-f95f-44c8-84fe-6631ec3b4691" />

Program mengecek operator yang dimasukkan:

 - Jika sesuai, program melakukan operasi matematika.
 - Pada pembagian, jika angka kedua bernilai 0, akan terjadi ZeroDivisionError.

 <img width="498" height="50" alt="Screenshot 2025-12-14 122515 - Copy" src="https://github.com/user-attachments/assets/d49fb3f1-9f0c-4e7c-9d58-ac474b94e2c3" />

 - Jika operator bukan +, -, *, atau /, maka:
 - Program secara sengaja memunculkan error menggunakan raise Exception
 - Menampilkan pesan kesalahan kustom.

 <img width="273" height="37" alt="image" src="https://github.com/user-attachments/assets/888aaa12-f3cc-472c-9fa1-fd0a48d9b065" />

Menampilkan hasil perhitungan jika tidak terjadi error.

 <img width="423" height="45" alt="image" src="https://github.com/user-attachments/assets/f003252c-e3e2-4e19-ae0d-1233947b4e49" />

Menangani kesalahan input non-angka.

 <img width="488" height="35" alt="image" src="https://github.com/user-attachments/assets/8c81decb-91f0-4cdf-af83-532aee76f93b" />

Menangani kesalahan pembagian dengan nol.

 <img width="252" height="38" alt="Screenshot 2025-12-14 123700" src="https://github.com/user-attachments/assets/ffb514a1-41b7-4314-bf5d-6dad9a837528" />

Menangani error kustom dari operator tidak valid.

 <img width="561" height="89" alt="image" src="https://github.com/user-attachments/assets/de71efd1-4176-4444-80cd-4ce228d9a08d" />

- Jika pengguna mengetik y, program mengulang dari awal.
- Jika tidak, program berhenti dengan break.

**HASIL OUTPUT KALKULATOR AMAN**

 <img width="492" height="275" alt="image" src="https://github.com/user-attachments/assets/d232b8ad-8f7f-4f68-b212-ea3fd22466fc" />

**--Program validasi data--**

 <img width="317" height="29" alt="image" src="https://github.com/user-attachments/assets/538d485e-6750-46de-9ecb-5a8f838bb673" />

List nilai berisi campuran data angka (int) dan string. Data string inilah yang berpotensi menyebabkan error saat proses penjumlahan.

 <img width="172" height="53" alt="image" src="https://github.com/user-attachments/assets/4d738978-f8a1-4ba1-bac4-8e4209b746ab" />

- total digunakan untuk menyimpan jumlah seluruh nilai yang valid (angka).
- jumlah_data digunakan untuk menghitung berapa banyak data angka yang berhasil diproses.

 <img width="175" height="25" alt="image" src="https://github.com/user-attachments/assets/262a4ece-3f34-40e4-8628-e0309f9b1d7c" />

Perulangan for digunakan untuk mengakses setiap elemen di dalam list nilai satu per satu.

 <img width="323" height="105" alt="image" src="https://github.com/user-attachments/assets/e1dbda70-676b-42e6-875e-274b594ab210" />

**try:**
- Mencoba menambahkan nilai n ke variabel total.
- Jika n berupa angka (int atau float), proses berhasil dan jumlah_data bertambah 1.
- Jika n berupa string ('A' atau 'B'), Python akan menghasilkan TypeError karena string tidak bisa dijumlahkan dengan angka.

**except TypeError:**
- Error ditangani tanpa menghentikan program, lalu continue digunakan untuk melewati data tersebut dan melanjutkan ke iterasi berikutnya.

<img width="296" height="36" alt="image" src="https://github.com/user-attachments/assets/45e8202b-7e12-44bf-9f72-57d3418d8307" />

- Rata-rata dihitung dengan membagi total nilai valid dengan jumlah data numerik yang berhasil diproses.

<img width="318" height="47" alt="image" src="https://github.com/user-attachments/assets/a97c3026-d076-4eca-b041-35401026c607" />

- Menampilkan hasil rata-rata nilai yang hanya dihitung dari data angka.

**Kesimpulan**

- Program tetap berjalan meskipun terdapat data tidak valid.
- try-except digunakan untuk menangani error tanpa menghentikan program.
- Hanya data numerik yang dihitung dalam rata-rata.
- Hasil akhir rata-rata adalah 85.0.

**HASIL OUTPUT VALIDASI DATA**

<img width="496" height="93" alt="image" src="https://github.com/user-attachments/assets/cfb1f5b7-4139-4f14-b6ef-9faa8a29811b" />

