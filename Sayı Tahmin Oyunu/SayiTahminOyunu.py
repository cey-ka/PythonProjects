import random

a = random.randrange(10)
b = input("1 den 10 a kadar bir sayı tuttum. Tuttuğum sayıyı tahmin et (3 hakkın var): ")


if int(a) == int(b):
    print(str(b) + " benim tuttuğum sayıydı tebrik ederim kazandınız.")

else:
    print("yanlış")
    sayac = 3 
    while(sayac > 1 ):
        print("kalan hak sayısı: " + str(sayac-1))
        sayac = sayac -1
        c = input("Tuttuğum sayıyı tahmin edin: ")
        
    if int(a) != int(b):
        print("bilemediniz tuttuğum sayı " + str(a) + " idi.") 


    

