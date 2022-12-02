# class Shaxs:
    
#     def __init__(self, ism, familiya, passport, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
        
        
#     def get_info(self):
#         info = f"{self.ism} {self.familiya}."
#         info += f"PASSPORT raqami: {self.passport}, {self.tyil} yilda tug'ilgan. "
#         return info
    
#     def get_age(self):
#         return (2022 - self.tyil)
    
# class Manzil:
#     """Manzil saqlash uchun klass"""

#     def __init__(self, uy, kocha, tuman, viloyat):
#         """Manzil xususiyatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat

#     def get_manzil(self):
#         """Manzilni ko'rish"""
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
#         return manzil
    
# class Talaba(Shaxs):
#     def __init__(self, ism, familiya, passport, tyil, idraqam,):
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
        
    
        
#     def get_id(self):
#         return self.idraqam
    
#     def get_bosqich(self):
#         return self.bosqich
 
#     def get_info(self):
#         info = f"{self.ism} {self.familiya}."
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}."
#         return info
# talaba1 = Talaba('Ali', "Valiyev", "AB12345678", 2000, 'ID87643456')
# talaba_m = Manzil("5/3", "Jayxun", "Yangiyer", "Sirdaryo")
# print(talaba1.get_info(), talaba_m.get_manzil())

# import turtle
# t = turtle.Turtle()
# t.speed(0)
# temp = 1
# c = ['red', 'green', 'blue']
# for i in range(400):
#     t.color(c[i%3])
#     t.forward(temp)
#     t.left(120)
#     t.left(1)
#     temp += 1

# turtle.mainloop()



       
        
        

    



class Talaba:
    def __init__(self, ism, familiya, passport, tyil, idraqam,):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.idraqam = idraqam
        self.bosqich = 1

    def get_name(self):
        return self.ism
    
    def get_bosqich(self):
        return self.bosqich
    
        
class Fan(Talaba):
    def __init__(self, ism, familiya, passport, tyil, idraqam, nomi, baho, chorak):
        super().__init__(ism, familiya, passport, tyil, idraqam)
        self.nomi = nomi
        self.baho = baho
        self.chorak = chorak
        
        
    def set_baho(self, baho1):
        return baho1
    
    
    def get_nomi(self):
        return self.nomi
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}."
        info += f"PASSPORT raqami: {self.passport}, {self.tyil} yilda tug'ilgan. "
        info += f"Fan nomi: {self.nomi}, baho: {self.baho}, chorak: {self.chorak}"
        return info
talaba = Fan("Ali", "valiyev", '999', 2000, "0000001", 'matematika', 5, 4)









