from matplotlib import pyplot as plt


class Skala:
    #segitiga awal
    segitiga_x = [0,0,3]
    segitiga_y = [0,3,0]
    
    def __init__(self,x,y) -> None:
        self.skala_x = x
        self.skala_y = y

    def hitung(self) -> None:
        #tempat menampung x dan y
        hasil_x = []
        hasil_y = []
        for i in range(len(self.segitiga_x)):
            hasil_x.append(self.segitiga_x[i]*self.skala_x)
            hasil_y.append(self.segitiga_y[i]*self.skala_y)
    
    #tampilkan
        plt.figure(7)
        plt.suptitle("Algoritma Skala | Aditya Difa 123210085")
        plt.title('Plot Scatter dari Array x dan y')
        plt.xlabel('Nilai x')
        plt.ylabel('Nilai y')

        plt.grid(True)

         #segitiga awal
        plt.plot([self.segitiga_x[0],self.segitiga_x[2]],[self.segitiga_y[0],self.segitiga_y[2]],color = 'black')
        plt.plot([self.segitiga_x[0],self.segitiga_x[1]],[self.segitiga_y[0],self.segitiga_y[1]],color = 'black')
        plt.plot([self.segitiga_x[1],self.segitiga_x[2]],[self.segitiga_y[1],self.segitiga_y[2]],color = 'black')

        #segitiga akhir
        plt.plot([hasil_x[0],hasil_x[1]],[hasil_y[0],hasil_y[1]],color = 'red')
        plt.plot([hasil_x[0],hasil_x[2]],[hasil_y[0],hasil_y[2]],color = 'red')
        plt.plot([hasil_x[1],hasil_x[2]],[hasil_y[1],hasil_y[2]],color = 'red')


        plt.show()