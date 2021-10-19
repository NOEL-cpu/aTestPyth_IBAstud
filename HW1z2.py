""" v1 Шестизначный автобусный билет считается удачным, если сумма его цифр делится на 7.
 Могут ли два билета подряд быть удачными?"""
f1 = False
for x in range(0, 999999):
    d0 = 0
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    y = str(x)
    lenx = len(y)
    if lenx > 1 or lenx == 1:
       d0 = int(y[0])
    if lenx > 2 or lenx == 2:
       d1 = int(y[1])
    if lenx > 3 or lenx == 3:
       d2=int(y[2])
    if lenx > 4 or lenx == 4:
       d3=int(y[3])
    if lenx > 5 or lenx == 5:
       d4=int(y[4])
    if lenx > 6 or lenx == 6:
       d5=int(y[5])
    sumDigit=d0+d1+d2+d3+d4+d5
    krat = sumDigit % 7
 #   print(lenx)
    if krat == 0 and f1 is True:
        print("Ого такое бывает "+str(x)+"  "+ str(x-1))

    if krat == 0:
        f1 = True
    if krat  != 0:
        f1 = False
    #if x == 222:
     #   print(x)

  #  print(x)
