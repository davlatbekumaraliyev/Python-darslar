#Kalkulyator
import math
lang = input("Select a language\nTilni tanlang\n(EN|UZ)>>>   ")
if lang.lower() == 'uz':
    print("Assalomu alaykum. Siz python kalkulyatoridasiz!")
    masalalar = ["Ko'paytirish", "bo'lish", "ayirish", "qo'shish", "daraja", "ildiz"]
    son = 1
    for a in masalalar:
        print(son, "-", a, end= ("\n"))
        son += 1
    amal = (input("Tanlagan amalingizni raqamini yozing\n>>> "))
    while True:
        if amal.lower() == '1':        
            a = (input("1 - sonni kiriting:  "))
            b = (input("2 - sonni kiriting(dasturni to'xtatish uchun 'chiqish' ni yozing):  "))
            if b != 'chiqish':  
                c = int(a)*int(b)
                print(int(c))
            elif a or b == 'chiqish':
                break
            else:
                print("Siz noto'g'ri yozdingiz.")
        elif amal.lower() == '2':        
            a = (input("1 - sonni kiriting:  "))
            b = (input("2 - sonni kiriting(dasturni to'xtatish uchun 'chiqish' ni yozing):  "))
            if b != 'chiqish':  
                c = int(a)/int(b)
                print(float(c))
            elif a or b == 'chiqish':
                break
            else:
                print("Siz noto'g'ri yozdingiz.")
        elif amal.lower() == '3':        
            a = (input("1 - sonni kiriting:  "))
            b = (input("2 - sonni kiriting(dasturni to'xtatish uchun 'chiqish' ni yozing):  "))
            if b != 'chiqish':  
                c = int(a)-int(b)
                print(int(c))
            elif a or b == 'chiqish':
                break
            else:
                print("Siz noto'g'ri yozdingiz.")
        elif amal.lower() == '4':        
            a = (input("1 - sonni kiriting:  "))
            b = (input("2 - sonni kiriting(dasturni to'xtatish uchun 'chiqish' ni yozing):  "))
            if b != 'chiqish':  
                c = int(a)+int(b)
                print(int(c))
            elif a or b == 'exit':
                break
            else:
                print("Siz noto'g'ri yozdingiz.")
        elif amal.lower() == '5':        
            a = (input("Sonni kiriting:  "))
            b = (input("Darajasini kiriting(dasturni to'xtatish uchun 'chiqish' ni yozing):  "))
            if b != 'chiqish':  
                c = int(a)**int(b)
                print(int(c))
            elif a or b == 'chiqish':
                break
            else:
                print("Siz noto'g'ri yozdingiz.")
        elif amal.lower() == '6':        
            b = (input("Sonni kiriting(dasturni to'xtatish uchun 'chiqish' ni yozing):  "))
            if b != 'chiqish':  
                c = int(math.sqrt(int(b)))
                print(int(c))
            elif a or b == 'chiqish':
                break
            else:
                print("Siz noto'g'ri yozdingiz.")
        else: 
            print("Siz noto'g'ri tanladingiz!")
            break
    u = input("Yana boshqa amalni bajarishni istaysizmi(ha|yo'q)?\n>>>  ")
    if u == 'ha':
        son2 = 1
        for a in masalalar:
            print(son2, "-", a, end= ("\n"))
            son2 += 1
        amal = (input("Tanlagan amalingizni raqamini yozing\n>>> "))
        while True:
            if amal.lower() == '1':        
                a = (input("1 - sonni kiriting:  "))
                b = (input("2 - sonni kiriting(dasturni to'xtatish uchun 'chiqish' ni yozing):  "))
                if b != 'chiqish':  
                    c = int(a)*int(b)
                    print(int(c))
                elif a or b == 'chiqish':
                    break
                else:
                    print("Siz noto'g'ri yozdingiz.")
            elif amal.lower() == '2':        
                a = (input("1 - sonni kiriting:  "))
                b = (input("2 - sonni kiriting(dasturni to'xtatish uchun 'chiqish' ni yozing):  "))
                if b != 'chiqish':  
                    c = int(a)/int(b)
                    print(float(c))
                elif a or b == 'chiqish':
                    break
                else:
                    print("Siz noto'g'ri yozdingiz.")
            elif amal.lower() == '3':        
                a = (input("1 - sonni kiriting:  "))
                b = (input("2 - sonni kiriting(dasturni to'xtatish uchun 'chiqish' ni yozing):  "))
                if b != 'chiqish':  
                    c = int(a)-int(b)
                    print(int(c))
                elif a or b == 'chiqish':
                    break
                else:
                    print("Siz noto'g'ri yozdingiz.")
            elif amal.lower() == '4':        
                a = (input("1 - sonni kiriting:  "))
                b = (input("2 - sonni kiriting(dasturni to'xtatish uchun 'chiqish' ni yozing):  "))
                if b != 'chiqish':  
                    c = int(a)+int(b)
                    print(int(c))
                elif a or b == 'chiqish':
                    break
                else:
                    print("Siz noto'g'ri yozdingiz.")
            elif amal.lower() == '5':        
                a = (input("Sonni kiriting:  "))
                b = (input("Darajasini kiriting(dasturni to'xtatish uchun 'chiqish' ni yozing):  "))
                if b != 'chiqish':  
                    c = int(a)**int(b)
                    print(int(c))
                elif a or b == 'chiqish':
                    break
                else:
                    print("Siz noto'g'ri yozdingiz.")
            elif amal.lower() == '6':        
                b = (input("Sonni kiriting(dasturni to'xtatish uchun 'chiqish' ni yozing):  "))
                if b != 'chiqish':  
                    c = int(math.sqrt(int(b)))
                    print(int(c))
                elif a or b == 'chiqish':
                    break
                    
                else:
                    print("Siz noto'g'ri yozdingiz.")
            else: 
                print("Siz noto'g'ri tanladingiz!")
                break
    elif u == 'yo\'q':    
        print("Dastur tugadi!")
    else:
        print("Siz noto'g'ri tanladingiz.")
    print("Dastur tugadi!")
