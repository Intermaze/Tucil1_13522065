import time
import os
import random

def findAllBuffer(iTemp: int, jTemp: int, currentBufferSize: int, currentBuffer: list[list], isMoveVertikal: bool):
	if currentBufferSize == bufferSize: #Jika buffer penuh
		if currentBuffer not in allBuffer:
			allBuffer.append(currentBuffer)
	else:
		if ([iTemp, jTemp]) in currentBuffer: #Jika koordinat sudah diakses, move tidak valid
			pass
		else:
			currentBufferSize += 1
			nextBuffer = currentBuffer.copy()
			nextBuffer.append([iTemp, jTemp])
			if isMoveVertikal:
				isMoveVertikal = not isMoveVertikal
				for i in range(0, mBar):
					findAllBuffer(i, jTemp, currentBufferSize, nextBuffer, isMoveVertikal)
			else:
				isMoveVertikal = not isMoveVertikal
				for j in range(0, mKol):
					findAllBuffer(iTemp, j, currentBufferSize, nextBuffer, isMoveVertikal)	

def isSekuensInBuffer(buffer, sekuens):
    n = len(buffer)
    m = len(sekuens)
    for i in range(n - m + 1):
        for j in range(m):
            if matrix[buffer[i + j][0]][buffer[i + j][1]] != sekuens[j]:
                break
        else:  
            return True
    return False

def poinInBuffer(buffer):
	poin = 0
	for case in range(len(sekuensMatrix)):
		if (isSekuensInBuffer(buffer, sekuensMatrix[case])):
			poin += poinArray[case]
	return poin

def solver(allBuffer):
	for i in range(len(allBuffer)):
		if i == 0:
			maxBuffer = allBuffer[0]
			maxPoin = poinInBuffer(maxBuffer)
		else:
			if poinInBuffer(allBuffer[i]) > maxPoin:
				maxBuffer = allBuffer[i]
				maxPoin = poinInBuffer(maxBuffer)
	
	return (maxBuffer, maxPoin)

def randomElementFromArr(array):
	i = random.randrange(len(array))
	return array[i]

print("Selamat datang ke program solver minigame Cyberpunk2077!")
print("1. Melalui Text File")
print("2. Melalui CLI")
while True:
	cara = input("Mau pakai cara mana?: ")
	if cara.isdigit():
		cara = int(cara)
		if cara == 1 or cara == 2:
			break
	print("Cara tidak valid.")
		
#Input cara text
if cara == 1:
	filename = input("Masukkan nama file (Taruh di dalam folder yang sama): ")
	try:
		f = open(filename, "r")
	except FileNotFoundError: 
		print("File tidak ditemukan. ")
		time.sleep(3)
		exit()
	print()

	bufferSize = int(f.readline())
	mBarKol = f.readline().split(" ")
	mKol = int(mBarKol[0])
	mBar = int(mBarKol[1])
	matrix = [f.readline().rstrip().split(" ") for _ in range(mBar)]
	
	nSekuens = int(f.readline())
	sekuensMatrix = [[0] for i in range(nSekuens)]
	poinArray = [0 for i in range(nSekuens)]
	for i in range(nSekuens):
		sekuensMatrix[i] = f.readline().rstrip().split(" ")
		poinArray[i] = int(f.readline())

#input cara CLI
else:
	nToken = int(input("Masukkan jumlah token unik: "))
	token = [str(x) for x in input("Masukkan token: ").split()]
	bufferSize = int(input("Masukkan ukuran buffer: "))
	mKol, mBar = map(int, input("Masukkan ukuran matriks: ").split())
	nSekuens = int(input("Masukkan jumlah sekuens: "))
	sekuensSize = int(input("Masukkan ukuran maksimal sekuens: "))
	print()

	matrix = [[randomElementFromArr(token) for j in range(mKol)] for i in range(mBar)]
	sekuensMatrix = [[randomElementFromArr(token) for j in range(random.randint(1,sekuensSize-1))] for i in range(nSekuens)]
	poinArray = [random.randint(0,100) for i in range(nSekuens)]
	
	print("Matrix: ")
	for bar in matrix:
		print(*bar)
	print()

	print("Sekuens: ")
	for i in range(nSekuens):
		print(*sekuensMatrix[i])
		print(poinArray[i])
	print()


start = time.time()

allBuffer = []
findAllBuffer(0, 0, 0, [], True)
(maxBuffer, maxPoin) = solver(allBuffer)

end = time.time()
waktu = str(round((end - start)*1000)) + " ms"

print(maxPoin)

for i in range(bufferSize-1):
	print(matrix[maxBuffer[i][0]][maxBuffer[i][1]], end= " ")
print(matrix[maxBuffer[bufferSize-1][0]][maxBuffer[bufferSize-1][1]])

for i in range(bufferSize):
	print(maxBuffer[i][1]+1, end=", ")
	print(maxBuffer[i][0]+1)

print()
print(waktu)
print()

konfirmasi = input("Apakah ingin menyimpan solusi? (y/n) ")
if konfirmasi == "y": #Jika input n atau bukan y, tidak melakukan penyimpanan
	f2 = open("SolusiCyberpunk2077.txt", "w")
	if cara == 2: #Format output text matrix dan sekuens untuk cara 2
		f2.write("Matrix: \n")
		for i in range(mBar):
			for j in range(mKol):
				f2.write(str(matrix[i][j]))
				f2.write(" ")
			f2.write("\n")
		f2.write("\n")

		f2.write("Sekuens: \n")
		for i in range(nSekuens):
			for j in range(len(sekuensMatrix[i])):
				f2.write(str(sekuensMatrix[i][j]))
				f2.write(" ")
			f2.write("\n")
			f2.write(str(poinArray[i]))
			f2.write("\n")
		f2.write("\n")

	f2.write(str(maxPoin))
	f2.write("\n")

	l = ""
	for i in range(bufferSize-1):
		l += str(matrix[maxBuffer[i][0]][maxBuffer[i][1]]) + " "
	l += str(matrix[maxBuffer[bufferSize-1][0]][maxBuffer[bufferSize-1][1]])
	f2.write(l)
	f2.write("\n")

	
	for i in range(bufferSize):
		l = ""
		l += str(maxBuffer[i][1]+1) + ", "
		l += str(maxBuffer[i][0]+1)
		f2.write(l)
		f2.write("\n")
	
	f2.write("\n")
	f2.write(str(waktu))
	f2.write("\n")
	f2.close()

if cara == 1:
	f.close()

