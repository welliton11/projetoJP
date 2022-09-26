raça = int(input('\n1. Humanos \n2. Elfos \n3. Anões \n\nDe acordo com as raças acima, digite aquela de acordo com a sua (1, 2 ou 3): '))

força =0
agilidade =0
inteligência =0
carisma =0

match raça:
    case 1:
        força = 5
        agilidade = 5
        inteligência = 5
        carisma = 5
        raça = 'Humano'
        print('Você escolheu a raça "Humano", agora escolha um tipo de classe')
    case 2:
        força = 3
        agilidade = 6
        inteligência = 8
        carisma = 3
        raça = 'Elfo'
        print('Você escolheu a raça "Elfos", agora escolha um tipo de classe')
    case 3:
        força = 7
        agilidade = 2
        inteligência = 8
        carisma = 3
        raça = 'Anão'
        print('\nVocê escolheu a raça "Anões", agora escolha um tipo de classe')

classe = int(input('\n1. Guerreiro \n2. Assassino \n3. Curandeiro \n\nDigite sua classe (1, 2 ou 3): '))

match classe:
    case 1:
        força += 12
        agilidade += 1
        inteligência += 0
        carisma += 2
        classe = 'Guerreiro'
    case 2:
        força += 0
        agilidade += 10
        inteligência += 5
        carisma += 0
        classe = 'Assassino'
    case 3:
        força += 0
        agilidade += 2
        inteligência += 5
        carisma += 8
        classe = 'Curandeiro'

print(f'\nVocê agora é um {raça} da classe {classe}, e seus atributos são: \nForça: {força} \nAgilidade: {agilidade} \nInteligência: {inteligência} \nCarisma: {carisma} ')