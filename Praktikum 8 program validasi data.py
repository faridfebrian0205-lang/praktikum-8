nilai = [97, 89, 'A', 95, 150, 'B']

total = 0
jumlah_data = 0

for n in nilai:
    try:
        total += n
        jumlah_data += 1
    except TypeError:
        # Melewati data yang bukan angka
        continue

rata_rata = total / jumlah_data

print("Rata-rata nilai:", rata_rata)
