from collections import deque
import tkinter as tk
from tkinter import messagebox

class Klinik:
    def __init__(self):
        self.antrian = deque()
        self.riwayat = []

    def daftarkan_pasien(self, nama):
        self.antrian.append(nama)
        print(f"Pasien {nama} telah didaftarkan ke antrian.")

    def layani_pasien(self):
        if self.antrian:
            pasien = self.antrian.popleft()
            self.riwayat.append(pasien)
            print(f"Pasien {pasien} sedang dilayani.")
        else:
            print("Tidak ada pasien dalam antrian.")

    def lihat_antrian(self):
        return list(self.antrian)

    def lihat_riwayat(self):
        return self.riwayat

class KlinikApp:
    def __init__(self, root, klinik):
        self.root = root
        self.klinik = klinik
        self.root.title("Manajemen Antrian Klinik")
        
        self.label = tk.Label(root, text="Nama Pasien:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.daftar_button = tk.Button(root, text="Daftarkan Pasien", command=self.daftarkan_pasien)
        self.daftar_button.pack()
        
        self.layani_button = tk.Button(root, text="Layani Pasien", command=self.layani_pasien)
        self.layani_button.pack()
        
        self.antrian_button = tk.Button(root, text="Lihat Antrian", command=self.lihat_antrian)
        self.antrian_button.pack()
        
        self.riwayat_button = tk.Button(root, text="Lihat Riwayat", command=self.lihat_riwayat)
        self.riwayat_button.pack()
        
        self.output = tk.Text(root, height=10, width=50)
        self.output.pack()
        
    def daftarkan_pasien(self):
        nama = self.entry.get()
        if nama:
            self.klinik.daftarkan_pasien(nama)
            messagebox.showinfo("Info", f"Pasien {nama} telah didaftarkan.")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Nama pasien tidak boleh kosong!")
    
    def layani_pasien(self):
        self.klinik.layani_pasien()
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, "Pasien sedang dilayani.\n")
        
    def lihat_antrian(self):
        antrian = self.klinik.lihat_antrian()
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, "Antrian Pasien:\n" + "\n".join(antrian))
    
    def lihat_riwayat(self):
        riwayat = self.klinik.lihat_riwayat()
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, "Riwayat Pasien:\n" + "\n".join(riwayat))

if __name__ == "__main__":
    klinik = Klinik()
    root = tk.Tk()
    app = KlinikApp(root, klinik)
    root.mainloop()
