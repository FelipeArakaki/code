# este sinal (#) comenta uma linha; comentários são ignorados na execução do código
# Códigos em Python são salvos com extensão ".py"
# Indentação, obrigatória, define o escopo de funções e métodos.
# Cada exercício foi definido como um método; a chamada dos métodos está no fim do arquivo
'''
Para comentar um bloco (mais de uma linha),
utilize 3 apóstrofos (') seguidos na abertura e 
3 no fechamento (como neste bloco).
'''
"""
Alternativamente, utilize aspas (")
(como aqui).
"""
'''
O código é executado no "main" (principal), onde há chamada de funções e métodos,
e declaração de variáveis, sendo o "main" iniciado como segue:

if __name__ == '__main__':

Exemplos:
# exemplo1:
if __name__ == '__main__': 
    print("Hello World!") # saída/output: Hello World!

# exemplo2:
if __name__ == '__main__':
    lista1_ex1() # chama um método

# exemplo3:
if __name__ == '__main__':
    a = 2
    b = 3
    print(a + b) # saída/output: 5
'''
"""
Todo dado tem um tipo.
Os tipos primitivos de dados são: int, float, string, boolean
int (integer): representa números inteiros
float: números com ponto flutuante (números com casas decimais)
string: cadeia de caracteres
boolean: representa True ("verdadeiro") ou False ("falso")
"""
'''
Declarar variáveis:

    <nome> = <dado>

<nome> é o nome da variável; não pode conter caracteres especiais (á, ç, ?, etc) nem iniciar com números
"=" é o sinal de atribuição (o lado esquerdo recebe o valor do lado direito)
<dado> é o valor da variável

O Python infere o tipo da variável de acordo com o valor atribuído.
a = 2    # variável "a" é do tipo "int" porque "2" é do tipo "int"
b = 2.0  # "b" é "float" porque "2.0" é "float"
c = "Oi" # ""Oi"" é "string", igualmente "c" o é; string é sempre envolta por aspas ("") ou apóstrofos ('')
oi = ""  # string vazia; esta variável "oi" é uma string vazia
teste = True # "teste" é um "boolean"

Operadores matemáticos:

    +  : soma
    -  : subtração
    *  : multiplicação
    /  : divisão
    %  : resto de uma divisão
    ** : potenciação

Operadores lógicos:

  and ("e"): 1 False torna toda a expressão False; para expressão True, todas as entradas devem ser True
  or ("ou"): 1 True torna toda a expressão True; para expressão False, todas as entradas devem ser False
'''
# ******************     E X E R C Í C I O S   R E S O L V I D O S  *******************
# PARA EXECUTAR, INFORME O NOME DO MÉTODO NO "MAIN" AO FINAL DO ARQUIVO
'''
1)  Leia dois valores numéricos e exibe a diferença do maior pelo menor. Se os números forem 
iguais informe ao usuário. 
'''
def lista1_ex1(): # "def" define uma função ou método para execução no "main"; tem "()" e termina com ":"
    num1 = 0 # declara variável atribuindo valor
    num2 = 0
    num1 = int(input("Digite um número: ")) # método "input()" lê digitação do teclado;
                                            # "int()" converte em "int" o valor recebido
    num2 = int(input("Digite outro número: "))
    diferenca = num1 - num2 # declara variável atribuindo o resultado da operação matemática
    if diferenca < 0: # "if" (condicional "se"): verifica se uma expressão booleana é "True" ou "False"
                      # neste caso, se "diferenca" for menor que "0", execute o próximo comando
        diferenca = diferenca * (-1) # atribui novo resultado à mesma variável, atualizando-a
    print("Módulo da diferença:", diferenca) # "print()" exibe na tela uma "string"
    if diferenca == 0: # "==" significa igualdade; compara se dois valores são iguais
        print("Números iguais.")

def lista1_ex1_alt(): # alternativamente
    num1 = int(input("Digite um número: ")) # recebe valor, converte para "int" e atribui à variável
    num2 = int(input("Digite outro número: "))
    print("Módulo da diferença:", abs(num1 - num2) if num1 != num2 else "números iguais")
    # "abs()" retorna o módulo de um valor; "!=" significa "diferente" numa comparação
    # <expressao1> if <condicao> else <expressao2> => operador ternário
    # executa "expressao1" se a "condicao" for "True", senão "expressao2" (se for "False")
