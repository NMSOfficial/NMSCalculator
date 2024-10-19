import tkinter as tk
import math

class NMSCalculator:
    def __init__(self, ana_pencere):
        self.ana_pencere = ana_pencere
        self.ana_pencere.title("NMSCalculator")
        self.ana_pencere.geometry("400x500")
        
        self.formül = ""
        self.girdi_değeri = tk.StringVar()

        self.butonlar()

    def butonlar(self):
        giriş = tk.Entry(self.ana_pencere, textvariable=self.girdi_değeri, font=("Bahnschrift", 18), bd=10, insertwidth=4, width=14, borderwidth=4)
        giriş.grid(row=0, column=0, columnspan=4)

        butonlar = [
            ('7', 1, 0, '#FFDDC1'), ('8', 1, 1, '#FFABAB'), ('9', 1, 2, '#FFC3A0'), ('/', 1, 3, '#D5AAFF'),
            ('4', 2, 0, '#85E3FF'), ('5', 2, 1, '#B9FBC0'), ('6', 2, 2, '#FF677D'), ('*', 2, 3, '#D9BF77'),
            ('1', 3, 0, '#F6D6A9'), ('2', 3, 1, '#FF677D'), ('3', 3, 2, '#FFABAB'), ('-', 3, 3, '#D5AAFF'),
            ('0', 4, 0, '#FFDDC1'), ('.', 4, 1, '#B9FBC0'), ('+', 4, 2, '#85E3FF'), ('=', 4, 3, '#FFC3A0'),
            ('√', 5, 0, '#FFD700'), ('Asal', 5, 1, '#FF6F61'), ('C', 5, 2, '#FF6F61'),
        ]

        for (metin, satır, sütun, renk) in butonlar:
            self.buton_oluştur(metin, satır, sütun, renk)

    def buton_oluştur(self, metin, satır, sütun, renk):
        buton = tk.Button(self.ana_pencere, text=metin, padx=20, pady=20, command=lambda: self.buton_tıkla(metin), font=("Bahnschrift", 18), bg=renk)
        buton.grid(row=satır, column=sütun)

    def buton_tıkla(self, karakter):
        if karakter == '=':
            self.hesapla()
        elif karakter == '√':
            self.karekök()
        elif karakter == 'Asal':
            self.asal_kontrol()
        elif karakter == 'C':
            self.temizle()
        else:
            self.formül += str(karakter)
            self.girdi_değeri.set(self.formül)

    def hesapla(self):
        try:
            sonuç = str(eval(self.formül))
            self.girdi_değeri.set(sonuç)
            self.formül = ""
        except:
            self.girdi_değeri.set("Hata")
            self.formül = ""

    def karekök(self):
        try:
            sonuç = str(math.sqrt(float(self.formül)))
            self.girdi_değeri.set(sonuç)
            self.formül = ""
        except:
            self.girdi_değeri.set("Hata")
            self.formül = ""

    def asal_kontrol(self):
        try:
            sayı = int(self.formül)
            if sayı < 2:
                self.girdi_değeri.set("Asal Değil")
            else:
                asal = all(sayı % i != 0 for i in range(2, int(math.sqrt(sayı)) + 1))
                self.girdi_değeri.set("Asal" if asal else "Asal Değil")
            self.formül = ""
        except:
            self.girdi_değeri.set("Hata")
            self.formül = ""

    def temizle(self):
        self.formül = ""
        self.girdi_değeri.set("")

if __name__ == "__main__":
    ana_pencere = tk.Tk()
    uygulama = NMSCalculator(ana_pencere)
    ana_pencere.mainloop()
