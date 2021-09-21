'''
1. Leia quinze elementos de um vetor. Após a alimentação mostre todos os elementos armazenados
no vetor.
'''
def lista4_ex1():
    lista = []
    for i in range(15):
        k = int(input(f"Digite elemento {i + 1}: "))
        lista.append(k)
    print(lista)

'''
2. Receba doze números positivos e armazene no vetor A. Após a alimentação de todos os números
mostre apenas os números maiores que 121 que estão armazenados no vetor.
'''
def lista4_ex2():
    a = []
    for i in range(12):
        k = int(input(f"Digite elemento {i+1}: "))
        a.append(k)
    print("Num > 121:", [n for n in a if n > 121])
'''
3. Armazene num vetor dez números positivos. Exiba o conteúdo do vetor. Mostre o maior número,
quantas vezes ele foi digitado e em que posições ele apareceu dentro do vetor.
'''
def lista4_ex3():
    lista = []
    for i in range(10):
        while(True):
            k = int(input(f"Digite elemento {i+1}: "))
            if k >= 0:
                break
        lista.append(k)
    maior = max(lista)
    print("Vetor: {}\nO maior {} aparece {} vezes nas posições:\n{}".format(lista, maior, len([n for n in lista if n == maior]), [index for index, n in enumerate(lista) if n == maior]))
    #print([index for index, n in enumerate(lista) if n == maior])
'''
4. Armazene no vetor A 10 elementos positivos. Construa o vetor B do mesmo tipo e dimensão. Cada
elemento do vetor B deve ser o valor negativo do elemento correspondente do vetor A. Desta
forma, se em A [1] estiver armazenado o elemento 8 deve estar em B [1] o valor –8, e assim por
diante. Apresentar o conteúdo dos dois vetores.
'''
def lista4_ex4():
    QT = 10 # qt elementos
    a = [None] * QT # aloca lista com "QT" espaços vazios
    b = [None] * QT
    for i in range(QT):
        while(True):
            k = int(input(f"Digite elemento {i + 1}: "))
            if k >= 0:
                break
        a[i] = k
        b[i] = -k
    print(a, "\n", b, sep="")

def lista4_ex4_alt(): # usando apenas um vetor, imprimindo dois
    QT = 10
    a = [None] * QT
    for i in range(QT):
        while(True):
            k = int(input(f"Digite elemento {i + 1}: "))
            if k >= 0:
                break
        a[i] = k
    print(a, "\n", [-n for n in a], sep="")
    
def lista4_ex4_alt_map(): # usando apenas um vetor, imprimindo dois usando "map()" (função de lista)
    QT = 10               
    a = [None] * QT
    for i in range(QT):
        while(True):
            k = int(input(f"Digite elemento {i + 1}: "))
            if k >= 0:
                break
        a[i] = k
    print(a, "\n", list(map(lambda x: -x, a)), sep="") # "map()" aplica uma função a cada elemento da lista
    # "lambda" cria uma função anônima, ou seja, sem nome
'''
5. O usuário poderá digitar a quantidade de números que ele deseja armazenar no vetor A desde
que esse valor seja superior a 4 e inferior ou igual a 20. Construa o vetor B da mesma dimensão
e com os mesmos elementos do vetor A. Observando que o primeiro elemento de A passa a ser
o último de B, o segundo elemento de A passa a ser o penúltimo de B e a assim por diante. Exibir
o conteúdo dos dois vetores.
'''
def lista4_ex5():
    while(True):
        qt = int(input("Digite qt entre 4 < qt <= 20: "))
        if qt <= 4 or qt > 20:
            print("Informe corretamente.")
        else:
            break
    a = [None] * qt
    b = a[:] # clona "a"
    for i in range(qt):
        while(True):
            k = int(input(f"Digite elemento {i + 1}: "))
            if k >= 0:
                break
        a[i] = k
        b[qt - i - 1] = k
    print(a, "\n", b, sep="")
    