'''
2)  Receba três números onde o primeiro deve ser maior do que zero e menor que 20. O segundo 
deve  ser  negativo  e  o  terceiro  representa  um  número  qualquer.  Calcule  a  soma  de  cada 
número  elevado  ao  quadrado.  Se  a  soma  resultar  um  valor  inferior  a  1000  solicite  novos 
dados. 
'''
def lista1_ex2():
    while(True): # "while()" ("enquanto"): repete os comandos enquanto sua condição for "True"
        num1 = int(input("Digite um número de 1 a 20: "))
        if num1 < 1 or num1 > 20:
            break # interrompe o laço de repetição "enquanto"
        num2 = int(input("Digite um número negativo: "))
        if num2 >= 0:
            break
        num3 = int(input("Digite um número qualquer: "))
        res = num1**2 + num2**2 + num3**2
        if res < 1000:
            print("Informe novos dados.")
        else: # "else" ("senão"): se a condição do "if" for "False", execute o próximo comando
            print("Resultado:", res)
            break
'''
3)  Efetue a leitura de um valor inteiro qualquer e exiba o número lido e o seu módulo. O módulo 
de  um  número  positivo  é  o  próprio  número  e  o  módulo  de  um  número  negativo  é  obtido 
multiplicando-o por menos 1. 
'''
def lista1_ex3():
    num = int(input("Digite um número inteiro: "))
    if num < 0:
        num = -num # "-num" equivale a "num * (-1)"
    print("Módulo:", num)

def lista1_ex3_alt(): # encadeando funções: input() dentro de int(), dentro de abs(), dentro de print()
    print("Módulo:", abs(int(input("Digite um número inteiro: "))))
'''
4)  Faça um programa que receba via teclado o salário-base de um funcionário, calcule e mostre 
o salário a receber, sabendo-se que esse funcionário tem gratificação de 5% sobre o salário-base e 
paga imposto de 7% sobre o salário-base. 
'''
def lista1_ex4():
    gratificacao = 0.05
    imposto = 0.07
    salario_base = float(input("Informe o salário-base: ")) # snake_case: nomes com "underscore" (_)
    # "float()" converte em "float"
    salario_novo = salario_base * (1 + gratificacao - imposto)
    print("Salário novo:", salario_novo)
'''
5)  Faça um programa que receba  via teclado: o valor de um depósito , o valor da taxa de juros 
e o período.Calcule e mostre o valor do rendimento e o valor total depois do rendimento. 
'''
def lista1_ex5():
    deposito = float(input("Informe o depósito: "))
    taxa = float(input("Informe a taxa: "))
    periodo = float(input("Informe o período: "))
    montante = deposito * (1 + taxa)**periodo
    rendimento = montante - deposito
    print(f"Rendimento: {rendimento:.2f}\nMontante: {montante:.2f}")
    # "f" permite formatar como a string e as variáveis serão exibidas no "print()"
    # {variavel:.2f} -> o valor da variável terá 2 casas decimais
    # "\n" comando de "pular linha"
'''
6)  Leia dois valores numéricos e efetue a adição. Caso o resultado seja maior ou igual a 10 deve 
ser acrescido de mais 5; caso contrário, este resultado deve ser diminuído em 7. Apresente 
o resultado após a avaliação da condição. 
'''
def lista1_ex6():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    res = num1 + num2
    if res < 10:
        print("Resultado-7:", res - 7) # o "print()" permite operações matemáticas/lógicas diretamente
    else:
        print("Resultado+5:", res + 5)
'''
7)  Faça um programa que receba o ano do nascimento de uma pessoa e o ano atual, calcule e 
mostre: 
a)  A idade dessa pessoa 
b)  Quantos anos essa pessoa terá em 2020. 
'''
def lista1_ex7():
    ano_nasc = int(input("Digite seu ano de nascimento: "))
    ano_atual = int(input("Digite ano atual: "))
    print("Sua idade atual é:", ano_atual - ano_nasc, "\nSua idade em 2020 será:", 2020 - ano_nasc)
