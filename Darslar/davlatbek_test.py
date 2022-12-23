# 1
class Teacher:
    
    __num_teacher = 0
    
    def __init__(self, ism, familiya, ochistva, mutaxasislik, b_universiteti, tel, email):
        self.ism = ism
        self.familiya = familiya
        self.ochistva = ochistva
        self.__mutaxasislik = mutaxasislik
        self.b_universiteti = b_universiteti
        self.tel = tel
        self.email = email
        Teacher.__num_teacher += 1
        
    def full_name(self):
        return f"Ismi: {(self.ism).title()}, familiyasi: {(self.familiya).title()}, {(self.ochistva).title()}."
    
    def get_phone(self):
        return self.tel
    
    def get_email(self):
        return self.email
    
    def get_study(self):
        return self.b_universiteti
    
    def get_info(self):
        return f"Ismi: {(self.ism).title()}, familiyasi: {(self.familiya).title()}, {(self.ochistva).title()}. Mutahasisligi: {self.__mutaxasislik}. Telefon raqami: {self.tel}"
    
    def get_m(self):
        return self.__mutaxasislik
    
    @classmethod
    def get_num(cls):
        return cls.__num_teacher
        
    
t1 = Teacher('Ali', 'vali', 'slimovich', 'matematika', 'samarqand', 998765432, "ali@gmail.com")
t2 = Teacher('Ali', 'vali', 'slimovich', 'matematika', 'samarqand', 998765432, "ali@gmail.com")



# 2
# class Avto:
    
#     def __init__(self, model, company, rang, yil,km=0):
#         self.model = model
#         self.company = company
#         self.rang = rang
#         self.km = km
#         self.yil = yil
        
#     def get_model(self):
#         return self.model
    
#     def get_company(self):
#         return self.company
    
#     def get_rang(self):
#         return self.rang
    
#     def get_yil(self):
#         return self.yil
    
#     def get_km(self):
#         return self.km
    
#     def update_km(self, a):
#         self.km += a
#         return self.km
    
#     def set_km(self, q):
#         self.km = q
#         return self.km
    
# a1 = Avto('lacetti', 'GM', 'qora', 2015)

# 3
# import json  

# talaba = {
#     'ism': 'Islom',
#     'yosh': 21,
#     'oila': False,
#     'fanlar': ('matematika', 'fizika'),
#     'baholar': [
#         {'fan': 'matematika', 'baho': 4},
#         {'fan': 'fizika', 'baho': 5}
#         ]
#     }

# talaba_json = json.dumps(talaba)


# with open('talaba.json', 'w') as f:
#     json.dump(talaba, f)

# filename = 'talaba.json'
# with open(filename) as f:
#     talaba = json.load(f)
# print(talaba)
# print(type(talaba))
    
# 4
    
# a = 0
# while True:
#     a+=1
#     print(a)
#     if a == 100:
#         break
        
    
# ismlar = ['ali', 'vali', 'salim', 'olim', 'asal']
# for a in ismlar:
#     print(f"{(a).title()} yaxshimisiz.")

# 5

# def __init__(self, ism, familiya, ochistva, mutaxasislik, b_universiteti, tel, email):
#         self.ism = ism
#         self.familiya = familiya
#         self.ochistva = ochistva
#         self.__mutaxasislik = mutaxasislik
#         self.b_universiteti = b_universiteti
#         self.tel = tel
#         self.email = email
#         Teacher.__num_teacher += 1
# 6

# from pprint import pprint
# import requests

# page = 'https://github.com'
# r = requests.get(page)
# pprint(r.text)

sonlar = [ 
1, 
2, 
3, 
4, 
5, 
6, 
7, 
8, 
9, 
10, 
11, 
12, 
13, 
14, 
15, 
16, 
17, 
18, 
19, 
20, 
21, 
22, 
23, 
24, 
25, 
26, 
27, 
28, 
29, 
30, 
31, 
32, 
33, 
34, 
35, 
36, 
37, 
38, 
39, 
40, 
41, 
42, 
43, 
44, 
45, 
46, 
47, 
48, 
49, 
50, 
51, 
52, 
53, 
54, 
55, 
56, 
57, 
58, 
59, 
60, 
61, 
62, 
63, 
64, 
65, 
66, 
67, 
68, 
69, 
70, 
71, 
72, 
73, 
74, 
75, 
76,  
78, 
79, 
80, 
81, 
82, 
83, 
84, 
85, 
86, 
87, 
88, 
89, 
90, 
91, 
92, 
93, 
94, 
95, 
96, 
97, 
98, 
99, 
100
]



a = 0
for e in sonlar:
    a += 1
    if a != e:
        print(a)
        a += 1
          
    












        