while True:
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        operator = input("Masukkan operator (+, -, *, /): ")
        angka2 = float(input("Masukkan angka kedua: "))

        if operator == "+":
            hasil = angka1 + angka2
        elif operator == "-":
            hasil = angka1 - angka2
        elif operator == "*":
            hasil = angka1 * angka2
        elif operator == "/":
            hasil = angka1 / angka2  # Bisa memicu ZeroDivisionError
        else:
            raise Exception(f"Operator '{operator}' tidak valid!")

        print("Hasil:", int(hasil))

    except ValueError:
        print("Error: Input harus berupa angka!")
    except ZeroDivisionError:
        print("Error: Tidak bisa melakukan pembagian dengan nol!")
    except Exception as e:
        print("Error:", e)

    # Tanya apakah ingin lanjut
    lanjut = input("\nIngin menghitung lagi? (y/n): ")
    if lanjut.lower() != "y":
        print("Program selesai. terimakasih telah menggunakan kalkulator ini")
        break
