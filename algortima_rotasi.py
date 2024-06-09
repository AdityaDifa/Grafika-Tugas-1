import math

from matplotlib import pyplot as plt


class Rotasi:
    def __init__(self,derajat) -> None:
        self.derajat = derajat

    def hitung(self):
        #segitiga awal
        segitiga_x = [0,3,0]
        segitiga_y = [0,0,3]
        hasil_x = []
        hasil_y = []
        pivot_x = 0
        pivot_y = 0

        #mencari titik P(pivot point)
        for i in range(3):
            pivot_x = pivot_x + segitiga_x[i]
            pivot_y = pivot_y + segitiga_y[i]

        pivot_x = pivot_x/3
        pivot_y = pivot_y/3

        #menghitung skala
        sudut_radian = math.radians(self.derajat)
        for i in range(3):
            hasil_x.append(pivot_x + (segitiga_x[i]-pivot_x)*math.cos(sudut_radian) - (segitiga_y[i]-pivot_y)*math.sin(sudut_radian))
            hasil_y.append(pivot_y + (segitiga_x[i]-pivot_x)*math.sin(sudut_radian)+(segitiga_y[i]-pivot_y)*math.cos(sudut_radian))

        #tampilkan
        plt.figure(8)
        plt.suptitle("Algoritma Rotasi | Aditya Difa 123210085")
        plt.title('Plot Scatter dari Array x dan y')
        plt.xlabel('Nilai x')
        plt.ylabel('Nilai y')

        plt.grid(True)

         #segitiga awal
        plt.plot([segitiga_x[0],segitiga_x[2]],[segitiga_y[0],segitiga_y[2]],color = 'black')
        plt.plot([segitiga_x[0],segitiga_x[1]],[segitiga_y[0],segitiga_y[1]],color = 'black')
        plt.plot([segitiga_x[1],segitiga_x[2]],[segitiga_y[1],segitiga_y[2]],color = 'black')
        plt.scatter(0,0,label = "A",color = 'black')
        plt.scatter(0,3,label = "C",color = 'brown')
        plt.scatter(3,0,label = "B",color = 'gray')

        #segitiga akhir
        plt.plot([hasil_x[0],hasil_x[1]],[hasil_y[0],hasil_y[1]],color = 'red')
        plt.plot([hasil_x[0],hasil_x[2]],[hasil_y[0],hasil_y[2]],color = 'red')
        plt.plot([hasil_x[1],hasil_x[2]],[hasil_y[1],hasil_y[2]],color = 'red')
        plt.scatter(hasil_x[0],hasil_y[0],label = "A'",color = 'purple')
        plt.scatter(hasil_x[1],hasil_y[1],label = "B'",color = 'orange')
        plt.scatter(hasil_x[2],hasil_y[2],label = "C'",color = 'green')

        plt.legend()

        plt.show()