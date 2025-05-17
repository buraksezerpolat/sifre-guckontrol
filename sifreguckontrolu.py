import tkinter as tk
from tkinter import ttk
import os
import re 
import hashlib
from datetime import datetime

salt = os.urandom(16)
salt_hex = salt.hex()

def kontrol_et():
    sifre = giris_kutusu.get()
    
    uzunluk = len(sifre) >= 8
    buyuk = bool(re.search(r"[A-Z]", sifre))
    kucuk = bool(re.search(r"[a-z]", sifre))
    sayi = bool(re.search(r"\d", sifre))
    ozel = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", sifre))

    puan = sum([uzunluk, buyuk, kucuk, sayi, ozel])

    if puan <= 2:
        sonuc_etiketi.config(text="Şifre Gücü: Zayıf", fg="red")
    elif puan == 3 or puan == 4:
        sonuc_etiketi.config(text="Şifre Gücü: Orta", fg="orange")
    else:
        sonuc_etiketi.config(text="Şifre Gücü: Güçlü", fg="green")

    kriter_etiketleri[0].config(text=f"{'✓' if uzunluk else '✗'} En az 8 karakter", fg="green" if uzunluk else "red")
    kriter_etiketleri[1].config(text=f"{'✓' if buyuk else '✗'} Büyük harf", fg="green" if buyuk else "red")
    kriter_etiketleri[2].config(text=f"{'✓' if kucuk else '✗'} Küçük harf", fg="green" if kucuk else "red")
    kriter_etiketleri[3].config(text=f"{'✓' if sayi else '✗'} Sayı", fg="green" if sayi else "red")
    kriter_etiketleri[4].config(text=f"{'✓' if ozel else '✗'} Özel karakter", fg="green" if ozel else "red")

    zaman_damgasi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sifre_hash = hashlib.sha256(salt + sifre.encode()).hexdigest()
    with open("sifre_log.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"[Tarih/Saat: {zaman_damgasi}]\n")
        dosya.write(f"Salt (hex): {salt_hex}\n")
        dosya.write(f"SHA-256 Hash (Salt + Şifre): {sifre_hash}\n")
        dosya.write(f"Şifre Gücü: {'Zayıf' if puan <= 2 else 'Orta' if puan <= 4 else 'Güçlü'}\n")
        dosya.write("Kriterler:\n")
        dosya.write(f" - En az 8 karakter: {'✓' if uzunluk else '✗'}\n")
        dosya.write(f" - Büyük harf: {'✓' if buyuk else '✗'}\n")
        dosya.write(f" - Küçük harf: {'✓' if kucuk else '✗'}\n")
        dosya.write(f" - Sayı: {'✓' if sayi else '✗'}\n")
        dosya.write(f" - Özel karakter: {'✓' if ozel else '✗'}\n")
        dosya.write("------\n")

pencere = tk.Tk()
pencere.title("🔐 Şifre Güç Kontrolü")
pencere.geometry("850x700")
pencere.configure(bg="#ecf0f1")

baslik = tk.Label(pencere, text="Şifre Güç Kontrolü", font=("Helvetica", 20, "bold"), bg="#ecf0f1", fg="#34495e")
baslik.pack(pady=20)

giris_frame = tk.Frame(pencere, bg="#ecf0f1")
giris_frame.pack(pady=10)

etiket = tk.Label(giris_frame, text="Şifrenizi Giriniz:", font=("Helvetica", 12), bg="#ecf0f1")
etiket.grid(row=0, column=0, padx=5)

giris_kutusu = tk.Entry(giris_frame, width=30, show="*", font=("Helvetica", 12))
giris_kutusu.grid(row=0, column=1, padx=5)

kontrol_butonu = tk.Button(pencere, text="Şifreyi Kontrol Et", font=("Helvetica", 12), bg="#3498db", fg="white", command=kontrol_et)
kontrol_butonu.pack(pady=10)

sonuc_etiketi = tk.Label(pencere, text="", font=("Helvetica", 14, "bold"), bg="#ecf0f1")
sonuc_etiketi.pack(pady=10)

kriter_etiketleri = []
for _ in range(5):
    etiket = tk.Label(pencere, text="", font=("Helvetica", 11), bg="#ecf0f1")
    etiket.pack(anchor="w", padx=40)
    kriter_etiketleri.append(etiket)


def loglari_goster():
    try:
        with open("sifre_log.txt", "r", encoding="utf-8") as dosya:
            icerik = dosya.read()
            log_goster_alani.delete("1.0", tk.END)
            log_goster_alani.insert(tk.END, icerik)
    except FileNotFoundError:
        log_goster_alani.delete("1.0", tk.END)
        log_goster_alani.insert(tk.END, "Henüz bir log dosyası oluşturulmamış.")

log_frame = tk.Frame(pencere, bg="#ecf0f1")
log_frame.pack(pady=10)

scrollbar = tk.Scrollbar(log_frame)
scrollbar.pack(side="right", fill="y")

log_goster_alani = tk.Text(log_frame, height=10, width=80, yscrollcommand=scrollbar.set, font=("Helvetica", 10))
log_goster_alani.pack(side="left")
scrollbar.config(command=log_goster_alani.yview)
log_butonu = tk.Button(pencere, text="Logları Göster", font=("Helvetica", 12), bg='#2c3e50', fg='white', command=lambda: loglari_goster())
log_butonu.pack(pady=10)

pencere.mainloop()