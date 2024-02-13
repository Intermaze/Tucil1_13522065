# Tucil1_13522065
Tugas Kecil 1 IF2211 Strategi Algoritma

Dibuat oleh Rafiki Prawhira Harianto | 13522065

## Apa ini?
Program ini adalah solver minigame hacking pada permainan video Cyberpunk 2077. Minigame ini merupakan simulasi hacking jaringan local dari ICE (_Intrusion Countermeasures Electronics_). Program dibuat dalam rangka menyelesaikan Tugas Kecil 1 IF2211 Strategi Algoritma

## Cara menjalankan
Buka folder bin, lalu buka program cyberpunk2077.exe. Ketik 1 jika ingin input matrix secara manual, kemudian ketik case1.txt, case2.txt, case3.txt, atau buat text file sendiri dengan format:
```
buffer_size
matrix_width matrix_height
matrix
number_of_sequences
sequences_1
sequences_1_reward
sequences_2
sequences_2_reward
…
sequences_n
sequences_n_reward
```
Contoh:
```
7
6 6
7A 55 E9 E9 1C 55
55 7A 1C 7A E9 55
55 1C 1C 55 E9 BD
BD 1C 7A 1C 55 BD
BD 55 BD 7A 1C 1C
1C 55 55 7A 55 7A
3
BD E9 1C
15
BD 7A BD
20
BD 1C BD 55
30
```

Ketik 2 untuk input automatis dengan format yang diberikan program. Contohnya:
```
5
BD 1C 7A 55 E9
7
6 6
3
4
```
