# cadastro do cliente 
# código do cliente / nome do cliente 
cadastro = {123: 'Luani', 532: 'Camis', 897: 'Lety'}
cadastro = {123: 'Luani', 
            532: 'Camis', 
            897: 'Lety'}
print(cadastro)
print(cadastro[532])

# alterar item 
cadastro[532] = 'Camis linda'
print(cadastro)

# inserir um item 
cadastro[652] = 'LuCa'
print(cadastro)

# remover um item 
cadastro.pop(652)
print(cadastro)

# busca de uma chave especifica 
codigo = int(input('Código: '))
if codigo in cadastro:
    print(f'Cliente cadastrado: {cadastro[897]}')
else: 
    print('Cliente não cadastrado')

# percorrer chaves do dicionario 
for codigo in cadastro. keys():
    print(codigo)

# percorrer os valores do dicionario
for nome in cadastro.values():
    print(nome)

# chave e valor ao mesmo tempo
for codigo, nome in cadastro.items():
    print(codigo, nome)

# preencher dicionario com inputs 
dados_cliente = {}
for i in range(3):
    codigo = int(input("Digite o código do cliente: "))
    nome = input("Digite o nome do cliente: ")
    dados_cliente[codigo] = nome
print(dados_cliente)

# dicionario armazenando listas 
alunos = {1234: [9, 7, 8],
          4565: [6, 7, 5],
          2233: [8, 9, 10]}
print(alunos[1234][0])
alunos[1234][0] = 10 
alunos[1234].append(6)
print(alunos)

lista = [alunos, cadastro]
print(lista)