elif lang.lower() == 'en':
    print("Hello. You are in a python calculator!")
    masalalar = ["Multiply", "divide", "subtract", "add", "degree", "root"]
    son = 1
    for a in masalalar:
        print(son, "-", a, end= ("\n"))
        son += 1
    amal = (input("Write the number of your chosen action\n>>> "))
    while True:
        if amal.lower() == '1':        
            a = (input("Enter number 1:  "))
            b = (input("Enter number 2 (type 'exit' to stop the program):  "))
            if b != 'exit':  
                c = int(a)*int(b)
                print(int(c))
            elif a or b == 'exit':
                break
            else:
                print("You typed wrong.")
        elif amal.lower() == '2':        
            a = (input("Enter number 1:  "))
            b = (input("Enter number 2 (type 'exit' to stop the program):  "))
            if b != 'exit':  
                c = int(a)/int(b)
                print(float(c))
            elif a or b == 'exit':
                break
            else:
                print("You typed wrong.")
        elif amal.lower() == '3':        
            a = (input("Enter number 1:  "))
            b = (input("Enter number 2 (type 'exit' to stop the program):  "))
            if b != 'exit':  
                c = int(a)-int(b)
                print(int(c))
            elif a or b == 'exit':
                break
            else:
                print("You typed wrong.")
        elif amal.lower() == '4':        
            a = (input("Enter number 1:  "))
            b = (input("Enter number 2 (type 'exit' to stop the program):  "))
            if b != 'exit':  
                c = int(a)+int(b)
                print(int(c))
            elif a or b == 'exit':
                break
            else:
                print("You typed wrong.")
        elif amal.lower() == '5':        
            a = (input("Enter the number:  "))
            b = (input("Enter the level (type 'exit' to stop the program):  "))
            if b != 'exit':  
                c = int(a)**int(b)
                print(int(c))
            elif a or b == 'exit':
                break
            else:
                print("You typed wrong.")
        elif amal.lower() == '6':        
            b = (input("Enter the number (type 'exit' to stop the program):  "))
            if b != 'exit':  
                c = int(math.sqrt(int(b)))
                print(int(c))
            elif a or b == 'exit':
                break
            else:
                print("You typed wrong.")
        else: 
            print("You made the wrong choice.")
            break
    u = input("Do you want to perform another action (yes|no)?\n>>>  ")
    if u == 'yes':
        son2 = 1
        for a in masalalar:
            print(son2, "-", a, end= ("\n"))
            son2 += 1
        amal = (input("Enter the number of your chosen action\n>>> "))
        while True:
            if amal.lower() == '1':        
                a = (input("Enter number 1:  "))
                b = (input("Enter number 2 (type 'exit' to stop the program):  "))
                if b != 'exit':  
                    c = int(a)*int(b)
                    print(int(c))
                elif a or b == 'exit':
                    break
                else:
                    print("You typed wrong.")
            elif amal.lower() == '2':        
                a = (input("Enter number 1:  "))
                b = (input("Enter number 2 (type 'exit' to stop the program):  "))
                if b != 'exit':  
                    c = int(a)/int(b)
                    print(float(c))
                elif a or b == 'exit':
                    break
                else:
                    print("You typed wrong.")
            elif amal.lower() == '3':        
                a = (input("Enter number 1:  "))
                b = (input("Enter number 2 (type 'exit' to stop the program):  "))
                if b != 'exit':  
                    c = int(a)-int(b)
                    print(int(c))
                elif a or b == 'exit':
                    break
                else:
                    print("You typed wrong.")
            elif amal.lower() == '4':        
                a = (input("Enter number 1:  "))
                b = (input("Enter number 2 (type 'exit' to stop the program):  "))
                if b != 'exit':  
                    c = int(a)+int(b)
                    print(int(c))
                elif a or b == 'exit':
                    break
                else:
                    print("You typed wrong.")
            elif amal.lower() == '5':        
                a = (input("Enter the number:  "))
                b = (input("Enter the degree (type 'exit' to stop the program):  "))
                if b != 'exit':  
                    c = int(a)**int(b)
                    print(int(c))
                elif a or b == 'exit':
                    break
                else:
                    print("You typed wrong.")
            elif amal.lower() == '6':        
                b = (input("Enter the number (type 'exit' to stop the program):  "))
                if b != 'exit':  
                    c = int(math.sqrt(int(b)))
                    print(int(c))
                elif a or b == 'exit':
                    break
                    
                else:
                    print("You typed wrong.")
            else: 
                print("You made the wrong choice.")
                break
    elif u == 'yo\'q':    
        print("The program is over.")
    else:
        print("You made the wrong choice.")
    print("The program is over.")
else:
    print("You made the wrong choice.\nSiz noto'g'ri tanlov qildingiz.\nThe program is over.\nDastur tugadi.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    