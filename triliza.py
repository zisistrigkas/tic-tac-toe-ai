import tkinter as tk
import math

class TrilizaPoyDenXanei:
    def __init__(self):
        self.parathyro = tk.Tk()
        self.parathyro.title("Ultimate Tic-Tac-Toe")
        self.parathyro.geometry("400x550")
        self.parathyro.configure(bg="#121212") # Πολύ σκοτεινό background

        self.paizei_to_pc = False
        self.tamplo = [" " for _ in range(9)]
        self.koympia = []

        # Header
        self.status_label = tk.Label(self.parathyro, text="Η σειρά σου (X)", font=('Montserrat', 18, 'bold'), 
                                     bg="#121212", fg="#00e5ff")
        self.status_label.pack(pady=20)

        # Πλέγμα
        self.frame = tk.Frame(self.parathyro, bg="#121212")
        self.frame.pack()

        self.dimioyrgia_grafikon()

        # Κουμπί Restart (μοντέρνο)
        self.restart_btn = tk.Button(self.parathyro, text="RESTART", font=('Montserrat', 12, 'bold'),
                                     bg="#00e5ff", fg="#121212", activebackground="#00b8d4",
                                     relief="flat", cursor="hand2", command=self.epanekkinisi)
        self.restart_btn.pack(pady=30, ipadx=20)

    def dimioyrgia_grafikon(self):
        for i in range(9):
            koympi = tk.Button(self.frame, text=" ", font=('Montserrat', 24, 'bold'), 
                               width=4, height=2, bg="#1e1e1e", fg="white",
                               activebackground="#333333", relief="flat", cursor="hand2")
            koympi.grid(row=i//3, column=i%3, padx=5, pady=5)
            koympi.config(command=lambda i=i: self.kinisi_paikti(i))
            self.koympia.append(koympi)

    def epanekkinisi(self):
        self.tamplo = [" " for _ in range(9)]
        self.paizei_to_pc = False
        self.status_label.config(text="Η σειρά σου (X)", fg="#00e5ff")
        for k in self.koympia:
            k.config(text=" ", bg="#1e1e1e", state="normal")

    def elegxos_nikiti(self, t):
        grammes = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for g in grammes:
            if t[g[0]] == t[g[1]] == t[g[2]] != " ": return t[g[0]], g
        if " " not in t: return "Isopalia", None
        return None, None

    def minimax(self, t, is_ai):
        res, _ = self.elegxos_nikiti(t)
        if res == "X": return -10
        if res == "O": return 10
        if res == "Isopalia": return 0
        if is_ai:
            best = -math.inf
            for i in range(9):
                if t[i] == " ":
                    t[i] = "O"
                    best = max(best, self.minimax(t, False))
                    t[i] = " "
            return best
        else:
            best = math.inf
            for i in range(9):
                if t[i] == " ":
                    t[i] = "X"
                    best = min(best, self.minimax(t, True))
                    t[i] = " "
            return best

    def kinisi_paikti(self, i):
        if self.paizei_to_pc or self.tamplo[i] != " ": return
        self.tamplo[i] = "X"
        self.koympia[i].config(text="X", fg="#00e5ff")
        res, grammi = self.elegxos_nikiti(self.tamplo)
        if res: self.telos_paixnidioy(res, grammi)
        else:
            self.paizei_to_pc = True
            self.status_label.config(text="Σκέφτομαι...", fg="#ff007f")
            self.parathyro.after(500, self.kinisi_ypologisti)

    def kinisi_ypologisti(self):
        best = -math.inf
        move = None
        for i in range(9):
            if self.tamplo[i] == " ":
                self.tamplo[i] = "O"
                score = self.minimax(self.tamplo, False)
                self.tamplo[i] = " "
                if score > best:
                    best = score
                    move = i
        if move is not None:
            self.tamplo[move] = "O"
            self.koympia[move].config(text="O", fg="#ff007f")
        self.paizei_to_pc = False
        self.status_label.config(text="Η σειρά σου (X)", fg="#00e5ff")
        res, grammi = self.elegxos_nikiti(self.tamplo)
        if res: self.telos_paixnidioy(res, grammi)

    def telos_paixnidioy(self, res, grammi):
        for k in self.koympia: k.config(state="disabled")
        if res == "Isopalia": self.status_label.config(text="Ισοπαλία!", fg="white")
        else:
            self.status_label.config(text=f"Νικητής: {res}!", fg="#ffea00")
            if grammi:
                for i in grammi: self.koympia[i].config(bg="#333333")

if __name__ == "__main__":
    app = TrilizaPoyDenXanei()
    app.parathyro.mainloop()