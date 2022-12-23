# docs.python.org/3/library

import datetime as dt
# hozir = dt.datetime.now()
# print(hozir)
# print(hozir.date())
# print(hozir.time())
# print(hozir.hour)
# print(hozir.minute)
# print(hozir.second)
# print(hozir.microsecond)
# print(hozir.isoweekday())
# print(hozir.isocalendar())



# bugun = dt.date.today()
# print(f"Bugungi sana: {bugun}")

# erta = dt.date(2022, 12, 19)
# print(f"Ertangi sana: {erta}")

# i = dt.date(2022, 12, 20)
# print(f"Indingi sana: {i}")

# hozir = dt.datetime.now()
# vh = (hozir.time())
# print(f'Hozir vaqt: {vh}')

# vk = dt.time(23, 45, 30)
# print(vk)



# bugun = dt.date.today()
# tatil = dt.date(2022, 12, 31)
# farq = tatil - bugun
# print(farq) 
# print(f"Tatilga {farq.days} kun qoldi.")


# h = dt.datetime.now()
# f = dt.datetime(2022, 12, 19, 00, 00, 00)
# fq = f - h
# s = f.seconds
# minutlar = int(s / 60)
# s = int(minutlar / 60)
# print(f"""Futbol tugashiga {fq.days} kuni {s} soat qoldi""")


# yyil = dt.datetime(2023, 1, 1, 00, 00)
# hozir = dt.datetime.now()
# f = yyil - hozir
# print(f"Yil tugashiga {f} kun, {f.hour} soat, {f.minute} ")


# h = dt.datetime.now()
# v = h.strftime("%H:%M:%S")
# print(v)
# sana = h.strftime('%d-%m-%Y')
# print(f"Bugun sana: {sana}")

# sana_v = h.strftime('%d/%m/%Y, %H:%M')
# print(sana_v)








# from fuzzywuzzy import fuzz

# from fuzzywuzzy import process

# words = ['talaba', 'tolib', 'kasalxona', 
#           'tatil', 'salat', 'salim',
#           'salom', 'assalom'
#           ]

# print(fuzz.ratio('salom', 'assalom'))



# text = 'salom'
# m = process.extract(text, words, limit=3)
# print(m)

# text = 'kasalhona'
# m = process.extractOne(text, words)
# print(m)












