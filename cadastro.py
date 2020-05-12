# cadastro
def cliente(n, entrega, e, t):
	if entrega == 1:
		print(f" nome: {n}, endereco: {e}, telefone: {t} ")
	elif entrega == 2:
		print(f" nome: {n}, telefone: {t} o cliente vem buscar o produto")
		
nome = str(input(" Nome: "))
entrega = int(input("entrega? 1 para sim e 2 para nao: "))
if entrega == 1:
	endereco = str(input("Endereco:  "))
elif entrega == 2:
	endereco = "Vem Buscar "
else:
	print("Dados incorretos")
telefone = str(input("telefone:  "))

cliente(nome, entrega, endereco, telefone )