import math

def delta(a, b, c):
        return b** 2 - 4 * a * c


def imprime_raizes(a,b,c):
        d = delta(a,b,c)
        if d == 0:
                raiz1 = (-b + math.sqrt(d)) / (2 * a)
                print("A única raiz é: ", raiz1)
        elif d < 0:
                print("Esta equação não possui raízes reais")
        else:
                raiz1 = (-b + math.sqrt(d)) / (2 * a)
                raiz2 = (-b + math.sqrt(d)) / (2 * a)
                print("A primeira raiz é: ", raiz1)
                print("A segunda raiz é: ", raiz2)


def main():
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        imprime_raizes(a, b, c)


main()



