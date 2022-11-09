# print("Kiritilgan sonning kavadratini qaytaruvchi dastur.")
# savol = 'Istalgan son kiriting'
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing):  "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print('Dastur tugadi!')






# print("Kiritilgan sonning kavadratini qaytaruvchi dastur.")
# savol = 'Istalgan son kiriting'
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing):  "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi!')



# print("Kiritilgan sonning kavadratini qaytaruvchi dastur.")
# savol = 'Istalgan son kiriting'
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing):  "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi!')




# sonlar = list(range(1, 11))
# for son in sonlar: 
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")


# sonlar = list(range(1, 11))
# for son in sonlar: 
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")



# from random import randint

# while True:
#     a = randint(1, 20)
#     b = randint(1, 20)
#     w = input(f'Javobini kiriting:  {a} x {b} (Dasturni to\'xtatish uchun \'exit\' deb yozing)  \n>>>  ')
#     if w != 'exit':
#         if w == (a * b):
#             print("to'g'ri")
#         else:
#             print("xato")
#     else:
#         break
# print('Dastur tugadi!')










# from random import randint
# while True:
#     a = randint(1, 10)
#     b = randint(1, 10)
#     u = input("Javobini kiriting: {} x {} (Dasturni to\'xtatish uchun \'exit\' deb yozing)\n>>>  ".format(a, b))
#     if u != 'exit':
        
#         if int(u) == int(a * b):
#             print("To'g'ri")
#         else:
#             print("Xato")
#     else:
#         break
# print('Dastur tugadi!')
    
    
    
    
    
    
# son = 0
# while son < 10:
#     son += 1
#     if son % 2 ==0:
#         continue
#     else:
#         print(son)
        
        
        
import math
print("Kiritilgan sonning ildizini qaytaruvchi dastur. ")
savol = "Istalgan son kiriting"
savol += '(dasturni to\'xtatish uchun \'exit\' deb yozing):  '
while True:
    son = input(savol)
    if son == 'exit':
        break
    else:
        if int(son) < 0:
            print("Iltimos musbat son kiriting!")
        else:
            print(math.sqrt(float(son)))
print('Dastur to\'xtadi!')
        
        
        

















        
        
        
        
        
        
        