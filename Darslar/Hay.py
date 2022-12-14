from random import randint
def hayvon_top(x=10):
    print('Assalomu alaykum!')
    print("Hayvon topish o'yinini o'ynaymiz.")
    hayvonlar = ('chumoli', "qo\'ng\'iz",'sichqon', 'kabutar', 'mushuk', 'kuchuk', 'sigir', 'begemot', 'fil', 'kit')
    hayvon = randint(1, 10)
    u = 0
    for i in hayvonlar:
        u += 1
        print(f"{u} - {i}")

    urunish = 0
    print("Taxmin qilgan hayvoningizni raqamini kiriting.")
    while True:
        h = int(input(">>>  "))
        if h < hayvon:
            print("Kattaroq hayvon kiriting:  ")
            urunish += 1
        elif h > hayvon:
            print("Kichikroq hayvon kiriting:  ")
            urunish += 1
        elif h == hayvon:
            urunish += 1
            break
    
    print("To'g'ri :)")
    print(f"{(hayvonlar[hayvon - 1]).title()} edi")
    print(f"Siz {urunish}ta urinishda topdingiz.") 
    

    




















