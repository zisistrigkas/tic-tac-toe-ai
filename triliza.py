import tkinter as tk
from tkinter import messagebox
import math

class TrilizaPoyDenXanei:
    def __init__(self): # ΔΙΟΡΘΩΣΗ: __init__
        self.parathyro = tk.Tk()
        self.parathyro.title("Η Αήττητη Τρίλιζα μου")

        self.paizei_to_pc = False
        self.tamplo = [" " for _ in range(9)]
        self.koympia = []
        self.dimioyrgia_grafikon()

    def dimioyrgia_grafikon(self):
        for i in range(9):
            koympi = tk.Button(self.parathyro, text=" ", font=('Segoe UI', 24, 'bold'), 
                               width=5, height=2, bg="#1caaa0", fg="white",
                               activebackground="#168a82",
                               command=lambda i=i: self.kinisi_paikti(i))
            koympi.grid(row=i//3, column=i%3, sticky="nsew")
            self.koympia.append(koympi)

    def elegxos_nikiti(self, t):
        grammes_nikis = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for g in grammes_nikis:
            if t[g[0]] == t[g[1]] == t[g[2]] != " ":
                return t[g[0]]
        if " " not in t: 
            return "Isopalia"
        return None

    def minimax(self, t, einai_i_seira_toy_ai):
        skor_nikis = self.elegxos_nikiti(t)
        if skor_nikis == "X": return -10
        if skor_nikis == "O": return 10
        if skor_nikis == "Isopalia": return 0
        
        if einai_i_seira_toy_ai:
            kalytero_skor = -math.inf
            for i in range(9):
                if t[i] == " ":
                    t[i] = "O"
                    skor = self.minimax(t, False)
                    t[i] = " "
                    kalytero_skor = max(skor, kalytero_skor)
            return kalytero_skor
        else:
            kalytero_skor = math.inf
            for i in range(9):
                if t[i] == " ":
                    t[i] = "X"
                    skor = self.minimax(t, True)
                    t[i] = " "
                    kalytero_skor = min(skor, kalytero_skor)
            return kalytero_skor

    def kinisi_paikti(self, i):
        if self.paizei_to_pc or self.tamplo[i] != " " or self.elegxos_nikiti(self.tamplo):
            return
        
        self.tamplo[i] = "X"
        self.koympia[i].config(text="X", fg="#2b2b2b", bg="#f8f1d4")
        
        teliko_apotelesma = self.elegxos_nikiti(self.tamplo)
        if teliko_apotelesma:
            self.telos_paixnidioy(teliko_apotelesma)
            return
            
        self.paizei_to_pc = True
        self.parathyro.after(1000, self.kinisi_ypologisti)

    def kinisi_ypologisti(self):
        kalytero_skor = -math.inf
        thesi_kinisis = None
        
        for i in range(9):
            if self.tamplo[i] == " ":
                self.tamplo[i] = "O"
                skor = self.minimax(self.tamplo, False)
                self.tamplo[i] = " "
                if skor > kalytero_skor:
                    kalytero_skor = skor
                    thesi_kinisis = i
                    
        if thesi_kinisis is not None:
            self.tamplo[thesi_kinisis] = "O"
            self.koympia[thesi_kinisis].config(text="O", fg="#ef476f", bg="#ffffff")
            
        self.paizei_to_pc = False
        teliko_apotelesma = self.elegxos_nikiti(self.tamplo)
        if teliko_apotelesma:
            self.telos_paixnidioy(teliko_apotelesma)

    def telos_paixnidioy(self, apotelesma):
        if apotelesma == "Isopalia":
            minyma = "Καλό, αλλά δεν με νίκησες! Ισοπαλία."
        else:
            minyma = f"Νικητής ο {apotelesma}!"
            
        messagebox.showinfo("Τέλος Παιχνιδιού", minyma)
        self.parathyro.destroy()

if __name__ == "__main__": # ΔΙΟΡΘΩΣΗ: __name__ και __main__
    paixnidi = TrilizaPoyDenXanei()
    paixnidi.parathyro.mainloop()