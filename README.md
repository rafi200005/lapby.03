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

