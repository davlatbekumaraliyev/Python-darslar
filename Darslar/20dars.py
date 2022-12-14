# import avto_dars_mod as adm

# avto1 = adm.avto_info("GM", "Malibu", "qora", "avto", 2020, 40000)
# adm.info_print(avto1)


# import avto_dars_mod as adm

# avto1 = adm.avto_kirit()

# for avto in avto1:
#     adm.info_print(avto)
    
    
# from avto_dars_mod import avto_info, info_print
# avto1 = avto_info("GM", "Malibu", "qora", "avto", 2020, 40000)
# info_print(avto1)

# from avto_dars_mod import avto_info as ainfo, info_print as iprint
# avto1 = avto_info("GM", "Malibu", "qora", "avto", 2020, 40000)
# info_print(avto1)


# from avto_dars_mod import *
# avto1 = avto_info("GM", "Malibu", "qora", "avto", 2020, 40000)
# info_print(avto1)
#___________________________________________________________________________________

# import math
# uzunlik = lambda pi, r : 2*pi*r

# print(uzunlik(math.pi, 10))

# daraja = lambda x, y : x**y
# print(daraja(3, 2))


# def daraja(n):
#     return lambda x: x ** n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(kvadrat(10))
# print(kub(10))
# print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng.")



# from math import sqrt
# sonlar = list(range(11))
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)

# print(list(map(lambda x: x*x, sonlar)))
# from math import pow

# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x, y: x + y, a, b))
# print(a_plus_b)



# ismlar = ['hasan', 'husan','olim','umid']
# print(list(map(lambda math:math.upper(),ismlar)))


# import random as r
# sonlar = r.sample(range(100), 10)
# print(sonlar)

# juft_sonlar = list(filter(lambda x: x % 2 ==0, sonlar))
# print(juft_sonlar)


# mevalar = ['olma', 'anor', 'anjir', 'shaftoli', 'o\'rik', 'tarvuz', 'qovun', 'banan']
# harf = 'a'
# mevalar_b = list(filter(lambda meva: meva.startswith(harf), mevalar))
# print(mevalar_b)

# mevalar2 = list(filter(lambda meva: len(meva) <= 5, mevalar))
# print(mevalar2)

# print(list(filter(lambda meva: (meva.startswith('a') and meva.endswith('r')), mevalar)))

# import random as r

# sonlar = r.sample(range(100), 10)

# juft = [son for son in sonlar if son%2==0]
# print(sonlar)
# print(juft)

# perimetr = lambda a, b: (a+b)*2

# print(perimetr(10, 5))


# daraja = lambda x, y: int(x)**int(y)
# son1 = (input("Sonni kiriting:  "))
# son2 = int(input(f"{son1} ning darajasini yozing:  "))
# print(daraja(son1, son2))


# insonlar = ['ali', 'sardor', 'vali', 'javoxir', 'diyor', 'odil', 'salim', 'bexruz']
# w = input("Siz qidirmoqchi bo'lgan insonni ismini 1-harfini yozing:  ")
# r = input("Siz qidirmoqchi bo'lgan insonni ismini 2-harfini yozing:  ")
# a = (list(filter(lambda inson: (inson.startswith(w) and inson.endswith(r)), insonlar)))
# if a == ['diyor']:
#     print('Salimov Diyor, 19 yoshda')
# elif a == ['ali']:
#     print('Tuychiyev Ali, 25 yoshda')
# elif a == ['sardor']:
#     print('Ilyosov Sardor,  yoshda')
# elif a == ['vali']:
#     print('Husanov Vali, 21 yoshda')
# elif a == ['javoxir']:
#     print('Aliyev Javoxir, 35 yoshda')
# elif a == ['odil']:
#     print('Zoyirox Odil, 43 yoshda')
# elif a == ['salim']:
#     print('Ro\'ziboyev Salim, 31 yoshda')
# elif a == ['bexruz']:
#     print('Toxirov Bexruz, 19 yoshda')
# else:
#     print("Uzur bizda bunday ma'lumot yo'q.")



