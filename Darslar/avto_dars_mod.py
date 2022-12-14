def avto_info(kompaniya, model, rang, korobka, yil, narh=None):
    """Avtomobil ma'lumotlari"""
    avto = {
        "company": kompaniya,
        "model": model,
        "color": rang,
        "box": korobka,
        "year": yil,
        "price": narh
        }
    return avto
def avto_kirit():
    avtolar = []
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting:   ")
        kompaniya = input("Ishlab chiqaruvchini kiriting:  ")
        model = input("Modelini kiriting:  ")
        rang = input("Rangini liriting:  ")
        korobka = input("Korobkasini kiriting:  ")
        yil = input("Yilini kiriting:  ")
        narh = input("Narhi:  ")
        avtolar.append(avto_info(kompaniya, model, rang, korobka, yil, narh))
        j = input("Yana avto qo'shamizmi (ha|yuq):  ")
        if j == 'yuq':
            break
    return avtolar


def info_print(avto_info):
    print('Saytimizga qo\'shgan ma\'lumotlaringiz:  \n')
    print(
        f"{avto_info['color'].title()} {avto_info['company'].upper()} "
        f"{avto_info['model'].upper()}, {avto_info['box']} korobka, "
        f"{avto_info['year']} - yil, {avto_info['price']}$")
