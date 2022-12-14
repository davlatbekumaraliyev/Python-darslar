###[:] copy
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talabani {ism.title()}ning bahosini qo'ying:   ")
#         baholar[ism] = baho
#     return baholar



# baholar = bahola(talabalar[:])
# for baho in baholar.values():
#     print(f"{(talabalar.pop()).title()}ning bahosi - {baho}")


# def summa(*sonlar):
#     """Yig'indini hisoblaydigan funksiya"""
#     yigindi = 0
#     for a in sonlar:
#         yigindi += a
#     return yigindi

# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def summa(*sonlar):
#     """Yig'indini hisoblaydigan funksiya"""
#     return sum(sonlar)



# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0,))


# def summa(x, y, *sonlar):
#     """Yig'indini hisoblaydigan funksiya"""
#     return x + y + sum(sonlar)

# print(summa(6, 4, 2, 3, 4, 5))
# print(summa(6, 4))


        
# def avto_info(kompaniya, model, **malumotlar):
#     malumotlar["company"] = kompaniya
#     malumotlar["model"] = model
#     return malumotlar

# avto1 = avto_info('GM', 'lacetti', rang='qora', yili=2016)
# print(avto1)



# 6 Foydalanuvchidan son qabul qilib, shu son miqdoricha fibonachchi ketma 
#ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing. Ta’rif: Har bir 
#hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik 
#Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb 
#olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

# def fibonacci(son):
#     """Ohirgi songa qo`shib ketadi"""
#     sonlar = [1, 1, 2]
#     for x in range(son-3):
#         sonlar.append((sonlar[-1] + sonlar[-2]))
        
        
#     return sonlar




# def fibonacci(son):
#     """Ohirgi songa qo`shib ketadi"""
#     sonlar = []
#     for x in range(son):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append((sonlar[-1] + sonlar[-2]))
        
        
#     return sonlar







def avto_info(kompaniya, model, rang, korobka, yil, narh=None):
    """Avtomobil ma'lumotlari"""
    avto = {
        "company": kompaniya,
        "model": model,
        "color": rang,
        "box": korobka,
        "year": yil,
        "price": narh
        }
    return avto

def avto_kirit():
    avtolar = []
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting:   ")
        kompaniya = input("Ishlab chiqaruvchini kiriting:  ")
        model = input("Modelini kiriting:  ")
        rang = input("Rangini liriting:  ")
        korobka = input("Korobkasini kiriting:  ")
        yil = input("Yilini kiriting:  ")
        narh = input("Narhi:  ")
        avtolar.append(avto_info(kompaniya, model, rang, korobka, yil, narh))
        j = input("Yana avto qo'shamizmi (ha|yuq):  ")
        if j == 'yuq':
            break
        
    return avtolar


def info_print(avto_info):
    print(
        f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
        f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
        f"{avto_info['yil']} - yil, {avto_info['narh']}$")
