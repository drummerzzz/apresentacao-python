"""
    Escreva um algoritimo que calcule a média de um aluno com 4 bimestres
    O programa deve receber 4 notas e calcular a média da seguinte forma:
    Entrada:
        soma = b1 + b2 + b3 + b4
        media = soma / 4

    Saída:
        O programa deverá mostrar na tela se o aluno passou ou não
        se a média for maior ou igual a 7: Aprovado
        se for menor do que 5: Reprovado
        se não: Recuperação
        uma nota só pode estar entre 0 e 10
"""

def is_valid(numero: int) -> bool:
    return numero >= 0 and numero <= 10

def get_bimester_note(numero_bimestre: int, texto: str = None):
    if not texto:
        texto = f'Digite a média do {numero_bimestre}° bimestre\n'
    nota = float(input(texto))
    if is_valid(nota):
        return nota
    print('Número inválido a nota só pode estar entre 0 e 10\n')
    return get_bimester_note(numero_bimestre, texto)

def student_status(soma_das_notas: float, bismestre_number: int, allowed_recuperacao: bool = True):
    media = soma_das_notas / bismestre_number
    if media >= 7:
        print("Aprovado")
    elif media < 5 or not allowed_recuperacao:
        print("Reprovado")
    else:
        print("Recuperação")
        nota_recuperacao = get_bimester_note(0, texto="Digite a nota da recuperacao\n")
        return student_status(media + nota_recuperacao, 2, False)


notas = []
quantidade_de_bimestres = 4 # int(input("Digite a quantidade de notas"))
for i in range(1, quantidade_de_bimestres +1):
    notas.append(get_bimester_note(i))

student_status(sum(notas), len(notas))
