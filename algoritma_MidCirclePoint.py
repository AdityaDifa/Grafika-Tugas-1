import math
import matplotlib.pyplot as plt

def minuskan(x):
    array_x = []
    for indeks in range(len(x)):
        array_x.append(x[indeks]* (-1))
    
    return array_x

class algoritma_MidCirclePoint:
    #untuk menyimpan nilai array yang dicerminkan di  kuadran kanan atas
    array_x2 = []
    array_y2 = []


    def __init__(self,jari_jari):
        self.jari_jari = abs(jari_jari) #di abselut agar kita bisa mulai dari kuadran kanan atas

        #set x awal yaitu x1,y1 = (0,r)
        self.array_x = [0]
        self.nilai_x = 0
        self.array_y = [self.jari_jari]
        self.nilai_y = self.jari_jari

        #p = 1-r
        self.nilai_p = 1 - self.jari_jari

        print(f"titik awal : {self.array_x[0]} dan {self.array_y[0]}")
        print(f"nilai p = 1-r = 1 - {self.jari_jari} = {self.nilai_p}")

    def hitung(self):
        '''
        jika p < 0
        x = x + 1
        y = y
        p = p + 2x + 1

        jika p >= 0
        x = x + 1 
        y = y - 1
        p = p + 2x + 1 - 2y

        tentukan sampai x >= y
        selanjutnya x dan y ditukar posisi
        '''
        while not(self.nilai_x >= self.nilai_y): #rumus 1/ langkah 1
            self.nilai_x = self.nilai_x + 1 #x tambah 1
            self.array_x.append(self.nilai_x) #tambahkan x ke array

            if self.nilai_p < 0:
                self.nilai_p = self.nilai_p + (2*self.nilai_x) + 1 #cari nilai p
            elif self.nilai_p >= 0:
                self.nilai_y = self.nilai_y - 1 #perbarui nilai y
                self.nilai_p = self.nilai_p + (2*self.nilai_x) + 1 - (2*self.nilai_y) #cari p dulu karena menggunakan y yang belum diubah
                
            self.array_y.append(self.nilai_y) #menambahkan y ke array

        #langkah 2, membalikan x dan y yang sudah ditemukan untuk melengkapi kuadran kanan atas
        print(self.array_x)
        print(self.array_y)
        for indeks in range(len(self.array_x)):
            self.array_x2.append(self.array_y[len(self.array_y) - indeks - 1])
            self.array_y2.append(self.array_x[len(self.array_x) - indeks - 1])
        
        print("perhitungan selesai!")
        print(f"kuadran satu = \nx = {self.array_x}{self.array_x2}\ny = {self.array_y}{self.array_y2}")

    def show(self):
        print("menampilkan tabel")

        # Menambahkan judul dan label sumbu
        plt.figure(3)
        plt.suptitle("Algoritma MidCirclePoint | Aditya Difa 123210085")
        plt.title('Plot Scatter dari Array x dan y')
        plt.xlabel('Nilai x')
        plt.ylabel('Nilai y')

        #menambahkan grid
        plt.grid(True)

        # bikin garis
        #kuadran atas kanan
        plt.scatter(self.array_x, self.array_y, color="#ff0000", marker='o', s=300)
        plt.scatter(self.array_x2, self.array_y2, color="#b50000", marker='o', s=300)
        #kuadran bawah kanan
        plt.scatter(self.array_x, minuskan(self.array_y), color="#26ff00", marker='o', s=300)
        plt.scatter(self.array_x2, minuskan(self.array_y2), color="#1ec700", marker='o', s=300)
        #kuadran kiri atas
        plt.scatter(minuskan(self.array_x), self.array_y, color="#00ffd5", marker='o', s=300)
        plt.scatter(minuskan(self.array_x2), self.array_y2, color="#00b597", marker='o', s=300)
        #kuadran kiri bawah
        plt.scatter(minuskan(self.array_x),minuskan(self.array_y), color="#ffff00", marker='o', s=300)
        plt.scatter(minuskan(self.array_x2),minuskan(self.array_y2), color="#bfbf00", marker='o', s=300)

        # Menampilkan plot
        plt.show()