def lista4_ex5_alt(): # usando apenas um vetor, imprimindo dois
    while(True):
        qt = int(input("Digite qt entre 4 < qt <= 20: "))
        if qt <= 4 or qt > 20:
            print("Informe corretamente.")
        else:
            break
    a = [None] * qt    
    for i in range(qt):
        while(True):
            k = int(input(f"Digite elemento {i + 1}: "))
            if k >= 0:
                break
        a[i] = k
    print(a, "\n", [n for n in a[::-1]], sep="") # a[::-1] faz a list comprehension iterar reversamente
'''
6. Leia três vetores (A, B e C) de uma dimensão com 5 elementos cada. Construa o vetor D, sendo
este a junção dos três outros vetores. Armazene no vetor D o primeiro elemento do vetor A depois
do B e do C e assim sucessivamente. Apresentar o conteúdo de todos os vetores. Exiba quantas
vezes apareceram números negativos no vetor D.
'''
def lista4_ex6():
    QT = 5
    a = [None for _ in range(QT)] # "_" no lugar de variável por desnecessidade de uso
    b = a[:]
    c = a[:]
    d = []
    for i in range(QT):
        k = int(input(f"Digite elemento {i + 1} do vetor A: "))
        a[i] = k
    for i in range(QT):
        k = int(input(f"Digite elemento {i + 1} do vetor B: "))
        b[i] = k
    for i in range(QT):
        k = int(input(f"Digite elemento {i + 1} do vetor C: "))
        c[i] = k
    for i in range(QT):
        d.append(a[i])
        d.append(b[i])
        d.append(c[i])
    print("Vetor A: {}\nVetor B: {}\nVetor C: {}\nVetor D: {}\nQt números negativos em D: {}".format(a, b, c, d, len([n for n in d if n < 0])))
'''
7. Receba a nota de dez alunos e armazene essas notas em um vetor. Calcule e mostre:
a) A média da classe;
b) A quantidade de alunos aprovados, isto é, com nota >=7;
c) A quantidade de alunos reprovados, isto é, com nota <7.
'''
def lista4_ex7():
    QT = 10
    a = list(map(lambda _: None, range(QT))) # aloca lista com "qt" espaços vazios usando "map()"
    for i in range(QT):
        while(True):
            k = float(input(f"Digite nota {i + 1}: "))
            if k >= 0 and k <= 10:
                break
            else:
                print("Informe corretamente.")
        a[i] = k
    #print(a)
    print("Média da turma: {}\nAprovados: {}\nReprovados: {}".format(round(sum(a)/QT, 2), len([n for n in a if n >= 7]), len([n for n in a if n < 7])))
    
def lista4_ex7_alt(): # usando "filter()" (função de lista), função que filtra elementos
    QT = 10
    a = [None] * QT
    for i in range(QT):
        while(True):
            k = float(input(f"Digite nota {i + 1}: "))
            if k >= 0 and k <= 10:
                break
            else:
                print("Informe corretamente.")
        a[i] = k
    #print(a)
    print("Média da turma: {}\nAprovados: {}\nReprovados: {}".format(round(sum(a)/QT, 2), len(list(filter(lambda x: x >= 7, a))), len(list(filter(lambda x: x < 7, a)))))
'''
8. Receba o peso e nome de um grupo contendo no máximo de 15 pessoas. Armazene esses dados
em dois vetores, o primeiro contendo os pesos e o segundo contendo os nomes. Calcule e mostre:
a) Quantas pessoas apresentaram peso superior ao menor peso. Armazene os nomes das
pessoas que satisfazem essa condição. Mostre o conteúdo desse vetor no programa
principal.
b) Armazene num outro vetor os pesos superiores a 55 quilos e menores ou igual a 80 quilos
das pessoas. Mostre o conteúdo desse vetor.
'''
def lista4_ex8():
    lista = []
    while(True):
        k = int(input("Digite qt até 15: "))
        if k <= 0 or k > 15:
            print("Informe corretamente.")
        else:
            break
    for i in range(k):
        while(True):
            peso = float(input(f"Digite a peso {i + 1}: "))
            if peso <= 0:
                print("Informe corretamente.")
            else:
                break
        nome = input(f"Digite nome {i + 1}: ")
        lista.append([peso, nome])
    menor = min([n[0] for n in lista])
    #print("Menor peso:", menor)
    print("Pessoas com peso maior que o menor {}: {}".format(menor, [n for n in lista if n[0] > menor]))
    print("Pessoas com peso de 55 a 88 kg:", [n for n in lista if n[0] > 55 and n[0] <= 88])
