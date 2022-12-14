# faylnomi = "new_file_2.txt"
# ism = 'Hasan'
# with open(faylnomi, 'w') as fayl:
#     fayl.write(ism + '\n')

# ismlar = ['Umar', 'Salim', 'Laziz', 'Asil', 'Nodir', 'Aziz']

# with open(faylnomi, 'a') as fayl:
#     for q in ismlar:
#         fayl.write(q + '\n')
    

import pickle

avto1 = {'company': 'GM', 'model': 'Lacetti', 'price': 11000, 'kilometr': 0}

with open('info1', 'wb') as file:
    pickle.dump(avto1, file)


with open('info1', 'rb') as file:
    avto_1 = pickle.load(file)

    
print(avto_1)