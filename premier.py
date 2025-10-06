n=int(input("Entrez un nombre nombre: "))
for diviseur in range (2,n):
    reste = n % diviseur
if reste == 0:
    print (f"{n}, n'est pas premier car divisible par {diviseur}")
    premier = False

if premier:
    print(n,"est premier")