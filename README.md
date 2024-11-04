# lapby.03

NAMA: MUHAMMAD RAFI ALBANI RASYIN

NIM: 312410316

KELAS: TI.24.A.4

MATKUL: BAHASA PEMOGRAMAN

## Latihan 1

1. Tampilkan n bilangan acak yang lebih kecil dari 0.5.
2. nilai n diisi pada saat runtime
3. anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya
4. gunakan fungsi random() yang dapat diimport terlebih dahulu

```python
from random import random

N = int(input("Masukkan nilai N: "))

i = 1
while i <= N:
    r = random()
    print(f"data ke: {i} => {r}")
    i += 1
````

## Membangkitkan Nilai Random() memasukan Nilai N dan menggunakan while

```python
from random import random
````

kode program ini untuk memanggil fungsi random() yang terletak pada library python itu sendiri

```python
N = int(input("Masukkan nilai N: "))
````

memasukan inputan N

```python
i = 1
while i <= N:
    r = random()
    print(f"data ke: {i} => {r}")
    i += 1
````

kode ini menggunakan perulangan dengan fungsi while yang dimana memprogramkan variable i lebih dari N(i=1),dan akan proses ke fungsi random() yang dibungkus oleh variable (r) ,cetak "data {i} yang dimana (i) itu (1),=> ke variable (r) yaitu random()

```python
i += 1
````

i+= 1 yaitu akan menambahkan menjadi 2,karena diprogram itu index 1=0,jika 0 < N maka output yang keluar tanpa batas.

hasil program tersebut

![Screenshot 2024-11-04 234022](https://github.com/user-attachments/assets/8fe5819a-986b-4cc8-9fd7-cae0e30fcac3)

![Screenshot 2024-11-04 234121](https://github.com/user-attachments/assets/439bf07f-0e3a-4890-8d87-22730c16e6ed)

