'''
1) Receba o salário base de um funcionário e calcule o reajuste. Considere
que o funcionário deve receber um reajuste de 15% caso seu salário seja
menor que 800 reais. Se o salário for maior ou igual a 800 e menor ou igual
a 1000, seu reajuste será de 10 %; caso seja maior que 1000, o reajuste
deve ser de 5%. Ao final do programa deverá ser exibido o antigo e o novo
salário.
'''
def lista3_ex1():
    salario_base = float(input("Digite o salário-base: "))
    if salario_base <= 0:
        return
    print("Salário antigo: %.2f" %salario_base)
    print("Salário reajustado em {}".format(f"15%: {salario_base * 1.15:.2f}" if salario_base < 800 else f"10%: {salario_base * 1.1:.2f}" if salario_base <= 1000 else f"5%: {salario_base * 1.05:.2f}"))
    # outra forma de escrita
    #print("Salário reajustado em %s" %(f"15%: {salario_base * 1.15:.2f}" if salario_base < 800 else f"10%: {salario_base * 1.1:.2f}" if salario_base <= 1000 else f"5%: {salario_base * 1.05:.2f}"))
    # outra forma de escrita
    #print("Salário reajustado em", (f"15%: {salario_base * 1.15:.2f}" if salario_base < 800 else f"10%: {salario_base * 1.1:.2f}" if salario_base <= 1000 else f"5%: {salario_base * 1.05:.2f}"))

'''
2) Receba três números que garantam a existência de uma equação completa do segundo grau.
Se existirem raízes reais exiba-as. Caso não existam raízes informe ao usuário.
Observações:
a) Condição de existência de uma equação do segundo grau: o coeficiente
que acompanha o x2 deverá ser um número diferente de zero.
b) Delta maior que zero: a equação possui duas raízes reais e distintas.
c) Delta igual à zero: a equação possui duas raízes iguais.
d) Delta menor que zero: a equação não apresenta raízes reais.
e) Equação completa do segundo grau os números que garantem a existência deverão ser diferentes de zero.
'''
def delta(a, b, c):
    return b**2 - 4 * a * c

def lista3_ex2():
    num_a = float(input("Digite um número diferente de 0: "))
    if num_a == 0:
        return
    num_b = float(input("Digite outro número diferente de 0: "))
    if num_b == 0:
        return
    num_c = float(input("Digite mais um número diferente de 0: "))
    if num_c == 0:
        return
    num_delta = delta(num_a, num_b, num_c)
    print("A equação ", end="")
    if num_delta < 0:
        print("não apresenta raízes reais.")
    elif num_delta == 0:
        print("apresenta duas raízes iguais de valor %.2f." %(-num_b / (2 * num_a)))
    else:
        print("possui duas raízes reais e distintas de valores %.2f e %.2f." %((-num_b + num_delta**0.5)/(2 * num_a), (-num_b - num_delta**0.5)/(2 * num_a)))
        
def lista3_ex2_alt():
    num_a = float(input("Digite um número diferente de 0: "))
    if num_a == 0:
        return
    num_b = float(input("Digite outro número diferente de 0: "))
    if num_b == 0:
        return
    num_c = float(input("Digite mais um número diferente de 0: "))
    if num_c == 0:
        return
    num_delta = delta(num_a, num_b, num_c)
    print("A equação {}.".format("não apresenta raízes reais" if num_delta < 0 else "apresenta duas raízes iguais de valor %.2f" %(-num_b / (2 * num_a)) if num_delta == 0 else "possui duas raízes reais e distintas de valores %.2f e %.2f" %((-num_b + num_delta**0.5)/(2 * num_a), (-num_b - num_delta**0.5)/(2 * num_a))))
'''
3) Receba três números que representam os lados de um triângulo e garantam
a existência de um triângulo. Informe ao usuário se o triângulo é isósceles,
equilátero ou escaleno.
Observações:
a) Garantir que cada lado é menor que a soma dos outros dois lados.
b) O triângulo é equilátero quando todos os lados são iguais.
c) O triângulo é isósceles quando apenas dois lados são iguais.
d) O triângulo é escaleno quando todos os lados são diferentes.
'''
def lista3_ex3():
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
    print("Triângulo {0}.".format("Equilátero" if (a == b) and (b == c) else "Escaleno" if (a != b) and (b != c) and (a != c) else "Isósceles"))

