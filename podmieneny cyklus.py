# Podmieneny cyklus

# while _ (znamienko) cislo: == pocas niecoho, ak nieco plati


# i = 1
# while i < 21:
#     print(i, i*i)
#     i += 1


#kod na druhu mocninu

#cislo = float(input('zadaj číslo:'))

#od = 0
#do = cislo

#x = (od + do) / 2


#while abs(x**2 - cislo) > 0.001:
    if x**2 > cislo:
        do = x
    else:
        od = x
    x = (od + do) / 2


#print('druhá odmocnina', cislo, 'je', x)