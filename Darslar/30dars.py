# yosh = input('Yoshingizni kiriting: ')
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Butun son kiritmadingiz.")
# else:
#     print(f"Siz {2022 - yosh} yilda tug'ilgansiz.")
    
# print('Dastur tugadi.')

# x, y = 3, 10
# try:
#     print(y/(x-2))
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")



# mevalar = ['olma','anor','anjir','uzum']
# a = int(input("index kiriting: "))
# index = a - 1
# try:
#     if len(mevalar) <= index:
#         mevalar[index]
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos.")
# else:
#     print(mevalar[index])

# user = {"username":"go",
#         "status":"admin",
#         "email":"admin@www.go",
#         "phone": 99899876543}

# key=input("Kalitni kiriting: ")
# try:
#     print(f'Foydalanuvchi: {user[key]}')
# except KeyError:
#     print("Bunday kalit yo'q")


# filename = "data_2.txt" # bunday fayl mavjud emas
# with open(filename) as f:
#     text = f.read()


# filename = "data_2.txt" # bunday fayl mavjud emas
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"Kechirasiz, {filename} fayl mavjud emas.")


# n = input('Butun son kiriting: ')
# n = int(n)
# x = 20/n

# print(x)

# n = input('Butun son kiriting: ')
# try:
#     n = int(n)
#     x = 20/n
# except ValueError:
#     print('Butun son kiritmadingiz!')
# except ZeroDivisionError:
#     print('0 ga bo\'linmaydi.')
# else:
#     x = 20%n
#     print(x)

# while True:
#     yosh = input('Yoshingizni kiriting: ')
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break


# print(f"Siz {2022 - yosh} yilda tug'ilgansiz.")




# try:
#     x = int(input("x ni kiriting: "))
#     y = int(input("y kiriting: "))
#     print(f'{x} / {y} = {x/y}')
# except ZeroDivisionError:
#     print("0 ga bo'linmaydi!")
# except ValueError:
#     print("Bu son emas!")
# except:
#     print("Xato yuz berd!")




