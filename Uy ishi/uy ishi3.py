# ismlar = ["Nurmuhammad", "Muhammadamin", "Asadbek"]

# print(f"Salom {ismlar[0]}, ishlaring yaxshimi?")
# print(f"Qandaysan {ismlar[1]}, omad senga!")
# print(f"Yaxshimisan {ismlar[2]}, sog'liklaring yaxshimi?")

# sonlar = [45, -56, 86.8, -34.2]

# sonlar[0] = sonlar[0] + sonlar[-1]
# sonlar[1] = 84
# sonlar[2] = sonlar[2] + 13.2
# print(sonlar)


# t_shaxslar = ["Amir temur", "Jaloliddin Manguberdi", "Alisher Navoi"] 
# z_shaxslar = ["Bill geyts", "Elon Mask", "Mark Zuckerberg"]
# print(f"Men zamonaviy shaxslardan {z_shaxslar.pop(-1)} intervyu olishni istardim. ")
# print(f"Men {t_shaxslar.pop(0)} eng buyuk odam deb uylayman.")


friends = []
friends.append("Nurmuhammad")
friends.append("Muhammadamin")
friends.append("Asadbek")
friends.append("Ahmadjon")
friends.append("Aziz")
print(f"To'liq ro'yhat-{friends}")

friends.remove("Asadbek")
friends.remove("Ahmadjon")
print(f"Kelganlar-{friends}")

friends.insert(0, "Behruz")
friends.insert(3, "Nikita")
friends.insert(7, "Eldor")
print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(-1))
print(f"Mening mehmonlarim {mehmonlar}.")
















