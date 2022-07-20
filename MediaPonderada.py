#Juntando informações sobre a matéria
def infoMateria():
    nomeMateria = input("Insira o nome da matéria: ")
    return nomeMateria

#Inforamções sobre a etapa
def infoEtapa():
    nomeEtapa = input("Insira o nome da etapa: ")
    return nomeEtapa


def infoNota(nomeEtapa):
    nota = float(input("Insira a nota da etapa " + nomeEtapa + ": "))
    if nota > 10:
        print("A nota não pode ser maior que 10")
    return nota


def infoPorcentagem():
    porcentagem = float(input("Qual a porcentagem dessa nota? "))
    if porcentagem >= 1.0:
        print("A porcentagem não pode ser maior que 1.0")
    return porcentagem

#Calculo da nota na etapa
def calculoNota(n1, p1):
    notaEtapa = n1 * p1
    return notaEtapa


nomeMateria = infoMateria()
numeroEtapa = int(input("Quantas etapas essa matéria tem? "))
contador = 0
media = 0
while contador < numeroEtapa:
    nomeEtapa = infoEtapa()
    nota = infoNota(nomeEtapa)
    porcetagem = infoPorcentagem()
    notaEtapa = calculoNota(nota, porcetagem)
    print("Sua nota na etapa: ", nomeEtapa, "%.1f" % notaEtapa)
    media = media + notaEtapa
    print("Sua nota na matéria: ", nomeMateria, "%.1f" % media)
    contador = contador + 1


if media > 6:
    print("Parabéns, você passou na matéria", nomeMateria)
else:
    print("Infelizmente, você não passou na matéria", nomeMateria)
