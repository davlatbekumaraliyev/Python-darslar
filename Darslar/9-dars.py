# yosh = int(input("Yoshinngizni kiriting: "))
# if yosh <= 4:
#     print("Sizga kirish bepul.")
# elif yosh <= 12:
#     print("Sizga kirish 5000 sum.")
# elif yosh <= 18:
#     print("Sizga kirish 10000 sum.")
# else:
#     print("Sizga kirish 15000 sum.")
    
    
# yosh  = int(input("Yoshingizni kiriting: "))
# if yosh <= 4:
#     price = 0
# elif yosh <=12:
#     price = 5000
# elif yosh < 60:
#     price = 10000
# else:
#     price = 8000
# print(f"Sizga kirish {price} so'm.")
    
# kun = input("Bugun qaysi kun?\n>>> ")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba': 
#     print("Bugun dam olish kuni.")
# else:
#     print("Bugun ish kuni.")    
    
    
# kun = input("Bugun nima kun?\n>>> ")
# h = float(input("Havo harorati qanday?>>> "))
# if kun.lower() == 'yakshanba' and h >= 30:
#     print("Chomilishga ketdik!")
# elif kun.lower() == 'yakshanba' and h < 30:
#     print("Uyda dam olamiz.")
    
    
    
# choy = True
# salat = False
# s = 15000
# if choy and salat:
#     s = s + 10000
# elif choy or salat:
#     s = s + 5000
    
# print(f"Jami {s} so'm.")
        

# narh = 15000
# non = True
# choy = True
# salat = False
# if choy:
#     print("Buyurtmachi choy oldi. ")
#     narh += 3000
# if salat:
#     print("Buyurtmachi salat oldi. ")
#     narh += 5000
# if non:
#     print("Buyuyrtmachi non oldi. ")
#     narh += 3000
    
# print(f"Jami {narh} so'm. ")
    
    
# ism = input("Ta'laba ism va familiyasini kiriting:  ")
# baho = int(input(f"{ism.title()}ni baholang>>> "))
# if baho == 5:
#     print("A'lo")
# elif baho == 4:
#     print("Yaxshi.")
# elif baho <= 3:
#     print("Yomon.")
    
    
# menu = []
# for a in range(1, 6):
#     menu.append(input("Nima ovqat kiritishni istaysiz>>> "))
# ovqat = input("Nima ovqat yeysiz?>>> ")
# if ovqat.lower() not in menu:
#     print(f"Afsuski bizda {ovqat} yo'q. Bizdagi taomlar: ")
#     for f in menu:
#         print(f, end=("\n"))
#     taom = input("Iltimos bizdagi taomlardan buyurtma qiling: ")
#     print(f"{taom} qabul qilindi.")
# else:
#     print("Buyurtmangiz qabul qilindi.")
    
    
    
    

avtolar = []
for b in range(1, 6):
    avtolar.append(input("Qanaqa kompaniya avtomobillarini qo'shishni istaysiz:  ")) 
avtomobil = input("Qaysi kompaniya avtomobilini tanlaysiz>>> ")
if avtomobil.lower() not in avtolar:
    print(f"Afsuski bizda {avtomobil} kompaniyasi avtomobili yo'q. Bizdagi avtomobil kompaniyalari: ")
    for a in avtolar:
        print(a, end= ("\n"))
    avto = input("Iltimos bizdagi kompaniya avtomobillaridan buyurtma qiling: ")
    print(f"{avto} qabul qilindi")
else:
    print("Buyurtmangiz qabul qilindi. ") 
    
    
    
    
    
    
    
    