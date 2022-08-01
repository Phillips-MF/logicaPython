#Verifica se o número passado é primo.
def primo(n):
    ePrimo = True
    if n == 2 or n == 3 or n == 5 or n == 7:
        ePrimo = True
    elif n >= 4 and n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n == 1:
        ePrimo = False
    else:
        ePrimo = True

    return ePrimo


#Devolve o maior primo antes do número indicado, caso ele não seja primo.
def maior_primo(n):
    count = 2
    maiorPrimo = 2
    while count <= n:
        ePrimo = primo(count)
        if ePrimo == True:
            maiorPrimo = count
            count += 1
        else:
            count += 1 
    

    return maiorPrimo
