from matplotlib import pyplot as plt
class Translasi:
    array_x = [0,0,3]
    array_y = [0,3,0]
    def __init__(self,x,y):
        self.poin_x = x
        self.poin_y = y

    def geser(self):
        #ambil nilai segitiga awal dulu
        

        #geser/translasi
        for i in range(3):
            self.array_x[i] += self.poin_x #geser sejumlah nilai x dan y nya
            self.array_y[i] += self.poin_y

        #tampilkan
        plt.figure(6)
        plt.suptitle("Algoritma Translasi | Aditya Difa 123210085")
        plt.title('Plot Scatter dari Array x dan y')
        plt.xlabel('Nilai x')
        plt.ylabel('Nilai y')

        plt.grid(True)

        #menyimpan tempat
        segitiga_x = [0,0,3]
        segitiga_y = [0,3,0]
        print(f'{segitiga_x}')
        print(f'{segitiga_y}')

        #segitiga awal
        plt.plot([segitiga_x[0],segitiga_x[1]],[segitiga_y[0],segitiga_y[1]],color = 'black')
        plt.plot([segitiga_x[0],segitiga_x[2]],[segitiga_y[0],segitiga_y[2]],color = 'black')
        plt.plot([segitiga_x[1],segitiga_x[2]],[segitiga_y[1],segitiga_y[2]],color = 'black')

        plt.plot([self.array_x[0],self.array_x[1]],[self.array_y[0],self.array_y[1]],color = 'red')
        plt.plot([self.array_x[0],self.array_x[2]],[self.array_y[0],self.array_y[2]],color = 'red')
        plt.plot([self.array_x[1],self.array_x[2]],[self.array_y[1],self.array_y[2]],color = 'red')


        plt.show()

