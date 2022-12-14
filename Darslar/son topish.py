from random import randint
def son_top(x=10):
    print('Assalomu alaykum!')
    print("Son topish o'yinini o'ynaymiz.")
    print("Men 1 dan 10 gacha son o'yladim.")
    oson = randint(1, x)
    urunish = 0
    print("Taxmin qilgan soningizni kiriting.")
    while True:
        son = int(input(">>>  "))
        if son < oson:
            print("Kattaroq son kiriting:  ")
            urunish += 1
        elif son > oson:
            print("Kichikroq son kiriting:  ")
            urunish += 1
        elif son == oson:
            urunish += 1
            break

    print("To'g'ri :)")
    print(f"Siz {urunish}da urinishda topdingiz.") 
    print(f"1 dan {x} gacha son o'ylang.")
    input("Son o'ylagan bo'lsangiz hohlagan tugmangizni bosing\n>>>  ")
    q = 1
    y = x
    urunish2 = 0
    while True:
        urunish2 += 1
        if q != y:
            son = randint(q, y)
        else:
            q = y
        javob = str(input(f"Siz {son}ni oyladingiz. To'gri bo'lsa (t), undan kattaroq bo'lsa(+), kichikroq bo'lsa(-). "))
        if javob == 't':
            break
        elif javob == '+':
            q = son + 1
        elif javob == '-':
            y = son - 1
        else:
            break
            print("Siz noto'g'ri tanladingiz!")
    
    print(f"Siz {urunish}da urinishda topdingiz.")     
    print(f"Men {urunish2}da urunishda topdim.")
    if urunish > urunish2:
        print("Men yutdim!")
    elif urunish < urunish2:
        print("Siz yutdingiz!")
    else:
        print("Durrang!")

son_top()




# AMALIYOT
#  • Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta 
# xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga 
# standart qiymat bering (masalan, kilometer=0)
#  • Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
#  ▪️ get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
#  • Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
#  ▪️ update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab
# borsin




# class Avto:
#     '''Avtomobil haqida ma'lumotlar'''
    
#     def __init__(self, korobka, model, rang, narh):
#         self.korobka = korobka
#         self.model = model
#         self.rang = rang
#         self.narh = narh
#         self.kilometr = 0
        
#     def get_box(self):
#         return self.korobka
    
#     def get_model(self):
#         return self.model
    
#     def get_narh(self):
#         return self.narh
    
#     def set_km(self, kilometr):
#         self.kilometr = kilometr
    
#     def malumotlar(self):
#         return f"{self.korobka} korobka {self.model} rangi {self.rang} narhi {self.narh}$, {self.kilometr} kilometr yurgan."
        
# avto1 = Avto('Avtomat', "Captiva", 'oq', 15000) 














