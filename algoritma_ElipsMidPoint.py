import math
import matplotlib.pyplot as plt

class algoritma_ElipsMidPoint:
    k = 0
    parameter_temp = 0
    x_array2 = []
    y_array2 = []

    def __init__(self, x_1, y_1):
        #di abselut agar bisa kuadran satu
        self.x_1 = abs(x_1)
        self.y_1 = abs(y_1)
        self.x_array = [0]
        self.y_array = [self.y_1]
        self.x_tambah1 = 0
        self.y_tambah1 = self.y_1
    
    def hitung(self):
        #FASE 1
        # parameter_awal = self.kuadran(self.y_1)-(self.kuadran(self.x_1)*self.y_1) + ((1/4)*self.kuadran(self.x_1))
        parameter_awal = self.y_1**2 - self.x_1**2 * self.y_1 + (1/4) * self.x_1**2
        parameter_temp = parameter_awal
        
        while not(2*self.y_1**2 *self.x_tambah1 > 2*self.x_1**2 *self.y_tambah1):
            if(parameter_temp < 0):
                self.x_tambah1 = self.x_tambah1 + 1
                self.x_array.append(self.x_tambah1)
                self.y_array.append(self.y_tambah1)
                parameter_temp = parameter_temp + (2*self.y_1**2 *self.x_tambah1) + self.y_1** 2
                print(f'parameter = {parameter_temp}, [{self.x_tambah1},{self.y_tambah1}]')

            else:
                self.x_tambah1 = self.x_tambah1 + 1
                self.y_tambah1 = self.y_tambah1 - 1
                self.x_array.append(self.x_tambah1)
                self.y_array.append(self.y_tambah1)
                parameter_temp = parameter_temp + (2*self.y_1**2 *self.x_tambah1) - (2*self.x_1**2 *self.y_tambah1) + self.y_1**2
                print(f'parameter = {parameter_temp}, [{self.x_tambah1},{self.y_tambah1}]')

        print(self.x_array)
        print(self.y_array)
        print("==========FASE 2==============")
        #FASE 2
        self.x_array2.append(self.x_array[-1])
        self.y_array2.append(self.y_array[-1])
        self.x_tambah1 = self.x_array[-1]
        self.y_tambah1 = self.y_array[-1]

        parameter_awal = self.y_1**2 * (self.x_array2[0] + (1/2))**2 + self.x_1**2 * (self.y_array2[0]-1)**2 - self.x_1**2 * self.y_1**2
        parameter_temp = parameter_awal

        while not(self.y_tambah1 <= 0):
            if(parameter_temp > 0):
                self.y_tambah1 = self.y_tambah1 - 1
                self.x_array2.append(self.x_tambah1)
                self.y_array2.append(self.y_tambah1)

                parameter_temp = parameter_temp - 2*self.x_1**2 * self.y_tambah1 + self.x_1**2
                print(f'parameter = {parameter_temp}, [{self.x_tambah1},{self.y_tambah1}]')
            else:
                self.x_tambah1 = self.x_tambah1 + 1
                self.y_tambah1 = self.y_tambah1 - 1
                self.x_array2.append(self.x_tambah1)
                self.y_array2.append(self.y_tambah1)
                parameter_temp = parameter_temp + 2*self.y_1**2 * self.x_tambah1 - 2*self.x_1**2*self.y_tambah1 + self.x_1**2
                print(f'parameter = {parameter_temp}, [{self.x_tambah1},{self.y_tambah1}]')

        print(self.x_array2)
        print(self.y_array2)

    def show(self):
        plt.figure(4)
        plt.suptitle("Algoritma ElipsMidPoints | Aditya Difa 123210085")
        plt.title('Plot Scatter dari Array x dan y')
        plt.xlabel('Nilai x')
        plt.ylabel('Nilai y')

        plt.grid(True)

        #bikin garis
        #kuadran 1
        plt.scatter(self.x_array, self.y_array, color="#ff0000", marker='o', s=300)
        plt.scatter(self.x_array2, self.y_array2, color="#b50000", marker='o', s=300)
        #kuadran 2
        plt.scatter(self.minuskan(self.x_array), self.y_array, color="#26ff00", marker='o', s=300)
        plt.scatter(self.minuskan(self.x_array2), self.y_array2, color="#1ec700", marker='o', s=300)
        #kuadran 3
        plt.scatter(self.x_array, self.minuskan(self.y_array), color="#00ffd5", marker='o', s=300)
        plt.scatter(self.x_array2, self.minuskan(self.y_array2), color="#00b597", marker='o', s=300)
        #kuadran 4
        plt.scatter(self.minuskan(self.x_array), self.minuskan(self.y_array), color="#ffff00", marker='o', s=300)
        plt.scatter(self.minuskan(self.x_array2), self.minuskan(self.y_array2), color="#bfbf00", marker='o', s=300)

        plt.show()
    def minuskan(self, x):
        array_x = []
        for indeks in range(len(x)):
            array_x.append(x[indeks]* (-1))
    
        return array_x
