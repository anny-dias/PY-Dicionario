'''Preencha um dicionário com os dados de 5 alunos.
- Utilize o ra do aluno como chave e uma lista de três notas como valor.
- Solicite os dados ao usuário.
Percorra o dicionário e exiba a média de cada aluno.'''


dados_alunos = {}

for i in range(5):
    ra = int(input("Insira o RA do aluno: "))
    nota1 = float(input("Insira a nota: "))
    nota2 = float(input("Insira a nota: "))
    nota3 = float(input("Insira a nota: "))
    media = (nota1 + nota2 + nota3) / 3
    dados_alunos[ra] = nota1,nota2,nota3, media 
    
for ra in dados_alunos.keys():
    print(dados_alunos)