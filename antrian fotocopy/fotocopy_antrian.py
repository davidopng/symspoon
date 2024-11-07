from collections import deque
import tkinter as tk
from tkinter import messagebox

class FotocopyService:
    def __init__(self):
        self.antrian = deque()
        self.riwayat = []

    def daftarkan_customer(self, nama):
        self.antrian.append(nama)
        print(f"Customer {nama} telah didaftarkan ke antrian.")

    def layani_customer(self):
        if self.antrian:
            customer = self.antrian.popleft()
            self.riwayat.append(customer)
            print(f"Customer {customer} sedang dilayani.")
        else:
            print("Tidak ada customer dalam antrian.")

    def lihat_antrian(self):
        return list(self.antrian)

    def lihat_riwayat(self):
        return self.riwayat

class FotocopyApp:
    def __init__(self, root, service):
        self.root = root
        self.service = service
        self.root.title("Manajemen Antrian Fotocopy di Ibaraki")
        
        self.label = tk.Label(root, text="Nama Customer:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.daftar_button = tk.Button(root, text="Daftarkan Customer", command=self.daftarkan_customer)
        self.daftar_button.pack()
        
        self.layani_button = tk.Button(root, text="Layani Customer", command=self.layani_customer)
        self.layani_button.pack()
        
        self.antrian_button = tk.Button(root, text="Lihat Antrian", command=self.lihat_antrian)
        self.antrian_button.pack()
        
        self.riwayat_button = tk.Button(root, text="Lihat Riwayat", command=self.lihat_riwayat)
        self.riwayat_button.pack()
        
        self.output = tk.Text(root, height=10, width=50)
        self.output.pack()
        
    def daftarkan_customer(self):
        nama = self.entry.get()
        if nama:
            self.service.daftarkan_customer(nama)
            messagebox.showinfo("Info", f"Customer {nama} telah didaftarkan.")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Nama customer tidak boleh kosong!")
    
    def layani_customer(self):
        self.service.layani_customer()
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, "Customer sedang dilayani.\n")
        
    def lihat_antrian(self):
        antrian = self.service.lihat_antrian()
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, "Antrian Customer:\n" + "\n".join(antrian))
    
    def lihat_riwayat(self):
        riwayat = self.service.lihat_riwayat()
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, "Riwayat Customer:\n" + "\n".join(riwayat))

if __name__ == "__main__":
    service = FotocopyService()
    root = tk.Tk()
    app = FotocopyApp(root, service)
    root.mainloop()

class FotocopyService:
    def __init__(self):
        self.antrian = deque()
        self.riwayat = []

    def daftarkan_customer(self, nama):
        self.antrian.append(nama)
        print(f"Customer {nama} telah didaftarkan ke antrian.")

    def layani_customer(self):
        if self.antrian:
            customer = self.antrian.popleft()
            self.riwayat.append(customer)
            print(f"Customer {customer} sedang dilayani.")
        else:
            print("Tidak ada customer dalam antrian.")

    def lihat_antrian(self):
        return list(self.antrian)

    def lihat_riwayat(self):
        return self.riwayat

class FotocopyApp:
    def __init__(self, root, service):
        self.root = root
        self.service = service
        self.root.title("Manajemen Antrian Fotocopy di Ibaraki")
        
        self.label = tk.Label(root, text="Nama Customer:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.daftar_button = tk.Button(root, text="Daftarkan Customer", command=self.daftarkan_customer)
        self.daftar_button.pack()
        
        self.layani_button = tk.Button(root, text="Layani Customer", command=self.layani_customer)
        self.layani_button.pack()
        
        self.antrian_button = tk.Button(root, text="Lihat Antrian", command=self.lihat_antrian)
        self.antrian_button.pack()
        
        self.riwayat_button = tk.Button(root, text="Lihat Riwayat", command=self.lihat_riwayat)
        self.riwayat_button.pack()
        
        self.output = tk.Text(root, height=10, width=50)
        self.output.pack()
        
    def daftarkan_customer(self):
        nama = self.entry.get()
        if nama:
            self.service.daftarkan_customer(nama)
            messagebox.showinfo("Info", f"Customer {nama} telah didaftarkan.")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Nama customer tidak boleh kosong!")
    
    def layani_customer(self):
        self.service.layani_customer()
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, "Customer sedang dilayani.\n")
        
    def lihat_antrian(self):
        antrian = self.service.lihat_antrian()
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, "Antrian Customer:\n" + "\n".join(antrian))
    
    def lihat_riwayat(self):
        riwayat = self.service.lihat_riwayat()
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, "Riwayat Customer:\n" + "\n".join(riwayat))

if __name__ == "__main__":
    service = FotocopyService()
    root = tk.Tk()
    app = FotocopyApp(root, service)
    root.mainloop()
