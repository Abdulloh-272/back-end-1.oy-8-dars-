
ball = int(input("Balingizni kiriting: "))

if ball <= 100 and ball >= 90:
    print('Sizning bahoingiz 5')
    
elif ball <= 90 and ball >= 80:
    print('Sizning bahoingiz 4')
    
elif ball <= 80 and ball >= 70:
    print('Sizning bahoingiz 3')
    
else:
    print('Sizning bahoingiz 2')



harf = input('Harf kiriting: ')

if harf in 'aeiou':
    print(harf, "unli")
else:
    print(harf, 'undosh')


son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("Uchinchi sonni kiriting: "))


if son1 > son2 and son1 > son3:
    print("Eng katta son: ",son1)
elif son2 > son1 and son2 > son3:
    print("Eng katta son: ",son2)
elif son3 > son2 and son3 > son2:
    print("Eng katta son: ",son3)
