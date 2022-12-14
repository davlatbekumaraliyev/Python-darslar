class Talaba:
    
    __num_talaba = 0
    
    def __init__(self, ism, familiya, sharfi, kurs, baho=0):
        self.ism = ism
        self.familiya = familiya
        self.sharfi = sharfi
        self.__kurs = kurs
        self.baho = baho
        
        Talaba.__num_talaba += 1
        
    @classmethod
    def get_num_talaba(cls):
        return cls.__num_talaba
       
    def get_ism(self):
        return self.ism
    
    def __str__(self):
        return f"{(self.ism).title()} {(self.familiya).title()}, {self.__kurs} - da o'qiydi."
    
    def __repr__(self):
        return f"{(self.ism).title()} {(self.familiya).title()}, {self.__kurs} - da o'qiydi."
    
    def __gt__(self, y):
        return self.baho > y.baho
    
    def __lt__(self, y):
        return self.baho > y.baho
    
    def get_info(self):
        return (
            f"{(self.ism).title()} {(self.familiya).title()}, {self.kurs} - da o'qiydi. Bahosi {self.baho}"
            )
    

talaba1 = Talaba('Muhammad', "Asilov", "sherzodovich", 3, 5)
talaba2 = Talaba('Muhammadamin', "to'ychiyev", "sherzodovich", 3, 2)
talaba3 = Talaba('Muhammadali', "azizov", "sherzodovich", 2, 5)    
talaba4 = Talaba('Muhammadjon', "aliyev", "sherzodovich", 4, 3)




class Audetoria:
    
    def __init__(self, name):
        self.name = name
        self.talabalar = []
        
    def __repr__(self, name):
        return f"{self.name} auditoriasi."
        
    def __getitem__(self, index):
        return self.talabalar[index]
        
    def __setitem__(self, index, value):
        if isinstance(value, Talaba):
            self.talabalar[index] = value
            
    def add_talaba(self, *qiymat):
        for talaba in qiymat:
            if isinstance(talaba, Talaba):
                self.talabalar.append(talaba)
            else:
                return ("Talabani kiriting.")
            
        def __add__(self, qiymat):
            if isinstance(qiymat, Audetoria):
                yangi_a = Audetoria(f"{self.name} {qiymat.name}")
                yangi_a.talaba = self.talaba + qiymat.talaba
                return yangi_a
            elif isinstance(qiymat, Audetoria):
                self.add_talaba(qiymat)
            else:
                print("Audetoriaga talaba qo'shib bo'lmaydi.")
                
        def __call__(self, *param):
            if param:
                for talaba in param:
                    self.add_talaba(talaba)
            else:
                return [talaba for talaba in self.talabalar]
            
a1 = Audetoria('1 - audetoria')
a2 = Audetoria("2 - audetoria")

a1.add_talaba(talaba1, talaba2)
a2.add_talaba(talaba3, talaba4)



