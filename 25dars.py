#INCAPSULATSIYA
from uuid import uuid4

# class Avto:
    
#     def __init__(self, make, model, rang, yil, narh, km=0):
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.__narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1
        
        
#     def get_km(self):
#         return self.__km
        
#     def get_id(self):
#         return self.__id
    
#     def add_km(self, km):
#         if km >= 0:
#             self.__km += km
#         else:
#             return "Mashina km kamaytirib bo'lmaydi"
    
#     def get_narh(self):
#         return self.__narh
    
#     def set_narh(self, n):
#         self.__narh = n
#         return self.__narh
    
        
        
# avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000, 1000) #UUID('6ed2d1cb-1ab2-41f9-a6f9-b8a8ebbcd575')
# avto2 = Avto("GM", "Malibu", "Qora", 2020, 40000, 1000)
# avto3 = Avto("GM", "Malibu", "Qora", 2020, 40000, 1000)


class Avto:
    
    __num_avto = 0
    
    def __init__(self, make, model, rang, yil, narh, km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.__narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
        
        
    def get_km(self):
        return self.__km
        
    def get_id(self):
        return self.__id
    
    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            return "Mashina km kamaytirib bo'lmaydi"
    
    def get_narh(self):
        return self.__narh
    
    def set_narh(self, n):
        self.__narh = n
        return self.__narh
    
    # def get_num_avto():
    #     return Avto.num_avto
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
        
        
avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000, 1000) #UUID('6ed2d1cb-1ab2-41f9-a6f9-b8a8ebbcd575')
avto2 = Avto("GM", "Malibu", "Qora", 2020, 40000, 1000)
avto3 = Avto("GM", "Malibu", "Qora", 2020, 40000, 1000)