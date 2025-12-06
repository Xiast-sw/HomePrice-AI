import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np

# Veriyi yükle ve modeli eğit
df = pd.read_csv("data/FatihEvFiyatları.csv", sep=";")
df['odasayi_binayasi'] = df['odasayisi'] * df['binayasi']

X = df[['alan', 'odasayisi', 'binayasi', 'odasayi_binayasi']]
y = df['fiyat']

rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)
rf_reg.fit(X, y)

# Tahmin fonksiyonu
def predict():
    try:
        alan = alan_entry.get()
        odasayisi = odasayisi_entry.get()
        binayasi = binayasi_entry.get()

        if not alan.replace('.', '', 1).isdigit() or not odasayisi.isdigit() or not binayasi.isdigit():
            raise ValueError("Lütfen geçerli sayılar giriniz.")
        
        alan = float(alan)
        odasayisi = int(odasayisi)
        binayasi = int(binayasi)
        
        fiyat_tahmin = rf_reg.predict([[alan, odasayisi, binayasi, odasayisi * binayasi]])
        messagebox.showinfo("Sonuç", f"Tahmin Edilen Fiyat: {fiyat_tahmin[0]:,.2f} TL")
    except ValueError as e:
        messagebox.showerror("Hata", str(e))

# Tkinter arayüzü
root = tk.Tk()
root.title("Ev Fiyatı Tahmin Aracı")
root.geometry("300x150")

# Girdi alanları
ttk.Label(root, text="Alan (m²):").grid(column=0, row=0, padx=10, pady=5)
alan_entry = ttk.Entry(root)
alan_entry.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(root, text="Oda Sayısı:").grid(column=0, row=1, padx=10, pady=5)
odasayisi_entry = ttk.Entry(root)
odasayisi_entry.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(root, text="Bina Yaşı:").grid(column=0, row=2, padx=10, pady=5)
binayasi_entry = ttk.Entry(root)
binayasi_entry.grid(column=1, row=2, padx=10, pady=5)

# Tahmin butonu
ttk.Button(root, text="Tahmin Et", command=predict).grid(column=0, row=3, columnspan=2, pady=10)

# Başlat
root.mainloop()
