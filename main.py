print("Xush kelibiz, matematik savollar tizimiga")
print("Siz bu o'yinda har bir to'g'ri javob uchun 1ball olasiz!!! ")


play = input("O'yinni boshlashni xoylayszmi (ha/yo'q)")

if play == 'ha':
    print()
else:
    quit()    

print("Okay o'yin boshlandi")  
score = 0

answer = int(input("15*6= "))
if answer == 90:
    print("Tug'ri javob")
    score += 1
else:
    print("Xato javob") 


answer = int(input("11ning kvadrati nechchi? "))
if answer == 121:
    print("Tug'ri javob")
    score += 1
else:
    print("Xato javob")  
 

answer = int(input("Fabrikaga 60litr sut olib kelindi va usha kun sutning 35foizi sotildi. Qancha sut sotilgan? "))
if answer == 21:
    print("Tug'ri javob")
    score += 1
else:
    print("Xato javob")   


answer =int(input("7! =  "))
if answer == 5040 :
    print("Tug'ri javob")
    score += 1
else:
    print("Xato javob") 

print("Siz" + str(score) + "ta tug'ri javob berdiz")  
print("Siz tupladiz " + str((score / 4) * 100) + "%.")   