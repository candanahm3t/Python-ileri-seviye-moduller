import sys


"""print(dir(sys))

a = int(input("a"))
b = int(input("b"))

sys.exit()# programı sona erdirir
c = int(input("c"))

sys.stderr.write("Bu bir hata mesajı\n")"""

"""for i in sys.argv:
    print(i)"""

def delta(a,b,c):

    hesap = b**2-(4*a*c)

    if hesap<0:
        print("Kök yok")

    else:
        x1 = (-b-hesap**0.5) / 2
        x2 = (-b+hesap**0.5) / 2
        return (x1,x2)

if len(sys.argv) == 4:
    print("sayının kökleri:",delta(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))

else:
    sys.stderr.write("Doğru değer girin")
    sys.stderr.flush()


   



    

