import math
import matplotlib.pyplot as plt

class Algoritma_DDA:
    x_increment = 0.
    y_increment = 0.
    step = 0.
    dx = 0.
    dy = 0.

    def __init__(self,x1, y1,x2,y2):
        self.nilai_x1 = x1
        self.nilai_y1 = y1
        self.nilai_x2 = x2
        self.nilai_y2 = y2
        self.temp_x = x1
        self.temp_y = y1

        #nilai x dan y awal
        self.x_array = [self.nilai_x1]
        self.y_array = [self.nilai_y1]


    def hitung(self):
        print("sedang menghitung")
        #langkah 1 : cari selisih x dan y
        self.dx = self.nilai_x2 - self.nilai_x1
        self.dy = self.nilai_y2 - self.nilai_y1
        print(f"nilai dx = {self.dx} dan nilai dy = {self.dy}")

        #langkah 2 : tentukan step
        if abs(self.dy) > abs(self.dx): #jika |dy| lebih besar dari |dx| maka step = |dy|
            self.step = abs(self.dy)
            print(f"step = dy yaitu {self.step}")
        else:
            self.step = abs(self.dx) #jika tidak maka step = |dx|
            print(f"step = dx yaitu {self.step}")

        #langkah 3 : mencari nilai increment
        print("menghitung step")
        self.x_increment = self.dx/self.step 
        self.y_increment = self.dy/self.step
        print(f"nilai increment x dan y adalah {self.x_increment} dan {self.y_increment}")
        print(f"array awal \nx = {self.x_array}\ny = {self.y_array}")

        #perulangan nilai x dan y
        for indeks in range(int(self.step)):
            self.temp_x += self.x_increment
            self.x_array.append(self.temp_x)
            self.temp_y += self.y_increment
            self.y_array.append(self.temp_y)
        #===================================================================
        # while self.temp_x != self.nilai_x2 or self.temp_y != self.nilai_y2:
        #     # self.temp_x += self.x_increment
        #     # self.temp_y += self.y_increment
        #     # self.x_array.append(self.temp_x)
        #     # self.y_array.append(self.temp_y)

        #     if self.temp_x != self.nilai_x2:
        #         self.temp_x += self.x_increment
        #         self.x_array.append(self.temp_x)
        #     # else:
        #     #     self.x_array.append(self.temp_x)

        #     if self.temp_y != self.nilai_y2:
        #         self.temp_y += self.y_increment
        #         self.y_array.append(self.temp_y)
        #     # else:
        #     #     self.y_array.append(self.temp_y)
        #===========================================

        print(f"array x = {self.x_array}\narray y = {self.y_array}\n")

        #langkah terakhir : memperbaiki nilai yang koma/ membulatkan semuanya
        for indeks in range(len(self.x_array)):
            self.x_array[indeks] = round(self.x_array[indeks])

        for indeks in range(len(self.y_array)):
            self.y_array[indeks] = round(self.y_array[indeks])

        print("hitung selesai")

    def show(self):
        #mengintegerkan array
        for indeks in range(len(self.x_array)):
            self.x_array[indeks] = int(self.x_array[indeks])
            self.y_array[indeks] = int(self.y_array[indeks])

        print(self.x_array)
        print(self.y_array)
        print("menampilkan tabel")

        # Menambahkan judul dan label sumbu
        plt.figure(1)
        plt.suptitle("Algoritma DDA | Aditya Difa 123210085")
        plt.title('Plot Scatter dari Array x dan y')
        plt.xlabel('Nilai x')
        plt.ylabel('Nilai y')

        #menambahkan grid
        plt.grid(True)

        # bikin garis
        plt.scatter(self.x_array, self.y_array, color='red', marker='o', s=300)

        # Menampilkan plot
        plt.show()
