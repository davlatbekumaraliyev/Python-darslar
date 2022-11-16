# def info(ism, familiya, t_yil, t_joy, yosh, email="", tel=None):
#     '''Foydalanuvchi ma'lumotlari'''
#     m = {
#         "name": ism,
#         "surname": familiya,
#         "year_of_birth": t_yil,
#         "address": t_joy,
#         "yers": yosh,
#         "phone_number": tel,
#         "@gmail": email
#         }
#     return m


# talaba1 = info('asadbek', 'saidov', 2000, 'jizzax', 22)
# talaba2 = info('temur', 'salimov', 1998, 'hovos', 24, 'temursalimov@gmail.com', 99_243_12_12)
# print('Talabaning ma\'lumotlari:  ')
# talabalar = [talaba1, talaba2]
# for m in talabalar:
#     if m['@gmail']:
#         email = f"{m['@gmail']}"
#     else:
#         email = 'Noma\'lum'
    
#     if m['phone_number']:
#         tel = f"{m['phone_number']}"
#     else:
#         tel = 'Noma\'lum'
#     a = (f"{m['name'].title()} {m['surname'].title()} {m['year_of_birth']}-yil {m['address'].title()}da tug'ilgan, telefon raqami: {m['phone_number']}, @gmail: {m['@gmail']} ")
        
# print(a)




# sonlar = []
# def maximum(sonlar):
#     '''Katta sonni qaytaruvchi funksiya'''
#     sonlar.append((input('Son kiriting:  ')))
#     sonlar.append((input('Son kiriting:  ')))
#     sonlar.append((input('Son kiriting:  ')))
    

# print(f'Sonlarni eng kattasi: {maximum(sonlar)}')






import math
def doira(diyametr, radiyus, perimetr):
    m = {
        'diameter': diyametr,
        'radius': radiyus,
        'perimeter': perimetr
        }
    return m

print("Aylana haqida ma'lumotlar")
malumotlar = []
while True:
    radiyus = int(input("Aylanani radiyusini kiriting:   "))
    diyametr = radiyus * 2
    perimetr = diyametr*(math.pi)
    malumotlar.append(doira(diyametr, radiyus, perimetr))
    e = str(input('Yana ma\'lumot kiritishni istaysizmi (ha|yo\'q):  '))
    if e.lower() == 'yo\'q':
        break
    elif e.lower() != 'ha':
        print("Siz noto'g'ri tanladingiz.")
        break
p = 0
print("Yig'ilgan ma'lumotlar:  ")
for m in malumotlar:
    p = p + 1
    w = (f"{p}) Diametr: {m['diameter']}, radius: {m['radius']}, perimetr: {m['perimeter']}")
    print(w.title())





