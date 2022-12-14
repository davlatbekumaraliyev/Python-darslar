def talaba_info(ism, familiya, kurs, yil, yosh):
    """Talabani ma'lumotlari"""
    """ism, familiya, kurs, yil, yosh."""
    talaba = {
        'name': ism,
        'surname': familiya,
        'curs': kurs,
        'year': yil,
        'years': yosh
        }
    return talaba
def t_k():
    tlar = []
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting:   ")
        ism = input('Ismingizni kiriting:  ')
        familiya = input('Familiyangizni kiriting:  ')
        kurs = input("Nechanchi kursligingizni kiriting:  ")
        yil = input("Tug'ilgan yilingizni kiriting:  ")
        yosh = input("Yoshingizni kiriting:  ")
        tlar.append(talaba_info(ism, familiya, kurs, yil, yosh))
        javob = input("Yana ma\'lumot qo\'shasizmi?\n(ha/yuq)>>>  ")
        if javob == "yuq":
            break
        return tlar
def t_i_p(talaba_info):
    print(
        'Siz qo\'shgan ma\'lumotlar:  \n'
        f"{talaba_info['name'].title()} {talaba_info['surname'].title()}, "
        f"yoshi {talaba_info['years']}da, {talaba_info['year']}-yilda tug'ilgan, "
        f"{talaba_info['curs']}-kursda o'qiydi."
        )
    
        
        
        