'''
8)  Receba dois números quaisquer, onde o primeiro deve ser maior que zero e o segundo menor 
ou igual a zero. Calcule e mostre na tela o produto entre eles.
'''
def lista1_ex8():
    num1 = int(input("Digite um número > 0: "))
    if num1 <= 0:
        return # "return" sem parâmetro interrompe a execução do método
    num2 = int(input("Digite um número <= 0: "))
    if num2 > 0:
        return
    # print("Produto:", num1 * num2)
    print(f'Produto: {num1 * num2}') # outra forma de escrita com variável, utilizando "f-string"
'''
9)   O custo ao consumidor de um carro novo e á soma do preço da fábrica com o percentual de 
lucro do distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que 
receba o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual 
de impostos. Calcule e mostre: 
a)  O valor correspondente ao lucro do distribuidor 
b)  O valor correspondente aos impostos 
c)  O preço final do veículo 
'''
def lista1_ex9():
    vl_fabrica = float(input("Digite preço de fábrica: "))
    pc_lucro = float(input("Digite percentual de lucro: "))
    pc_imposto = float(input("Digite percentul de imposto: "))
    print("Lucro do distribuidor:", vl_fabrica * pc_lucro)
    print("Imposto:", vl_fabrica * pc_imposto)
    print("Preço final:", round(vl_fabrica * (1 + pc_lucro + pc_imposto), 2))
    # "round()" arredonda o número de acordo com casas decimais informadas; round(numero, casas_decimais)
'''
10) Receba três números, onde o primeiro e o segundo devem ser maiores ou iguais a 100 e o 
terceiro é qualquer. Calcule e exiba o produto dos seus quadrados. 
'''
def lista1_ex10():
    num1 = int(input("Digite um número >= 100: "))
    if num1 < 100:
        return
    num2 = int(input("Digite outro número >= 100: "))
    if num2 < 100:
        return
    num3 = int(input("Digite um número qualquer: "))
    print("O produto dos seus quadrados é: %d" %(num1**2 * num2**2 * num3**2))
    # "%d" indica: o tipo de dado (inteiro) e a posição do cálculo na string (final do texto)
    # nesta formatação, o resultado do cálculo dentro de "%()" será exibido no lugar do "%d"
    # String Interpolation
'''
11) Receba dois números quaisquer, calcule e mostre na tela o resultado da divisão do segundo 
pelo primeiro. 
'''
def lista1_ex11():
    num1 = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite um número diferente 0: "))
    if num2 == 0:
        return
    print("A divisão de %d por %d é: %f" %(num1, num2, num1 / num2))
    # "%f" indica que o tipo de dado é "float"
    # os parâmetros dentro de "%()" estão na ordem de exibição (%d, %d, %f) e separados por vírgulas
'''
12) Elabore  um  programa  que  efetue  o  cálculo  do  reajuste  de  salário  de  um  funcionário. 
Considere que o funcionário deve receber um reajuste de 15% caso seu salário seja menor 
que 800 reais. Se o salário for maior ou igual a 800 e menor ou igual a 1000, seu reajuste 
será de 10 %; caso seja maior que 1000, o reajuste deve ser de 5%.Ao final do programa 
deve  apresentar o valor antigo e o novo salário. 
'''
def lista1_ex12():
    salario_base = float(input("Digite o salário-base: "))
    print("Salário-base:", salario_base)    # por padrão, print() termina com "\n"
    print("Salário reajustado em ", end="") # "end=" permite definir o término do print()
    if salario_base < 800:
        print(f"15%: {salario_base * 1.15:.2f}") # {variavel * valor:.2f} -> calcula e formata
    elif salario_base <= 1000: # "elif": contração de "else if"
        print(f"10%: {salario_base * 1.1:.2f}")
    else:
        print(f"5%: {salario_base * 1.05:.2f}")
