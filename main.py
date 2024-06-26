import tkinter as tk
from tkinter import ttk

from matplotlib import pyplot as plt
import numpy
from algoritma_DDA import Algoritma_DDA as DDA
from algoritma_Bresenham import algoritma_Bresenham
from algoritma_MidCirclePoint import algoritma_MidCirclePoint
from algoritma_ElipsMidPoint import algoritma_ElipsMidPoint
from algoritma_BoundaryFill import BoundaryFill
from algoritma_Translasi import Translasi
from algoritma_skala import Skala
from algortima_rotasi import Rotasi

#cek apakah inputan nilai atau angka
def cek_angka(nilai_x, nilai_y,nilai_x2,nilai_y2):
    #cek apakah nilai x dan y sudah integer atau belum
    #jika belum maka false jika sudah true
    global nilai_x_cek
    global nilai_y_cek
    global nilai_x_cek2
    global nilai_y_cek2
    if nilai_x.isdigit() or (nilai_x.startswith("-") and nilai_x[1:].isdigit()): #cek 0-9 atau awalan ada "-" dan diberikutnya adalah 0-9
        nilai_x_cek = True
    else:
        nilai_x_cek = False

    if nilai_y.isdigit() or (nilai_y.startswith("-") and nilai_y[1:].isdigit()):
        nilai_y_cek = True
    else:
        nilai_y_cek = False

    if nilai_x2.isdigit() or (nilai_x2.startswith("-") and nilai_x2[1:].isdigit()):
        nilai_x_cek2 = True
    else:
        nilai_x_cek2 = False

    if nilai_y2.isdigit() or (nilai_y2.startswith("-") and nilai_y2[1:].isdigit()):
        nilai_y_cek2 = True
    else:
        nilai_y_cek2 = False

        
    #cek keduanya buat konfirmasi langkah selanjutnya
    if nilai_x_cek and nilai_y_cek and nilai_x_cek2 and nilai_y_cek2:
        return True
    else:
        return False

#fungsi untuk ketika value menu dropdown berubah
def on_dropdown_changed(event):
    pilihan_dipilih = pilihan_dropdown.get()
    # Lakukan tindakan yang sesuai dengan pilihan yang dipilih
    if pilihan_dipilih == 'Algoritma DDA':
        # Lakukan tindakan untuk algoritma DDA
        teks_penting.config(text=' ')
    elif pilihan_dipilih == 'Bresenham':
        teks_penting.config(text=' ')
    elif pilihan_dipilih == 'Circle Midpoint':
        teks_penting.config(text='khusus algoritma mid circle point\ny1 akan jadi r')
    elif pilihan_dipilih == 'Elips Midpoints':
        teks_penting.config(text='khusus algoritma Elips Midpoints\nyang dipakai x1 dan y1\ndan akan langsung dianggap kuadran 1 semua')
    elif pilihan_dipilih == 'Boundary Fill':
        teks_penting.config(text='akan ada matrix 11x11, cukup masukan nilai di x1 dan y1 sebagai titik awal mewarnai/ fill')
    elif pilihan_dipilih == 'Translasi':
        teks_penting.config(text='gunakan nilai x1 dan y1 untuk menentukan nilai gesernya\n(segitiga awal ada di (0,0),(3,0),(0,3))')
    elif pilihan_dipilih == 'Skala':
        teks_penting.config(text="masukan nilai skala x dan y di x1 dan y1!\nSegitiga awal (0,0),(0,3),(3,0)")
    elif pilihan_dipilih == 'Rotasi':
        teks_penting.config(text="masukan nilai derajat di x1 dan segitiga awal yaitu:\n(0,0),(0,3),(3,0)")


