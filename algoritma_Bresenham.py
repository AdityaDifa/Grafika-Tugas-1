import math
import matplotlib.pyplot as plt


class algoritma_Bresenham:

    def __init__(self,x1,x2,y1,y2):
        #x1 harus lebih kecil dari x2 karena gambarnya kiri kekanan
        #cek x1 dan x2
        if x2>x1 : #jika sudah benar
            self.nilai_x1 = x1
            self.nilai_x2 = x2
            self.nilai_y1 = y1
            self.nilai_y2 = y2
        else:
            #kita balik yang x1,y1 jadi x2,y2 dan sebaliknya
            self.nilai_x1 = x2
            self.nilai_x2 = x1
            self.nilai_y1 = y2
            self.nilai_y2 = y1

        #untuk mengecek apakah perlu di mirror atau tidak
        self.nilai_mirror = False #default = false
        
        #cek m atau gradien, jika menaik = 1 dan jika turun(m < 0) kita akan mirror kan
        self.nilai_gradien = ((self.nilai_y2-self.nilai_y1)/(self.nilai_x2-self.nilai_x1))
        if self.nilai_gradien < 0 : #jika m atau gradien menurun (m < 0)
            print(f"gradien menurun, gradien = {self.nilai_gradien}! mencerminkan titik koordinat kedua")
            self.nilai_mirror = True #biar nanti diakhir bisa kita mirror kan kembali
            self.nilai_gradien = abs(self.nilai_gradien) #kita abselutkan
            self.nilai_y2 = self.nilai_y1 + self.nilai_gradien * (self.nilai_x2 - self.nilai_x1) #kita cerminkan sumbu y
        
        print(f"nilai x1 dan y1 = {self.nilai_x1},{self.nilai_y1}")
        print(f"nilai x2 dan y2 = {self.nilai_x2},{self.nilai_y2}")

    def hitung(self):
        #set nilai awal
        self.array_x = [self.nilai_x1]
        self.array_y = [self.nilai_y1]
        print(f"nilai awal x dan y = {self.array_x[0]} dan {self.array_y[0]}")

        #dx = x2-x1
        #dy = y2-y1
        self.nilai_dx = self.nilai_x2 - self.nilai_x1
        self.nilai_dy = self.nilai_y2 - self.nilai_y1
        print(f"nilai dx dan dy = {self.nilai_dx} dan {self.nilai_dy}")
        print(f"gradien = {self.nilai_gradien}")

        if(self.nilai_gradien < 1 and self.nilai_gradien > 0): #jika m-> 0 < m < 1
            '''
            jika m --> 0 < m < 1
            d1 = 2*dy
            d2 = 2*(dx-dy)
            p = d1-dx

            jika p = 0
            p = p-d2
            y = y+1

            jika p < 0
            p = p + d1
            y = y

            x di increment +1
            '''
            #rumus awal
            self.nilai_d1 = 2 * self.nilai_dy
            self.nilai_d2 = 2*(self.nilai_dx - self.nilai_dy)
            self.nilai_p = self.nilai_d1 - self.nilai_d2
            self.array_p = [self.nilai_p]
            print(f"nilai d1 dan d2 = {self.nilai_d1} dan {self.nilai_d2}")
            print(f"nilai p = {self.nilai_p}")

            #perulangan perhitungan
            for indeks in range(int(self.nilai_dx)):
                if self.nilai_p >= 0: #jika p >= 0
                    self.nilai_p = self.nilai_p-self.nilai_d2
                    self.nilai_y1 = self.nilai_y1 + 1

                else: #jika p < 0
                    self.nilai_p = self.nilai_p + self.nilai_d1
                
                self.nilai_x1 = self.nilai_x1 + 1
                
                #incement x
                self.array_x.append(self.nilai_x1)
                self.array_y.append(self.nilai_y1)
                self.array_p.append(self.nilai_p)
        
        else:
            '''
            d1 = 2*dx
            d2 = 2*(dx-dy)
            p = d1-dy

            jika p >= 0
            p = p+d2
            x = x+1

            jika p<0
            p = p+d1
            x = x

            y diincrement kan 1
            '''
            #rumus
            self.nilai_d1 = 2*self.nilai_dx
            self.nilai_d2 = 2*(self.nilai_dx-self.nilai_dy)
            self.nilai_p = self.nilai_d1 - self.nilai_dy
            self.array_p = [self.nilai_p]
            print(f"nilai d1 dan d2 = {self.nilai_d1} dan {self.nilai_d2}")
            print(f"nilai p = {self.nilai_p}")

            #perulangan perhitungan
            for indeks in range(int(self.nilai_dy)):
                if self.nilai_p >= 0: #jika p >= 0
                    self.nilai_p = self.nilai_p+self.nilai_d2
                    self.nilai_x1 = self.nilai_x1 + 1

                else: #jika p < 0
                    self.nilai_p = self.nilai_p + self.nilai_d1

                self.nilai_y1 = self.nilai_y1 + 1
                
                #incement x
                self.array_x.append(self.nilai_x1)
                self.array_y.append(self.nilai_y1)
                self.array_p.append(self.nilai_p)

        print("perhitungan selesai")
    
    def show(self):
        #cek dulu apakah sempat memiror atau tidak
        if self.nilai_mirror :
            for indeks in range((len(self.array_y))-1):
                self.array_y[indeks+1] = self.array_y[indeks+1] - (2*(self.array_y[indeks+1] - self.array_y[0]))

        #mengintegerkan array
        for indeks in range(len(self.array_x)):
            self.array_x[indeks] = int(self.array_x[indeks])
            self.array_y[indeks] = int(self.array_y[indeks])

        print(f"nilai x = {self.array_x}")
        print(f"nilai y = {self.array_y}")
        print(f"nilai p = {self.array_p}")
        print("menampilkan tabel")

        # Menambahkan judul dan label sumbu
        plt.figure(2)
        plt.suptitle("Algoritma Bresenham | Aditya Difa 123210085")
        plt.title('Plot Scatter dari Array x dan y')
        plt.xlabel('Nilai x')
        plt.ylabel('Nilai y')

        #menambahkan grid
        plt.grid(True)

        # bikin garis
        plt.scatter(self.array_x, self.array_y, color='red', marker='o', s=300)

        # Menampilkan plot
        plt.show()