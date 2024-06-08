import tkinter as tk
from tkinter import ttk
from algoritma_DDA import Algoritma_DDA as DDA
from algoritma_Bresenham import algoritma_Bresenham
from algoritma_MidCirclePoint import algoritma_MidCirclePoint

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
pilihan_dropdown['values'] = ('Algoritma DDA', 'Bresenham', 'Circle Midpoint')
pilihan_dropdown.pack(pady=2)

#button
tombol = ttk.Button(main_frame,text="jalankan",command=Kerjakan)
tombol.pack(fill='x',expand=True,padx=10,pady=10)
window.bind('<Return>', trigger_tombol) #untuk biar tekan enter keyboard bisa langsung tekan tombol

#teks
teks = ttk.Label(main_frame,text="khusus algoritma mid circle point\ny1 akan jadi r")
teks.pack(pady=5,fill="x",expand=True)

#run
window.mainloop()