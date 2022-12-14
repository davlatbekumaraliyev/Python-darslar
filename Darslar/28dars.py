# file = open('pi.txt')
# PI = file.read()
# print(PI)
# file.close()

# with open('pi.txt') as file:
#     pi = file.read()
    
# # print(pi)


# pi = pi.rstrip()
# pi = pi.replace('\n', "")
# pi = float(pi)
# print(pi)



# filename = 'data/talabalar.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)
        
# with open(filename) as file:
#     talabalar = file.readlines()

# print(talabalar)   

# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)

# filename = 'file/ismlar.txt'

        
# with open(filename) as file:
#     talabalar = file.readlines()



# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)


# print(list(filter(lambda talabalar:(talabalar.startswith('n') and talabalar.endswith('r')), talabalar)))
    

    
# faylnomi = "new_file.txt"
# ism = 'Umar Hasanov'
# tyil = 1999
# with open(faylnomi, 'w') as fayl:
#     fayl.write(ism + '\n')
#     fayl.write(str(tyil) + '\n')


# with open(faylnomi, 'a') as fayl:
#     fayl.write('Alijon Valiyev\n')
#     fayl.write('2000\n')


import pickle

talaba1 = {'ism': 'hasan', 'familiya': 'umarov', 'tyil': 2000, 'kurs': 2}

with open('info1', 'wb') as file:
    pickle.dump(talaba1, file)


with open('info1', 'rb') as file:
    talaba_1 = pickle.load(file)

    
print(talaba_1)





