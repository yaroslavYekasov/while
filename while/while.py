print("*** MÄNGUD TŠISLID ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisesta täisarv => "))))
        break
    except ValueError:
         print("See pole täisarv.")
         break #lisas break
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi teha.")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju on paaris- ja mitu paaritut numbrit")
    print()
    c=b=a #eemaldas =
    paaris =0 #eemaldas =
    paaritu = 0 #eemaldas =
    while b > 0:
        if b % 2 == 0:  #lisatud =
            paaris += 1 #vahetas kohad + ja 
        else:
            paaritu += 1 #vahetas kohad + ja
        b = b // 10
print("Numbrite arv:",paaris)
print("Paaritu arv:",paaritu)
print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("*Pöörame* sisestatud arvu ümber")
print()
b=0
while a > 0:    #asendanud mõned muutujad mugavuse
    l = a % 10
    a = a // 10
    b = b * 10       #jagas arvu tühikutega ja ühendas teises järjekorras
    b = b + l
print("*Muudetud* arv", b)
print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("Syracuse hüpoteesi testimine")
print()
if c % 2 == 0:     #lisatud ==
    print("s on paarisarv. Jagage 2 -ga.")
else:
    print("s on paaritu arv. Korrutage 3 -ga, lisage 1 ja jagage 2 -ga.")
while c > 1:    #lisatud >
    if c%2:
        c = 3*c+1  #eemaldas sulud
    c //= 2
    print(c, end=" ")
print()
print("Hüpotees on õige")