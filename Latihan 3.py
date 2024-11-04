saldo = 1000000

while True:
    print(f"Saldo saat ini: Rp {saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")
    pilihan = input("Pilih menu : ")

    if pilihan == '1':
        jumlah_penarikan = int(input("Masukkan jumlah penarikan: "))
        if jumlah_penarikan <= saldo:
            saldo -= jumlah_penarikan
            print("Penarikan berhasil!")
        else:
            print("Saldo tidak mencukupi!")
    elif pilihan == '2':
        print("Terima kasih telah menggunakan ATM!")
        break
    else:
        print("Pilihan tidak valid!")

    print()  # Menambahkan baris kosong untuk pemisah antar transaksi