'''
13) Leia quatro  valores  referentes  às  notas  escolares  de  um  aluno e  exiba  uma  mensagem 
dizendo que ele foi aprovado se a média for maior ou igual a 5. Caso contrário informe que 
ele  está  reprovado.  Apresente  junto  à  mensagem  o  valor  da  média  obtida  pelo  aluno
independente de ter sido aprovado ou não. As notas deverão ser maiores ou iguais a zero e 
menores ou iguais a dez. 
'''
def lista1_ex13():
    notas = [0,0,0,0] # atribui "list" (lista) com 4 valores "0" à variável
    qt_notas = len(notas) # "len()" retorna o tamanho (quantidade de elementos) da lista em int
    for i in range(qt_notas): # "for ... in ...:" itera sobre elementos de uma lista; 
                              # "i" representa cada item da lista; primeiro elemento tem índice "0"
                              # "range()" limita quantidade de iterações
        notas[i] = float(input("Digite a nota do bimestre {}: ".format(i + 1)))
        # "notas[i]": atribui à variável "notas", em seu índice "i", o valor digitado
        # ".format()": string interpolation; seus parâmetros substituem "{}" na sequência informada
        if notas[i] < 0 or notas[i] > 10:
            return
    media = sum(notas) / qt_notas # "sum()" soma o conteúdo da lista
    print("Sua média foi {0:.2f}.\nVocê foi {1}provado".format(media, "a" if media >= 5 else "re"))
    # {0:.2f} é substituído pelo parâmetro "0" do ".format()"; {1}, pelo "1"
'''
14) Receba dois números, o primeiro deve ser maior que 100, o segundo deve ser menor que 50 
e o terceiro deve ser a soma dos dois anteriores. Calcule e exiba o produto entre eles. 
'''
def lista1_ex14():
    num1 = int(input("Digite um número > 100: "))
    if num1 <= 100:
        return
    num2 = int(input("Digite um número < 50: "))
    if num2 >= 50:
        return
    num3 = num1 + num2
    print("num1 = {}\nnum2 = {}\nnum3 = {}".format(num1, num2, num3))
    print( "O produto entre num1, num2 e num3 é:", num1 * num2 * num3)
    print( "O produto entre num1, num2 e num3 é: %d" %(num1 * num2 * num3))
    print( "O produto entre num1, num2 e num3 é: {}".format(num1 * num2 * num3))
    print(f"O produto entre num1, num2 e num3 é: {num1 * num2 * num3}")
    # acima, 4 formas diferentes de print() com o mesmo resultado

'''
15) Receba dois números, o primeiro deve ser maior que 10 e menor que 25, o segundo deve ser 
maior ou igual a zero, o terceiro deve ser a soma dos dois primeiros e o quarto é o produto 
dos três números anteriores. Calcule e exiba a soma dos quadrados de cada um dos quatro 
números. Caso o resultado seja menor que 50000, solicite novos dados. 
'''
def lista1_ex15():
    while(True):
        num1 = int(input("Digite um num 10 < num < 25: "))
        if num1 <= 10 or num1 >= 25:
            return
        num2 = int(input("Digite um número >= 0: "))
        if num2 < 0:
            return
        num3 = num1 + num2
        num4 = num1 * num2 * num3
        num5 = num1**2 + num2**2 + num3**2 + num4**2
        print("num5 = %d" %(num5))
        if num5 < 50000:
            print("Insira novos dados.")
        else:
            break
'''
16) Receba  três  números  que  garantam  a  existência  de  uma  equação do segundo  grau.  Se 
existirem raízes reais exiba-as. Caso não existam raízes informe ao usuário. 
Observações: 
a)  Condição de existência de uma equação do segundo grau: o coeficiente que acompanha 
o x**2 deverá ser um número diferente de zero. 
b)  Delta maior que zero: a equação possui duas raízes reais e distintas. 
c)  Delta igual à zero: a equação possui duas raízes iguais. 
d)  Delta menor que zero: a equação não apresenta raízes reais. 
'''
def delta(a, b, c): # função "delta()" tem como parâmetros "a", "b" e "c"
    return b**2 - 4 * a * c # retorno da função é o valor calculado

