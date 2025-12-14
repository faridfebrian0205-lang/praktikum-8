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

