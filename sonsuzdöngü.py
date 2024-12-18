sayi = 60

while sayi > 30:
    if sayi % 2 == 0:
        print(sayi)
    sayi -= 1
    
    # Kullanıcıdan devam edip etmeme seçimi
    cevap = input("Devam etmek ister misiniz? (E/H): ").lower()
    if cevap != 'e':
        print("Döngü sonlandırıldı.")
        break