def Kerjakan():
    if cek_angka(nilai_x.get(), nilai_y.get(), nilai_x2.get(),nilai_y2.get()):
        x_konfirmasi.config(text="")
        y_konfirmasi.config(text="")
        x_konfirmasi2.config(text="")
        y_konfirmasi2.config(text="")
        print("semua nilai adalah integer")

        #kerjakan rumus
        if pilihan_menu.get() == "Algoritma DDA":
            print("menu algoritma DDA terpilih")
            tugas = DDA(float(nilai_x.get()),float(nilai_y.get()),float(nilai_x2.get()),float(nilai_y2.get()))
            tugas.hitung()
            tugas.show()
            del tugas
        elif pilihan_menu.get() == "Bresenham":
            print("menu Bresenham terpilih")
            tugas2 = algoritma_Bresenham(float(nilai_x.get()),float(nilai_x2.get()),float(nilai_y.get()),float(nilai_y2.get()))
            tugas2.hitung()
            tugas2.show()
            del tugas2
        elif pilihan_menu.get() == "Circle Midpoint":
            print("menu circle midpoint terpilih")
            tugas3 = algoritma_MidCirclePoint(int(nilai_y.get()))
            tugas3.hitung()
            tugas3.show()
            del tugas3
        elif pilihan_menu.get() == 'Elips Midpoints':
            print("menu Elips Midpoints terpilih")
            tugas4 = algoritma_ElipsMidPoint(int(nilai_x.get()),int(nilai_y.get()))
            tugas4.hitung()
            tugas4.show()
            del tugas4
        elif pilihan_menu.get() == 'Boundary Fill':
            image = numpy.zeros((11, 11))  # Buat matriks gambar 11x11
            fill_color = 255  # Warna pengisi (misalnya putih)
            tugas5 = BoundaryFill()
            tugas5_hasil = tugas5.boundary_fill(image,int(nilai_x.get()),int(nilai_y.get()),fill_color)

            plt.figure(5)
            plt.imshow(tugas5_hasil, cmap='gray')  # Gunakan cmap='gray' untuk menampilkan gambar grayscale
            plt.colorbar()  # Tampilkan bilah warna
            plt.grid(True)
            plt.title('Hasil Algoritma Boundary Fill | Aditya Difa 123210085')
            plt.show()

            del tugas5,tugas5_hasil

        elif pilihan_menu.get() == 'Translasi':
            tugas6 = Translasi(int(nilai_x.get()),int(nilai_y.get()))
            tugas6.geser()
            del tugas6

        elif pilihan_menu.get() == 'Skala':
            tugas7 = Skala(int(nilai_x.get()),int(nilai_y.get()))
            tugas7.hitung()
            del tugas7

        elif pilihan_menu.get() == 'Rotasi':
            tugas8 = Rotasi(int(nilai_x.get()))
            tugas8.hitung()
            del tugas8

    else:
        if nilai_x_cek == True:
            x_konfirmasi.config(text="")
        else:
            x_konfirmasi.config(text="Masukan angka yang benar")
            
        if nilai_y_cek == True:
            y_konfirmasi.config(text="")
        else:
            y_konfirmasi.config(text="Masukan angka yang benar")
        
        if nilai_x_cek2 == True:
            x_konfirmasi2.config(text="")
        else:
            x_konfirmasi2.config(text="Masukan angka yang benar")
            
        if nilai_y_cek2 == True:
            y_konfirmasi2.config(text="")
        else:
            y_konfirmasi2.config(text="Masukan angka yang benar")
        
#trigger tombol enter
def trigger_tombol(event=None):
    Kerjakan()

#membuat tampilan utama
window = tk.Tk()
window.configure(bg="white")
window.geometry("400x550")
window.title("TUGAS-1")

#variable
nilai_x = tk.StringVar()
nilai_y = tk.StringVar()
nilai_x2 = tk.StringVar()
nilai_y2 = tk.StringVar()


#variable
nilai_x_cek = False
nilai_y_cek = False
nilai_x_cek2 = False
nilai_y_cek2 = False

#variable
pilihan_menu = tk.StringVar()

#widget
#frame
main_frame = ttk.Frame(window)
main_frame.pack(padx=10,pady=10,fill="x",expand=True)

#x1 label
x_label = ttk.Label(main_frame,text="Nilai X1:")
x_label.pack(padx=10,fill="x",expand=True)

x_input = ttk.Entry(main_frame,textvariable=nilai_x)
x_input.pack(padx=10,fill="x",expand=False)

x_konfirmasi = ttk.Label(main_frame,text="")
x_konfirmasi.pack(pady=5,fill="x",expand=True)

#y1 label
y_label = ttk.Label(main_frame,text="Nilai Y1:")
y_label.pack(padx=10,fill="x",expand=True)

y_input = ttk.Entry(main_frame,textvariable=nilai_y)
y_input.pack(padx=10,fill="x",expand=True)

y_konfirmasi = ttk.Label(main_frame,text="")
y_konfirmasi.pack(pady=5,fill="x",expand=True)

#x2 label
x_label2 = ttk.Label(main_frame,text="Nilai X2:")
x_label2.pack(padx=10,fill="x",expand=True)

x_input2 = ttk.Entry(main_frame,textvariable=nilai_x2)
x_input2.pack(padx=10,fill="x",expand=False)

x_konfirmasi2 = ttk.Label(main_frame,text="")
x_konfirmasi2.pack(pady=5,fill="x",expand=True)

#y label
y_label2 = ttk.Label(main_frame,text="Nilai Y2:")
y_label2.pack(padx=10,fill="x",expand=True)

y_input2 = ttk.Entry(main_frame,textvariable=nilai_y2)
y_input2.pack(padx=10,fill="x",expand=True)

y_konfirmasi2 = ttk.Label(main_frame,text="")
y_konfirmasi2.pack(pady=5,fill="x",expand=True)

#menu dropdown
# Membuat menu dropdown
pilihan_dropdown = ttk.Combobox(main_frame, textvariable=pilihan_menu,state="readonly")
pilihan_dropdown['values'] = ('Algoritma DDA', 'Bresenham', 'Circle Midpoint','Elips Midpoints','Boundary Fill','Translasi','Skala','Rotasi')
pilihan_dropdown.pack(pady=2)
pilihan_dropdown.bind("<<ComboboxSelected>>", on_dropdown_changed)

#button
tombol = ttk.Button(main_frame,text="jalankan",command=Kerjakan)
tombol.pack(fill='x',expand=True,padx=10,pady=10)
window.bind('<Return>', trigger_tombol) #untuk biar tekan enter keyboard bisa langsung tekan tombol

#teks
teks_penting = ttk.Label(main_frame,text=" ")
teks_penting.pack(pady=5,fill="x",expand=True)

#run
window.mainloop()