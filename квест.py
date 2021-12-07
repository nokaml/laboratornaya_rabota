def cop_nor(a,b):
    print('Интенсивно - 1', '\nЛениво - 2')
    y = int(input())
    if y == 1:
        return a+5, b-30
    else:
        return a+2, b-10
def trava(a,b,c):
    print('Жухлая - 1', 'Зелёная - 2')
    y = int(input())
    if y == 1:
        return a + 10, b + 15, c
    else:
        if c < 30:
            print('Сорян, лохов не пускают на лужайку. Здоровье - 30')
            return a - 30
        elif c >= 30:
            return a + 30, b + 30, c
def draka(a,b,c):
    import random
    print('Драться с: слабым - 1(вес - 30), средним - 2(вес - 50), сильным - 3(вес - 70)')
    y = int(input())
    if y == 1:
        r = random.randint(0,2)
        summ = a//(a+30)
        if r == summ:
            if a < 30:
                return a, b+40, c
            elif a == 30:
                return a, b+20, c
            else:
                return a, b+5, c
        else:
            return a, b, c-(abs(a-30))
    if y == 2:
        r = random.randint(0,2)
        summ = a//(a+50)
        if r == summ:
            if a < 50:
                return a, b+40, c
            elif a == 50:
                return a, b+20, c
            else:
                return a, b+5, c
        else:
            return a, b, c-(abs(a-50))
    if y == 3:
        r = random.randint(0,2)
        summ = a//(a+70)
        if r == summ:
            if a < 70:
                return a, b+40, c
            elif a == 70:
                return a, b+20, c
            else:
                return a, b+5, c
        else:
            return a, b, c-(abs(a-70))
D = 10
Z = 100
Y = 20
V = 30
while D != 0 or Z != 0 or Y != 0 or V != 0:
    print('Показатели:', '\nДлина норы =', D, '\nЗдоровье =', Z, '\nУважение =', Y, '\nВес =', V)
    for i in range(1):
        D -= 2
        Z += 20
        Y -= 2
        V -= 5
    for j in range(1):
        print('Выберите действие:', '\nКопать нору - 1', '\nПоесть травки - 2', '\nПойти драться - 3', '\nПоспать весь день - 4')
        x = int(input())
        if x == 1:
            D, Z = cop_nor(D,Z)
        elif x == 2:
            Z, V, Y = trava(Z,V,Y)
        elif x == 3:
            V, Y, Z = draka(V,Y,Z)
        elif x == 4:
            D -= 2
            Z += 20
            Y -= 2
            V -= 5 