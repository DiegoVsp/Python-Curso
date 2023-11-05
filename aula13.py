nome = 'Diego'
altura = input('Digite sua altura: ')
peso = input('Digite seu peso: ')
imc = int(peso)/(float(altura)**2)

# print(f'Seu IMC é de {imc:.2f}')
# formatação
# f-strings
linha_1 = f'{nome} tem altura de {altura}, pesa {peso} quilos e seu IMC é de {imc:.2f}'
print(linha_1)
print(f'{nome} tem {altura} de altura, pesa {peso} quilos e seu IMC é de {imc:.2f}')
