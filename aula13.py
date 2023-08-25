nome='Diego'
altura= 1.83
peso = 88
imc = peso/(altura**2)

#formatação
#f-strings 
linha_1 = f'{nome} tem altura de {altura:.2f}, pesa {peso} quilos e seu IMC é de {imc:.2f}'
print(linha_1)
print(nome,'tem',altura,'de altura, pesa',peso,'quilos e seu IMC é de',imc)