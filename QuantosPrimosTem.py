def primo(n):
    count = 2
    ePrimo = True
    while n % count != 0:
        count += 1
    if count == n:
        ePrimo = True
    else:
        ePrimo = False

    return ePrimo

#Devolve a quantidade de números primos que existem antes do número passado;        
def n_primos(n):
    count = 2
    numerosPrimos = 0
    while count <= n:
        if primo(count) == True:
            numerosPrimos += 1
            count += 1
        else:
            numerosPrimos += 0
            count += 1


    return numerosPrimos
