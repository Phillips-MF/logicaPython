largura = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))
countLargura = 1
countAltura = 1
while countAltura <= altura:
    if countAltura == 1 or countAltura == altura:    
            while countLargura <= largura:
                print("#", end="")
                countLargura += 1
    else:
        while countLargura <= largura:
            if countLargura > 1 and countLargura <= (largura - 1):
                print(" ", end="")
            else:
                print("#", end="")
            countLargura += 1
    print("")
    countAltura += 1
    countLargura = 1
                        
        
        
                        
                        
                
