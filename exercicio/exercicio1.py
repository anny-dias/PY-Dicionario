'''Preencha um dicionário com as informações de 5 pessoas.
- Utilize o cpf da passoa como chave e o nome como valor.
- Solicite os dados ao usuário'''

dados_do_cliente = {}

while len(dados_do_cliente) < 5:
    cpf = input("Insira seu CPF: ")
    nome = input("Digite seu nome: ")
    if cpf not in dados_do_cliente:
        dados_do_cliente[cpf] = nome    # insere no dicionario 
    else:
        print('CPF já cadastrado. Insira novamente.')


print(dados_do_cliente)