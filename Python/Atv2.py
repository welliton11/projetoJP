s = input('Qual seu sexo?(f ou m): ').lower()

if s == 'f':
    print('Você poderá se aposentar com 60 anos.')
elif s =='m':
    print('Você poderá se aposentar com 65 anos')
else:
    print('Opção inválida')