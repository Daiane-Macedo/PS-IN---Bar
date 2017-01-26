vetpedido=[]
vetqtd=[]
vetpreco= [5.00, 3.00, 4.00, 3.50, 2.00]
total=0
print ('Bem vindo ao Bar Toca do Lobo')
nome=input("Entre com o seu nome:")
vetpedido.append (nome)
print ("MENU:")
print ("1 - Cerveja R$ 5,00")
print ("2 - Refrigerante R$ 3,00")
print ("3 - Suco R$ 4,00")
print ("4 - Salgado R$ 3,50")
print ("5 - Biscoito R$ 2,00")

print ("Finalizar pedido = 0")

fechar_conta=False

opcao=int(input("Digite o número do seu pedido: "))
if opcao!=0:
    vetpedido.append (opcao)
while opcao!=0:
    qtd= int (input("Digite a quantidade"))
    vetqtd.append(qtd)
    total+=float (vetpreco[opcao-1])*qtd
    opcao = int(input("Digite o número do seu pedido: "))
    vetpedido.append (opcao)
tampedido=len(vetpedido)
print("Total da conta R$:",total,)






