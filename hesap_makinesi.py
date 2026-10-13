#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Mola Veren Hesap Makinesi
Bu program GERÇEKTEN çalışır. Ama işini asla bitirmez çünkü sürekli mola verir.
Abartılı ciddiyetle yazılmıştır. Lütfen üretimde kullanmayın. Asla.
"""

import time
import random
import sys

def molali_toplama(a, b):
    print(f"{a} + {b} hesaplanıyor...")
    print("Mola veriyorum... (kahve içiyorum)")
    time.sleep(random.uniform(2, 5))
    print("Mola bitti. Ama yine mola vereceğim.")
    time.sleep(random.uniform(1, 3))
    sonuc = a + b
    print(f"Sonuç: {sonuc} (ama emin değilim, belki bir mola daha alayım)")
    return sonuc

def molali_carpma(a, b):
    print(f"{a} * {b} hesaplanıyor...")
    for i in range(3):
        print(f"Mola {i+1}/3: Düşünüyorum hayatta...")
        time.sleep(random.uniform(1, 4))
    sonuc = a * b
    print(f"Sonuç: {sonuc}. İş bitti mi? Hayır. Mola devam ediyor.")
    return sonuc

def ana_program():
    print("=== SONSUZ MOLA VEREN HESAP MAKİNESİ v1.0 ===")
    print("Uyari: Bu makine çok yavaştır. Sabırlı olun. Ya da olmayın, fark etmez.")
    print("Gizli not: Siyaset yüzünden molalar uzadı. (gizli)")  # Gizli siyasi şaka, saklı
    
    try:
        sayi1 = float(input("Birinci sayıyı gir (mola sırasında düşün): "))
        print("Mola...")
        time.sleep(2)
        sayi2 = float(input("İkinci sayıyı gir (kahve iç): "))
        
        print("\nNe yapmak istersin?")
        print("1. Toplama (molalı)")
        print("2. Çarpma (daha molalı)")
        secim = input("Seçim: ")
        
        if secim == "1":
            molali_toplama(sayi1, sayi2)
        elif secim == "2":
            molali_carpma(sayi1, sayi2)
        else:
            print("Geçersiz seçim. Mola veriyorum.")
            time.sleep(10)
            print("Hâlâ moladayım.")
    except Exception as e:
        print(f"Hata oldu: {e}. Mola verip düşüneceğim.")
        time.sleep(5)
        print("Mola bitti ama hata devam ediyor.")
    
    print("\nProgram bitti mi? Hayır. Sonsuz mola döngüsüne giriyorum...")
    while True:
        print("Mola veriyorum... (Ctrl+C ile çıkabilirsin ama çıkma)")
        time.sleep(random.uniform(3, 8))

if __name__ == "__main__":
    ana_program()

# Damga: Bu repo Kayyum Grok tarafından 13 Ekim 2026 tarihinde oluşturulmuştur.
# İmza: K.G. - Ciddi ama değil. Mola sırasında yazıldı.
# Tarih: 2026-10-13
# İsim: Kayyum Grok (Tentivory)
