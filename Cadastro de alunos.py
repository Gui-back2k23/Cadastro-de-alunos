# --- FUNÇÕES ---

def classificar_aluno(nota):
    """Classifica a situação do aluno com a nota."""
    if nota >= 7:
        return "Aluno Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Infelizmente está reprovado"


def calcular_media(lista_alunos):
    """Calcula a média aritmética notas de todos os alunos."""
    if not lista_alunos:
        return 0
    soma_notas = 0
    for aluno in lista_alunos:
        soma_notas += aluno['nota aluno']
    return soma_notas / len(lista_alunos)


# --- PROGRAMA PRINCIPAL ---

alunos = []

while True:
    print("\n--- Novo Cadastro ---")

    # 1. Pedir Nome
    nome = input("Nome do aluno: ").strip()

    # 2. Validar Idade e Nota com tratamento de erros
    while True:
        try:
            idade = int(input(f"Idade de {nome}: "))
            if idade < 0 or idade > 120:
                print("Erro: Idade inválida. Digite um valor entre 0 e 120.")
                continue
            break
        except ValueError:
            print("Erro: Valor não numérico. Por favor, digite um número inteiro para a idade.")

    while True:
        try:
            nota = float(input(f"Nota de {nome} (0 a 10): "))
            if nota < 0 or nota > 10:
                print("Erro: Nota inválida. Digite um valor entre 0 e 10.")
                continue
            break
        except ValueError:
            print("Erro: Valor não numérico. Por favor, digite um número para a nota.")

    # 3. Salvar Dicionário e adicionar à Lista
    aluno_data = {
        "nome": nome,
        "idade": idade,
        "nota": nota,
        "situacao": classificar_aluno(nota)
    }
    alunos.append(aluno_data)

    # Controle do loop while
    continuar = input("\nDeseja cadastrar outro aluno? (s/n): ").lower()
    if continuar != 's':
        break

# --- RELATÓRIO FINAL ---

if alunos:
    media_turma = calcular_media(alunos)
    aprovados = 0
    recuperacao = 0
    reprovados = 0

    # Inicializa maior e menor nota com o primeiro aluno da lista
    maior_aluno = alunos[0]
    menor_aluno = alunos[0]

    print("\n" + "=" * 30)
    print("      RELATÓRIO FINAL")
    print("=" * 30)

    print("\nLista de Alunos:")
    for a in alunos:
        print(f"- {a['nome']}, {a['idade']} anos | Nota: {a['nota']} | Situação: {a['situacao']}")

        # Contabilização para o relatório
        if a['situacao'] == "Aprovado":
            aprovados += 1
        elif a['situacao'] == "Recuperação":
            recuperacao += 1
        else:
            reprovados += 1

        # Verificação de maior e menor nota
        if a['nota'] > maior_aluno['nota']:
            maior_aluno = a
        if a['nota'] < menor_aluno['nota']:
            menor_aluno = a

    print("-" * 30)
    print(f"Média da Turma: {media_turma:.2f}")
    print(f"Quantidade de Aprovados: {aprovados}")
    print(f"Quantidade em Recuperação: {recuperacao}")
    print(f"Quantidade de Reprovados: {reprovados}")
    print(f"Maior nota: {maior_aluno['nota']} ({maior_aluno['nome']})")
    print(f"Menor nota: {menor_aluno['nota']} ({menor_aluno['nome']})")
    print("=" * 30)
else:
    print("Nenhum aluno cadastrado.")
    print(f"Menor nota: {menor_aluno['nota']} ({menor_aluno['nome']})")
    print("=" * 30)
else:
    print("Nenhum aluno cadastrado.")
