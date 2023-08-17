# Quiz game
questions = ("1) Qual é a função da declaração 'print' em Python?",
             "2) Qual das seguintes opções é um tipo de dado numérico em Python?",
             "3) O que é um 'loop' em Python?",
             "4) Qual é a sintaxe correta para definir uma função em Python?",
             "5) Qual é a diferença entre uma lista e uma tupla em Python?")

options = (("a) Ler dados do usuário","b) Armazenar valores em uma variável","c) Exibir informações na saída padrão","d) Executar operações matemáticas"),
           ("a) String","b) Lista","c) Dicionário","d) Inteiro"),
           ("a) Um bloco de código que é executado uma única vez","b) Uma estrutura de controle para tomar decisões","c) Uma função pré-definida em Python","d) Um bloco de código que é repetido várias vezes"),
           ("a) start_function nome_da_função:","b) function nome_da_função()","c) def nome_da_função():","d) new_function nome_da_função():"),
           ("a) Listas são mutáveis e tuplas são imutáveis","b) Listas podem armazenar apenas números inteiros, enquanto tuplas podem armazenar qualquer tipo de dado","c) Listas são ordenadas e tuplas não têm ordem","d) Listas têm tamanho fixo e tuplas podem crescer dinamicamente"))

answears = ("c", "d", "d", "c", "a")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----"*15)
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Escolha entre (A, B, C, D): ").lower()
    guesses.append(guess)
    if guess == answears[question_num]:
        score += 1
        print("Resposta correta!")
    else:
        print("Resposta incorreta!")
        print(f"A resposta correta é alternativa {answears[question_num]}...")
    question_num += 1

print("\nFim!")
score = int(score / len(questions)* 100)
print("-----"*15)
print(f"Você acertou {score}%")
print("-----"*15)