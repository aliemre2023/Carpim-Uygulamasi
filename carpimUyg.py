from random import randint

print("_" * 50)
print("Çarpma Uygulaması")
print("_" * 50)


print("""
Seviye seçin -
    1 - Kolay (1,6)
    2 - Orta (7,15)
    3 - Zor (16,25)
    (-1) - Programdan Çıkış
    
""")


while True: 
    svy = input("seçiminiz >> ")

    if svy == "1":
        a = 1
        b = 6
    elif svy == "2":
        a = 7
        b = 15
    elif svy == "3" :
        a = 16    
        b = 25
    elif svy == "-1":
        break


    while True:

        sayi1 = randint(a,b)
        sayi2 = randint(a,b)
        sonuc = sayi1 * sayi2

        print("-"*15, "\n", sayi1, "*", sayi2, "= ?")
        tahmin = input(" >> ")

        if tahmin == str(sonuc):
            print("-"*10, "\n","Tebrikler. Cevap Doğru.")
        elif tahmin == "-1":
            print("-"*15, "\n","Seviye seçiminden çıkıldı.\nYeni bir seviye seçin\n(1-Kolay, 2-Orta, 3-Zor) >> ")
            break
        else:
            print("-"*10, "\n","Yanlış cevap. sonuç {} olmalıydı".format(sonuc))