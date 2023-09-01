'''Preencha um dicionário com as informações de 5 produtos.
- Utilize o nome do produto como chave e o preço como valor.
- Solicite os dados ao usuário.
Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00'''

dados_produtos = {}
while len(dados_produtos) < 5:
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    if nome in dados_produtos:
        print("Produto já cadastrado. Insira novamente")
    else:
        dados_produtos[nome] = preco        # insere no dicionario 
print(dados_produtos)


for nome, preco in dados_produtos.items():
    if preco > 50:
        print(nome)