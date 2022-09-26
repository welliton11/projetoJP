resposta_certa= 10+5
resposta_do_usuario = int(input('Quanto é 10 + 5? '))
while resposta_do_usuario != resposta_certa:
    resposta_do_usuario = int(input('Quanto é 10 + 5? '))    

print('Você acertou.')