def lista1_ex16():
    num_a = float(input("Digite um número diferente de 0: "))
    if num_a == 0:
        return
    num_b = float(input("Digite um número qualquer: "))
    num_c = float(input("Digite outro número qualquer: "))
    num_delta = delta(num_a, num_b, num_c) # variável recebe o retorno da função
    print("A equação ", end="")
    if num_delta < 0:
        print("não apresenta raízes reais.")
    elif num_delta == 0:
        print("apresenta duas raízes iguais de valor %.2f." %(-num_b / (2 * num_a)))
    else:
        x1 = (-num_b + num_delta**0.5)/(2 * num_a)
        x2 = (-num_b - num_delta**0.5)/(2 * num_a)
        print("possui duas raízes reais e distintas de valores %.2f e %.2f." %(x1, x2))
'''
17) Receba três números que representam os lados de um triângulo e garantam a existência de 
um triângulo. Informe ao usuário se o triângulo é isósceles, eqüilátero ou escaleno. 
Observações: 
a)  Garantir que cada lado é menor que a soma dos outros dois lados. 
b)  O triângulo é eqüilátero quando todos os lados são iguais. 
c)  O triângulo é isósceles quando apenas dois lados são iguais. 
d)  O triângulo é escaleno quando todos os lados são diferentes.  
'''
def lista1_ex17():
    while(True):
        a = int(input("Digite um número positivo: "))
        if a <= 0:
            return
        b = int(input("Digite outro número positivo: "))
        if b <= 0:
            return
        c = int(input("Digite mais um número positivo: "))
        if c <= 0:
            return
        if (a >= b + c) or (b >= a + c) or (c >= a + b):
            print("Informe novos dados.")
        else:
            break
    print("Triângulo {}.".format("Equilátero" if (a == b) and (b == c) else "Escaleno" if (a != b) and (b != c) and (a != c) else "Isósceles"))
'''
18) Receba três números que garantam a existência de uma equação completa do segundo grau. 
Se existirem raízes reais exiba-as e informe ao usuário se são iguais ou diferentes. Caso não 
existam raízes também informe ao usuário e solicite novos dados. Considerar as observações 
do ex.17.
'''
def lista1_ex18():
    while(True):
        num_a = float(input("Digite um número diferente de 0: "))
        if num_a == 0:
            return
        num_b = float(input("Digite um número qualquer: "))
        num_c = float(input("Digite outro número qualquer: "))
        num_delta = delta(num_a, num_b, num_c)
        print("A equação ", end="")
        if num_delta < 0:
            print("não apresenta raízes reais.\nInforme novos dados.")
        else:
            break
    if num_delta == 0:
        print("apresenta duas raízes iguais de valor %.2f." %(-num_b / (2 * num_a)))
    else:
        x1 = (-num_b + num_delta**0.5)/(2 * num_a)
        x2 = (-num_b - num_delta**0.5)/(2 * num_a)
        print("possui duas raízes reais e distintas de valores %.2f e %.2f." %(x1, x2))
'''
19) Faça um programa que receba a altura e o sexo de uma pessoa e que calcule e mostre o seu 
peso ideal, utilizando as seguintes fórmulas: 
  Para homens (72 * h) – 58 
  Para mulheres (62,1* h) – 44.7
'''
def lista1_ex19():
    altura = float(input("Digite altura: "))
    sexo = input("Informe sexo com 'm' ou 'f': ")
    sexo = sexo.strip() # "strip()" tira espaços vazios antes e após a letra
    sexo = sexo.lower() # "lower()" tudo em minúscula
    if sexo != 'm' and sexo != 'f': 
        return                                                      
    print("Peso ideal: %.2f." %(72 * altura - 58 if sexo == 'm' else 62.1 * altura - 44.7))

'''
20) Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a 
seguir e mostre qual a classificação dessa pessoa. 
                  |                   Peso                          | 
Altura            | Até 60 | Entre 60 e 90(Inclusive) | Acima de 90 |
Menores que 1,20  |    A   |            D             |      G      |
De 1,20 a 1,70    |    B   |            E             |      H      |
Maiores que 1,70  |    C   |            F             |      I      |
'''
def lista1_ex20():
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))
    if peso <= 60:
        print("A" if altura < 1.2 else "B" if altura < 1.7 else "C")
    elif peso <= 90:
        print("D" if altura < 1.2 else "E" if altura < 1.7 else "F")
    else:
        print("G" if altura < 1.2 else "H" if altura < 1.7 else "I")

if __name__ == '__main__':
    lista1_ex14()