'''
4) Receba a quantidade de números positivos determinada pelo usuário. Essa
quantidade deverá também deverá ser positiva.
a) Verifique e exiba quantas vezes foram digitados números pares positivos
maiores que 10 e menores que 100.
b) Verifique e exiba quantas vezes o número zero foi digitado.
c) Verifique e exiba quantas vezes foram digitados números que são
múltiplos de 4 e 5 ao mesmo tempo.
Obs. Múltiplos e divisores são números que resultam da multiplicação por um
número natural e que dividem um número deixando resto zero. Exemplo:
Se 15 é divisível por 3, então 3 é divisor de 15, assim, 15 é múltiplo de 3.
'''
def lista3_ex4():
    lista = []
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return
    for i in range(k):
        lista.append(int(input("Digite elemento %d: " %(i + 1))))
    print("Pares 10 < p < 100:", len([n for n in lista if n > 10 and n <100]), "\nQt 0:", len([n for n in lista if n == 0]), "\nMúltiplos de 20:", len([n for n in lista if n % 20 == 0 and n > 0]))
    
'''
5) Receba o salário base e o sexo de um grupo de funcionários e calcule o
reajuste. A quantidade de funcionários deverá ser positiva e determinada
pelo usuário.
a) Considere que o funcionário deve receber um reajuste de 15% caso seu
salário seja menor que 800 reais. Se o salário for maior ou igual a 800 e
menor ou igual a 1000, seu reajuste será de 10 %; caso seja maior que
1000, o reajuste deve ser de 5%. Ao final do programa deverá ser
exibido o antigo e o novo salário.
b) Exiba o menor salário digitado dos funcionários do sexo feminino.
c) Calcule e exiba a média de salários dos funcionários.
'''
def lista3_ex5():
    lista = []
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return

    for i in range(k):
        while(True):
            salario_base = float(input(f"Digite o salário-base {i + 1}: "))
            if salario_base <= 0:
                print("Informe corretamente.")
            else:
                break
        while(True):
            sexo = input("Digite 'f' ou 'm': ").strip().lower()
            if sexo != 'f' and sexo != 'm':
                print("Informe corretamente.")
            else:
                break
        lista.append([salario_base, sexo])
    lista_f = [n[0] for n in lista if n[1] == 'f']
    print("Informados: ", lista)
    print("Reajustados:", [[round(n[0] * 1.15 if n[0] < 800 else n[0] * 1.1 if n[0] <= 1000 else n[0] * 1.05, 2), n[1]] for n in lista])
    print("Menor salário 'f': %.2f." %(min(lista_f) if len(lista_f) > 0 else 0))
    print("Média dos salários: %.2f." %(sum([n[0] for n in lista])/k))
    #print([n[0] for n in lista])
    #print([n[1] for n in lista])
    #print([n for n in lista if n[1] == 'f'])
    #print(sum([n[0] for n in lista]))

'''
6) Receba a altura e o sexo de um grupo de pessoas. A quantidade de
pessoas deverá ser positiva e determinada pelo usuário.
a) Verifique e exiba a maior a altura encontrada e qual é o sexo.
b) Calcule e mostre o seu peso ideal, utilizando as seguintes fórmulas:
 Para homens (72 * h) – 58
 Para mulheres (62,1* h) – 44.7
c) Calcule a média de pesos dos homens e das mulheres.
d) Quantos homens e quantas mulheres foram alimentados no programa.
'''
def lista3_ex6():
    lista = []
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return

    for i in range(k):
        while(True):
            altura = float(input(f"Digite a altura {i + 1}: "))
            if altura <= 0:
                print("Informe corretamente.")
            else:
                break
        while(True):
            sexo = input("Digite 'f' ou 'm': ").strip().lower()
            if sexo != 'f' and sexo != 'm':
                print("Informe corretamente.")
            else:
                break
        lista.append([altura, sexo])

    print("Todos:",lista)
    print(max([(n[0], n[1]) for n in lista]))
    print("Peso ideal m:", [round(72 * n[0] - 58) for n in lista if n[1] == 'm'], "\nPeso ideal f:", [round(62.1 * n[0] - 44.7) for n in lista if n[1] == 'f'])
    print("Peso ideal:", [[round(72 * n[0] - 58 if n[1] == 'm' else 62.1 * n[0] - 44.7, 2), n[1]] for n in lista])
    print("Média das alturas:", round(sum([n[0] for n in lista]) / k, 2))
    print("Qt homens:", len([n[1] for n in lista if n[1] == 'm']), "\nQt mulheres:", len([n[1] for n in lista if n[1] == 'f']))
        
