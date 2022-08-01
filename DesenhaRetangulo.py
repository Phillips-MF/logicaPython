largura = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))
countLargura = 1
countAltura = 1
while countAltura <= altura:
    while countLargura <= largura:
        print("#", end="")
        countLargura += 1
    print("")
    countAltura += 1
    countLargura = 1