'''
9. Receba o salário e o nome de um grupo contendo no máximo 13 pessoas. Armazene esses dados
em dois vetores, o primeiro contendo os salários e o segundo contendo os nomes. Calcule e
mostre:
a) Armazene em um vetor os nomes de todas as pessoas que apresentam a maior salário.
b) Armazene num outro vetor os nomes de todas as pessoas que apresentam a menor salário
encontrada. Mostre o conteúdo de todos os vetores.
'''
def lista4_ex9(): 
    salarios = []
    nomes = []
    while(True):
        k = int(input("Digite qt até 13: "))
        if k <= 0 or k > 13:
            print("Informe corretamente.")
        else:
            break
    for i in range(k):
        while(True):
            salario = float(input(f"Digite salário {i + 1}: "))
            if salario <= 0:
                print("Informe corretamente.")
            else:
                break
        nome = input(f"Digite nome {i + 1}: ")
        salarios.append(salario)
        nomes.append(nome)
    maior = max(salarios)
    menor = min(salarios)
    print("Salários: {}\nNomes: {}\nPessoas maior salário: {}\nPessoas menor salário: {}\n".format(salarios, nomes, [n for n in salarios if n == maior], [n for n in salarios if n == menor]))
#    print([(nomes[n], salarios[n]) for n in range(k)])

def lista4_ex9_alt(): # um vetor
    lista = []
    while(True):
        k = int(input("Digite qt até 13: "))
        if k <= 0 or k > 13:
            print("Informe corretamente.")
        else:
            break
    for i in range(k):
        while(True):
            salario = float(input(f"Digite salário {i+1}: "))
            if salario <= 0:
                print("Informe corretamente.")
            else:
                break
        nome = input(f"Digite nome {i+1}: ")
        lista.append([salario, nome])

    print(* lista, sep="\n")
'''
10. Efetue a leitura de dez elementos para o vetor A. No final, apresente a somatória de todos os
elementos do vetor A que sejam ímpares. Armazene no vetor B a posição em que estão
armazenados os números ímpares. Mostre o conteúdo dos dois vetores.
'''
def lista4_ex10():
    QT = 10
    a = []
    b = []
    print(id(a))
    print(id(b))
    for indice, n in enumerate(range(QT)):
        a.append(int(input(f"Digite número posição {n}: ")))
        if a[n] % 2:
            b.append(indice)

    print(f"Lista: {a}\nPosições dos ímpares: {b}")

'''
11. Leia 8 elementos (valores inteiros) para os vetores A e B de uma dimensão do tipo vetor. Construir
vetores C e D de mesmo tipo e dimensão. O vetor C deve ser formado pelos elementos de índice
ímpar dos vetores A e B, e O vetor D deve ser formado pelos elementos de índice par dos vetores
A e B. Apresente os conteúdos de todos os vetores.
'''
def lista4_ex11():    
    QT = 8
    a = []
    b = []
    c = []
    d = []
    for indice, n in enumerate(range(QT)):
        a.append(int(input(f"Digite número posição {n}, lista 'a': ")))
        if a[n] % 2:
            c.append(indice)
        else:
            d.append(indice)

    for indice, n in enumerate(range(QT)):
        b.append(int(input(f"Digite número posição {n}, lista 'b': ")))
        if b[n] % 2:
            c.append(indice)
        else:
            d.append(indice)

    print(f"Lista 'a': {a}\nLista 'b': {b}\nLista 'c': {c}\nLista 'd': {d}")
  
if __name__ == '__main__':
    lista4_ex11()
