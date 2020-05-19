def dodawanie():
    try:
        a = int(input('podaj piewszą liczbę(dodawanie):'))
        b = int(input('podaj drugą liczbe:'))
        print('wynik to', a + b)
    except:
        print('wystąpił błąd')
        dodawanie()


def odejmowanie():

    a = int(input('podaj piewszą liczbę(odejmowanie):'))
    b = int(input("podaj drugą liczbę:"))
    print("wynik to", a - b)


def menu():
    try:
        print("1.dodawanie")
        print("2.odejmowanie")
        wybur = int(input("wybiesz tryb:"))
        if wybur == 1:
            dodawanie()
        else:
            if wybur == 2:
                odejmowanie()
    except:
        print('wystąpił błąt')
        print("sprubuj ponownie")
        menu()


menu()
