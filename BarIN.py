vetpedido=[] #vetor que guarda o numero dos pedidos
vetpreco= [5.00, 3.00, 4.00, 3.50, 2.00] #vetor com os preços (produto corresponedente: vetpedido[indice+1])
total=0
print ('Bem vindo ao Bar Toca do Lobo :D')
nome=input("Entre com o seu nome:")
vetpedido.append (nome)
print ("MENU:")
print ("1 - Cerveja R$ 5,00")
print ("2 - Refrigerante R$ 3,00")
print ("3 - Suco R$ 4,00")
print ("4 - Salgado R$ 3,50")
print ("5 - Biscoito R$ 2,00")
print("0 - Finalizar  e pedir a conta")

opcao=int(input("Digite o número do seu pedido: "))
if (opcao > 5):
    print("Pedido Inválido")
    opcao = int(input("Digite o número do seu pedido: "))

while opcao!=0:
    if (opcao<=5):
        vetpedido.append(opcao)
        qtd= int (input("Digite a quantidade"))
        total+=float (vetpreco[opcao-1])*qtd        #calcula o total da conta do cliente
        opcao = int(input("Digite o número do seu pedido: "))
    else:
        print("Pedido Inválido")
        opcao = int(input("Digite o número do seu pedido: "))
print ("Total da Conta: ",total)
print("Volte sempre, ",vetpedido[0],":)")






