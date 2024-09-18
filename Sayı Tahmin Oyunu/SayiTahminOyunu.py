import random

a = random.randrange(1,10)

print("\n\nSayı Tahmin Oyununa Hoşgeldin 3 Hakkın var\n\n")

sayac = 3
while(sayac > 0):

    b = input("1 den 10 a kadar bir sayı tuttum. Tuttuğum sayıyı tahmin et: ")
    if int(b) == a:
        print(str(b) + " benim tuttuğum sayıydı tebrik ederim kazandın.")
        break

    else:

        if sayac == 1:
            if int(b) != a:
                print(f"bilemedin tuttuğum sayı: {a}")
                break

        else:
            sayac -= 1
            print("yanlış bildiniz.\nKalan hak sayısı:" + str(sayac))
            b
