#notas= int(input('Quantas notas você quer calcular? '))
#medias= 0
#lista= []

#while True:

#    n1= float(input('Digite uma nota: '))
#    lista.append(n1)
#    lista.append('+')
#    medias = medias+1
#    if medias == notas:
#        resultado= (lista)
#        print(resultado)

notas= int(input('quantas notas deseja adicionar?'))
medias= 0

for i in range(1,notas):
   nota= float(input(f'Digite a nota'))
   medias += nota

print(medias/notas)