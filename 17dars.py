# nums = [5, 7, 2, 10, 0, 4, 9, 8, 6, 1, 3]

# def bubble(nums):
#     n = len(nums)
#     swaps = 0
#     for i in range(n-1):
#         if nums[i] > nums[i+1]:
#             nums[i], nums[i+1] = nums[i+1], nums[i]
#             swaps += 1
#     return swaps
    
# def bubble_sort(nums):
#     n = len(nums)
#     for _ in range(n-1):
#         if bubble(nums) == 0:
#             break
        
# bubble_sort(nums) = 0

# def summa():
#     natija = 0
#     a = input("Hohlagan soningizni kiriting\n>>>  ")
#     for q in range(len(a)):
#         natija += int(a[q])
#     return natija


# def toliq_ism_dasturi(ism, familiya):
#     '''Ism chiqaruvchi funksiya'''
#     toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism


# talaba1 = toliq_ism_dasturi('olim', 'olimov')
# talaba2 = toliq_ism_dasturi('aziz', 'azizov')
# print(f"Assalomu alaykum {talaba1}")
# print(f"Hush kelibsiz {talaba2}")






# def toliq_ism_dasturi(ism, familiya, otasining_ismi=''):
#     '''Ism chiqaruvchi funksiya'''
#     if otasining_ismi:
#         toliq_ism = f"{ism} {familiya} {otasining_ismi}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_dasturi('olim', 'olimov')
# talaba2 = toliq_ism_dasturi('halim', 'hakimov', 'saidovich')
# print(f"Darsga kechikib kelganlar: {talaba1} va {talaba2}")



# def avto_info(kompaniya, model, rang, korobka, yil, narh=None):
#     """Avtomobil ma'lumotlari"""
#     avto = {
#         "company": kompaniya,
#         "model": model,
#         "color": rang,
#         "box": korobka,
#         "year": yil,
#         "price": narh
#         }
#     return avto


# avto1 = avto_info('GM', 'malibu', 'qora', 'avtomat', 2018)
# avto2 = avto_info('GM', 'gentra', 'oq', 'mexanika', 2016, 15000)
# print("Onlayn bozordagi mavjud avtomobillar:")
# avtolar = [avto1, avto2]
# for avto in avtolar:
#     if avto['price']:
#         narh = f"{avto['price']}$"
#     else:
#         narh = 'Noma\'lum'
#     a = (f"{avto['color']} {avto['model']}. Narhi {narh}")
#     print(a.title())



# def oraliq(min, max):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(0, 11))
# print(oraliq(10, 21))







# def oraliq(min, max, qadam=1):
#     sonlar = []
#     while min < max:
#             sonlar.append(min)
#             min += qadam
#     return sonlar   
# print(oraliq(1, 21, 3))



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


print("Saytimizdagi avtolar ro'yhatini shakllantiramiz.")
avtolar = []
while True:
    print("Quyidagi ma'lumatlarni kiriting:  ")
    kompaniya = input("Ishlab chiqaruvchi:  ")
    model = input("Modeli:  ")
    rang = input('Rangi:  ')
    korobka = input('Korobkasi:  ')
    yil = input('Yili:  ')
    narh = input('Narhi($ ):  ')
    avtolar.append(avto_info(kompaniya, model, rang, korobka, yil, narh))
    a = input('Yana ma\'lumot kiritishni istaysizmi (yes|no):  ')
    if a == 'no':
        break
    elif a != 'yes' or 'no':
        print('Siz noto\'g\'ri tanladingiz.')
        break
        
print('Saytdagi ma\'lumotlar')   
for avto in avtolar:
    if avto['price']:
        narh = f"{avto['price']}$"
    else:
        narh = 'Noma\'lum'
    w = (f"{avto['color']} {avto['company']} {avto['model']} {avto['box']} korobka {avto['year']} - yil {avto['price']}")
    print(w.title())




def talabani_bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f'Talaba {ism.title()}ning bahosini qo\'ying.')
        baholar[ism] = int(baho)
    return baholar

baho = talabani_bahola(['umaraliyev_Diyorbek', 'vali', 'hasan', 'husan'])
print(baho)

    

    
    
    
    
    