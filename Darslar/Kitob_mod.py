#Kitob 
from uuid import uuid4

class Kitob:
    
    __num_book = 0
    
    def __init__(self, name, author, page, part, price=0):
        self.name = name     #ismi
        self.__author = author     #avtori
        self.page = page     #varaqi
        self.__isbn = uuid4()     #ID
        self.part = part     #Qismlari
        self.price = price     #narhi
        Kitob.__num_book += 1
        
        
    @classmethod
    def get_num_book(cls):
        return cls.__num_book
    
    def get_isbn(self):
        return self.__isbn
    
    def __repr__(self):
        return f"{self.name} {self.__author} yozgan. {self.price}"
        
    def get_author(self):
        return self.__author
    
    def get_name(self):
        return self.name
    
    def get_page(self):
        return self.page
    
    def get_part(self):
        return self.part
    
    def get_price(self):
        return self.price
    
    def get_info(self):
        info = f"Kitob nomi: {self.name}, avtori: {(self.__author).title()}, "
        info += f"Varoqlar soni: {self.page}, kitob {self.part} qismdan iborat. "
        info += f"Narhi: {self.price}"
        return info
    
kitob1 = Kitob('Boburnoma', "Bobur", 700, 8, 30000)
kitob2 = Kitob('Sariq devni minib', "To'xtaboyev", 150, 15, 24000)
kitob3 = Kitob('Boburnoma', "Bobur", 700, 8, 30000)
kitob4 = Kitob('Sariq devni minib', "To'xtaboyev", 150, 15, 24000)

    
class Kutibxona:
    
    def __init__(self, name):
        self.name = name
        self.kitoblar = []
        
    def __repr__(self):
        return f"{self.name} kutibxonasi."
        
    def __getitem__(self, index):
        return self.kitoblar[index]
        
    def __setitem__(self, index, value):
        if isinstance(value, Kitob):
            self.kitoblar[index] = value
            
    def add_kitob(self, *qiymat):
        for k in qiymat:
            if isinstance(k, Kitob):
                self.kitoblar.append(k)
            else:
                return ("Kitobni kiriting.")
            
    
    def __add__(self, qiymat):
        if isinstance(qiymat, Kutibxona):
            yangi_kutibxona = Kutibxona(f"{self.name} {qiymat.name}")
            yangi_kutibxona.kitoblar = self.kitoblar + qiymat.kitoblar
            return yangi_kutibxona
        elif isinstance(qiymat, Kitob):
            self.add_kitob(qiymat)
        else:
            print(f"Avtosalon ga {type(qiymat)} qo'shib bo'lmaydi.")
        
    def __call__(self, *param):
        if param:
            for kit in param:
                self.add_kitob(kit)
        else:
            return [kitob for kitob in self.kitoblar]
        
            
kutibxona1 = Kutibxona('Bilimdonlar')   
kutibxona2 = Kutibxona('Assalomu alaykum')

kutibxona1.add_kitob(kitob1, kitob2)
kutibxona2.add_kitob(kitob2, kitob4)

   
        