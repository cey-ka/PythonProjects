import random

print("\n TAŞ KAĞIT MAKAS OYUNUNA HOŞGELDİNİZ \n")

rakip = input("Seçim yap (taş = t, kağıt = k , makas = m): ").lower()

def rules(comp, rakip):

    if str(comp) == "taş" and str(rakip) == "t" or str(comp) == "kağıt" and str(rakip) == "k" or str(comp) == "makas" and str(rakip) == "m":
        return

    elif str(comp)== "taş" and str(rakip) == "m" or str(comp) == "kağıt" and str(rakip)== "t" or str(comp) == "makas" and str(rakip)== "k":
        return

    elif str(comp) == "makas" and str(rakip) == "t" or str(comp) == "kağıt" and str(rakip) == "m" or str(comp) == "taş" and str(rakip) == "k":
        return

    else:
        return"hatalı tuşlama yaptınız."





compscore = 0
userscore = 0

while compscore < 3 and userscore < 3:
    

    eleman = ["taş", "kağıt" , "makas"]
    comp = random.choice(eleman)

    rules(comp, rakip)

    if str(comp)== "taş" and str(rakip) == "m" or str(comp) == "kağıt" and str(rakip)== "t" or str(comp) == "makas" and str(rakip)== "k":
        compscore += 1
        
        if compscore == 3:
            print(f"Game Over\nSkor: Bilgisayar {compscore} - Kullanıcı {userscore}")
            break
                
        else: 
            print(f"\nBilgisayar {comp.upper()} hamlesini yaptı. güncel skor: Bilgisayar {compscore} - Kullanıcı {userscore}")
            rakip = input("Seçim yap (taş = t, kağıt = k , makas = m): ")
        
    elif str(comp) == "taş" and str(rakip) == "t" or str(comp) == "kağıt" and str(rakip) == "k" or str(comp) == "makas" and str(rakip) == "m":
            print(f"\nBilgisayar {comp.upper()} hamlesini yaptı. güncel skor: Bilgisayar {compscore} - Kullanıcı {userscore}")
            rakip = input("Seçim yap (taş = t, kağıt = k , makas = m): ")


    elif str(comp) == "makas" and str(rakip) == "t" or str(comp) == "kağıt" and str(rakip) == "m" or str(comp) == "taş" and str(rakip) == "k":
            userscore += 1

            if userscore == 3:
                print(f"Tebrikler kazandınız.\nSkor: Bilgisayar {compscore} - Kullanıcı {userscore}")
                break

            else:
                print(f"\nBilgisayar {comp.upper()} hamlesini yaptı. güncel skor: Bilgisayar {compscore} - Kullanıcı {userscore} \n")
                rakip = input("Seçim yap (taş = t, kağıt = k , makas = m): ")

    else:
        print("HATALI TUŞLAMA YAPTINIZ!")
        break