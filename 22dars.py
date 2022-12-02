# class Talaba:
#     """Talaba nomli klass yaratamiz"""
    
#     def __init__(self, ism, familiya, tyil, tel):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.tel = tel
        
#     def get_f_name(self):
#         return f"To'liq ism familiyam: {(self.ism).title()} {(self.familiya).title()}"
    
#     def get_tel(self):
#         return self.tel
    
#     def tanishuv(self):
#         print(f"Mening ism familiyam {(self.ism).title()} {(self.familiya).title()}, tug'ilgan yilim {self.tyil}, telefon raqamim {self.tel}")
    
#     def get_name(self):
#         return self.ism
    
#     def get_lastname(self):
#         return self.familiya
    
#     def get_age(self, yil):
#         return yil - self.tyil
    
# talaba1 = Talaba('Ali', 'valiyev', 2000, 992345678)
# talaba2 = Talaba('vali', 'aliyev', 1995, 991234567)
# print((talaba1.ism).title()), print((talaba1.familiya).title()), talaba2.tanishuv()

# class Avto:
#     '''Avtomobil haqida ma'lumotlar'''
    
#     def __init__(self, kompaniya, model, rang, narh):
#         self.kompaniya = kompaniya
#         self.model = model
#         self.rang = rang
#         self.narh = narh
        
#     def get_company(self):
#         return self.kompaniya
    
#     def get_model(self):
#         return self.model
    
#     def get_narh(self):
#         return self.narh
    
#     def malumotlar(self):
#         return f"{self.kompaniya} {self.model} rangi {self.rang} narhi {self.narh}$"
        
# avto1 = Avto('GM', "Captiva", 'oq', 15000)     