'''
7) Receba a idade e o sexo de um grupo de nadadores. A quantidade de
nadadores deverá ser positiva e determinada pelo usuário. Verifique e exiba
a maior idade encontrada entre as nadadoras e a quantidade de vezes que
essa maior idade apareceu. Classifique-os em uma das seguintes
categorias:
a) Infantil A = 5 - 7 anos
b) Infantil B = 8-10 anos
c) Juvenil A = 11-13 anos
d) Juvenil B = 14-17 anos
e) Adulto = maiores de 18 anos
'''
def lista3_ex7():
    lista = []
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return

    for i in range(k):
        while(True):
            idade = int(input(f"Digite a idade {i + 1}: "))
            if not idade < 5:
                break
            else:
                print("Informe idade >= 5.")
        while(True):
            sexo = input("Digite 'f' ou 'm': ").strip().lower()
            if sexo in ['f', 'm']: # verifica se a variável  está contida na lista
                break
            else:
                print("Informe corretamente.")
        lista.append([idade, sexo])

    print("Todos:", lista)
    lista_f = [n for n in lista if n[1] == 'f']
    max_f = max([n[0] for n in lista_f] if lista_f != [] else [0])
    #print([n[0] for n in lista_f if n[0] == max_f])
    print("Maior f aparece:", len([n[0] for n in lista_f if n[0] == max([n[0] for n in lista_f])]), "vezes e é", max_f)
    print("Classificação:", [[n[0], n[1], "Infantil A" if n[0] < 8 else "Infantil B" if n[0] < 11 else "Juvenil A" if n[0] < 14 else "Juvenil B" if n[0] < 18 else "Adulto"] for n in lista])
'''
8) Leia quatro valores referentes a quatro notas escolares de um grupo de
alunos. A quantidade de pessoas deverá ser positiva e determinada pelo
usuário. As notas deverão se maiores ou iguais a zero e menores ou iguais
a 10. Imprimir uma mensagem dizendo que o aluno foi aprovado, se o valor
da média escolar for maior ou igual a 7.0. Se o valor da média for menor
que 7.0, solicitar a nota de exame, somar com o valor da média e obter
nova média. Se a nova média for maior ou igual a 5, apresentar uma
mensagem dizendo que o aluno foi aprovado em exame. Se o aluno não foi
aprovado, indicar uma mensagem informando esta condição. Apresentar
junto com as mensagens o valor da média do aluno, para qualquer
condição.
'''
def lista3_ex8():
    lista = []
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return

    for i in range(k):
        notas = []
        for j in range(4):            
            while(True):
                nota = float(input(f"Digite a nota {j + 1}, estudante {i + 1}: "))
                if nota < 0 or nota > 10:
                    print("Informe corretamente.")
                else:                    
                    break
            notas.append(nota)
            if j == 3:
                media = sum(notas) / 4
                print("Estudante {} {} com média {}.\n".format(i + 1, "aprovado" if media >= 7 else "reprovado", media))
                if media < 7:
                    nota = float(input(f"Digite a nota de exame, estudante {i + 1}: "))
                    media = (media + nota) / 2
                    print("Aprovado em exame.\n" if media >= 5 else "Reprovado no exame.\n")
        lista.append(notas)
    print(* lista, sep="\n", end="\n\n") 
    # '*', nesse contexto, separa os elementos da lista, permitindo a personalização do separador
'''
9) Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a 
seguir e mostre qual a classificação dessa pessoa. 
                  |                   Peso                          | 
Altura            | Até 60 | Entre 60 e 90(Inclusive) | Acima de 90 |
Menores que 1,20  |    A   |            D             |      G      |
De 1,20 a 1,70    |    B   |            E             |      H      |
Maiores que 1,70  |    C   |            F             |      I      |
'''
def lista3_ex9():
    altura = float(input("Digite a altura: "))
    if altura <= 0:
        return
    peso = float(input("Digite o peso: "))
    if peso <= 0:
        return
    print("Classificação: ", end="")
    if peso <= 60:
        print("A" if altura < 1.2 else "B" if altura < 1.7 else "C")
    elif peso <= 90:
        print("D" if altura < 1.2 else "E" if altura < 1.7 else "F")
    else:
        print("G" if altura < 1.2 else "H" if altura < 1.7 else "I")

'''
10)Calcule o valor de E da sequência abaixo. A quantidade de termos da
sequência deverá ser positiva e determinada pelo usuário.
E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / 4! + ......
'''
def fatorial(a):
    fatorial = 1
    for i in range(2, a + 1):
        fatorial *= i
    return fatorial

def lista3_ex10():
    lista = []
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return

    for i in range(1, k + 1):
        lista.append(1 / fatorial(i))
    
    #print(lista)
    print(sum(lista))

if __name__ == '__main__':
    #lista3_ex10()
    #print(fatorial(5))
    lista3_ex8()
    
