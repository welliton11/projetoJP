from retangulo import Retangulo

comprimento = (float(input('Digite a base do seu local: ')))
largura = (float(input('Digite a altura do seu local: ')))

ret1 = Retangulo(comprimento, largura)

print(f'Você precisará de {ret1.calcularPerimetro()} pisos e rodapés.')