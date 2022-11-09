# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
    
    
# salom_ber()


# def salom_ber(ism, familiya):
#     """Foydalanuvchini ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum hurmatli {ism.title()} {familiya.title()}")
    
# salom_ber('hasan', 'hasanov')
# salom_ber('ali', 'aliyev')


# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(
#         f"Foydalanuvchi ismi: {ism.title()}\n"
#         f"Foydalanuvchi familiyasi: {familiya.title()}\n"
#         )
    
# toliq_ism('ali', "aliyev")


# def yosh_hisobla(ism, tugilgan_yil):
#     '''Yosh hisoblovchi dastur'''
#     print(f"{ism.title()} {2022-tugilgan_yil} yoshda.")
    
# yosh_hisobla('ali', 1997)


# def yosh_hisobla(t_y, j_y=2022):
#     """Foydalanuvchi tugilgan yilidan uning yoshini hisoblaydigan dastur"""
#     print(f"Siz {j_y-t_y} yoshdasiz")
    
# yosh_hisobla(2200, 2022)

def talaba_malumotlari(ism, familiya, t_yil, tel_raqam, kurs):
    """Talaba malumotlari"""
    print(f"Talabaning ismi: {ism.title()},\nfamiliyasi: {familiya.title()},\ntugulgan yili:{t_yil},\ntelefon raqami: {tel_raqam},\n{kurs} da o'qiydi.")

talaba_malumotlari('ali', 'aliyev', 2000, 99_123_45_67, 4)

