'''
1)  Gere e exiba cada uma das seqüências abaixo com uma quantidade k de 
termos determinados pelo usuário. 
i.  3, 6, 9, 12, 15,... 
ii.  1/4, 1/8, 1/12, 1/16, 1/20,... 
iii.  1/8, 3/16, 5/24, 7/32, 9/40, 11/48,... 
iv.  2/3, 4/6, 6/9, 8/12,... 
v.  2/5, 4/10, 6/15, 8/20, 10/25, 12/30,... 
vi.   4/8, 1, 36/24, 2, 100/40, 144/48,... 
'''
# i.  3, 6, 9, 12, 15,... 
def lista2_ex1_i():
    k = int(input("Informe qt k de termos: "))
    if k <= 0:
        return
    for i in range(k):
        print(3 * (i + 1), end="")
        if i < k - 1:
            print(", ", end="")

def lista2_ex1_i_alt(): # com list comprehension
    k = int(input("Informe qt k de termos: "))
    if k <= 0:
        return
    print("List comprehension:", [3 * (n + 1) for n in range(k)])
    # list comprehesion: gera uma nova lista a partir de outra, iterando sobre seus elementos
    # neste caso, a lista original será definida pelo "k" em "range(k)"
    # ainda neste caso, para cada "n" da lista, calcule a expressão "3*(n+1)" e gere a nova lista

def lista2_ex1_i_alt2(): # com list comprehension e em uma linha
    print("List comprehension:", [3 * (n + 1) for n in range(int(input("Código em uma linha\nInforme qt k de termos: ")))])

# ii.  1/4, 1/8, 1/12, 1/16, 1/20,... 
def lista2_ex1_ii():
    k = int(input("Informe qt k de termos: "))
    if k <= 0:
        return
    for i in range(k):
        print("1/", 4 * (i + 1), sep="", end="") 
        # "sep=" define o separador dos argumentos do print(); por padrão é um espaço simples
        if i < k - 1:
            print(", ", end="")

def lista2_ex1_ii_alt(): # com list comprehension
    k = int(input("Informe qt k de termos: "))
    if k <= 0:
        return
    print("List comprehension (string):\n", ["1/" + str(4 * (n + 1)) for n in range(k)], sep="")
    # neste caso, o retorno é string
    print("List comprehension (float):\n", [round(1 / (4 * (n + 1)), 5) for n in range(k)], sep="")
    # neste caso, o retorno é float

# iii.  1/8, 3/16, 5/24, 7/32, 9/40, 11/48,... 
def lista2_ex1_iii():
    k = int(input("Informe qt k de termos: "))
    if k <= 0:
        return
    for i in range(k):
        print(2 * i + 1, "/", 8 * (i + 1), sep="", end="")
        if i < k - 1:
            print(", ", end="")

def lista2_ex1_iii_alt(): # com list comprehension
    k = int(input("Informe qt k de termos: "))
    if k <= 0:
        return
    print("List comprehension (string):\n{}".format([str(2 * n + 1) + "/" + str(8 * (n + 1)) for n in range(k)]))
    print("List comprehension (float):\n", [round((2 * n + 1)/(8 * (n + 1)), 5) for n in range(k)], sep="")

# iv.  2/3, 4/6, 6/9, 8/12,... 
def lista2_ex1_iv():
    k = int(input("Informe qt k de termos: "))
    if k <= 0:
        return
    for i in range(k):
        print(2 * (i + 1), "/", 3 * (i + 1), sep="", end="")
        if i < k - 1:
            print(", ", end="")

def lista2_ex1_iv_alt():
    k = int(input("Informe qt k de termos: "))
    if k <= 0:
        return
    print("List comprehension (string):\n", [str(2 * (i + 1)) + "/" + str(3 * (i + 1)) for i in range(k)], sep="")

def lista2_ex1_iv_alt2(): # com list comprehension e em uma linha
    print("List comprehension (string):\n", [str(2 * (i + 1)) + "/" + str(3 * (i + 1)) for i in range(int(input("Código em uma linha\nInforme qt k de termos: ")))])

# v.  2/5, 4/10, 6/15, 8/20, 10/25, 12/30,... 
def lista2_ex1_v():
    k = int(input("Informe qt k de termos: "))
    if k <= 0:
        return
    for i in range(k):
        print(2 * (i + 1), "/", 5 * (i + 1), sep="", end="")
        if i < k - 1:
            print(", ", end="")

def lista2_ex1_v_alt(): # com list comprehension
    k = int(input("Informe qt k de termos: "))
    if k <= 0:
        return
    print("List comprehension (string):\n", [str(2 * (i + 1))+"/"+str(5 * (i + 1)) for i in range(k)], sep="")

def lista2_ex1_v_alt2(): # com list comprehension e em uma linha
    print("List comprehension (string):\n", [str(2 * (i + 1))+"/"+str(5 * (i + 1)) for i in range(int(input("Código em uma linha\nInforme qt k de termos: ")))], sep="")

# vi.   4/8, 1, 36/24, 2, 100/40, 144/48,... 
def lista2_ex1_vi():
    k = int(input("Informe qt k de termos: "))
    if k <= 0:
        return
    for i in range(k):
        numerador = (2 * (i + 1))**2
        denominador = 8 * (i + 1)
        print(int(numerador / denominador) if numerador % denominador == 0 else str(numerador) + "/" + str(denominador), sep="", end="")
        # str() converte um valor para o tipo "string"
        # "+" com strings serve para concatenação
        if i < k - 1:
            print(", ", end="")

def lista2_ex1_vi_alt(): # com list comprehension
    k = int(input("Informe qt k de termos: "))
    if k <= 0:
        return
    print("List comprehension (str e int):\n", [int((2 * (n + 1))**2 / (8 * (n + 1))) if n % 2 == 1 else str((2 * (n + 1))**2)+"/"+str(8 * (n + 1)) for n in range(k)], sep="")

def lista2_ex1_vi_alt2(): # com list comprehension em uma linha
    print("List comprehension (str e int):\n", [int((n + 1) / 2) if n % 2 == 1 else str((2 * (n + 1))**2) + "/" + str(8 * (n + 1)) for n in range(int(input("Código em uma linha\nInforme qt k de termos: ")))], sep="")

'''
2)  Receba  a  quantidade K  de  números  quaisquer.  K  representa  essa 
quantidade  e  deve  ser  digitada  pelo  usuário.  A  variável Num armazena 
cada uma dos K números digitados e  deverá ser alimentada pelo usuário. 
Verifique e exiba a quantidade de números positivos digitada.
'''
def lista2_ex2():
    lista = [] # declara uma lista vazia
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return
    for i in range(k):
        lista.append(int(input(f"Digite elemento {i + 1}: "))) # "append()" insere um dado na lista
    positivos = []
    for i in lista:
        if i > 0:
            positivos.append(i)
    print("Qt positivos:", len(positivos), "\nLista positivos:", positivos)

def lista2_ex2_alt():
    lista = [] # declara uma lista vazia
    for i in range(int(input("Digite qt de elementos (usando list comprehension): "))):
        lista.append(int(input(f"Digite elemento {i + 1}: ")))
    positivos = [n for n in lista if n > 0]
    # para cada elemento "n" em "lista", se satisfizer a condição "n>0", inclua na nova lista
    print("Qt positivos:", len(positivos), "\nLista positivos:", positivos)
'''
3)  Receba  a  quantidade  de  idades  de K  indivíduos.  K  representa  essa 
quantidade  e  deve  ser  digitada  pelo  usuário.  A  variável Idade armazena 
cada  uma  das  K  idades  digitadas.  Calcule  e  mostre  a  somatória  dessas 
idades.  
'''
def lista2_ex3():
    idades = []
    for i in range(int(input("Digite qt de indivíduos: "))):
        while(True):
            idade = int(input("Idade %d: " %(i + 1)))
            if idade >= 0:
                idades.append(idade)
                break
    print("Soma das idades:", sum(idades))
'''
4)  Receba K números. Exiba a quantidade de números pares negativos e 
quantas vezes o número zero foi digitado.  
Obs1: K representa a quantidade de números digitados pelo usuário. 
Obs2: A variável Num representa cada número digitado pelo usuário. 
'''
def lista2_ex4():
    lista = []
    for i in range(int(input("Digite qt de elementos: "))):
        lista.append(int(input("Elemento %d: " %(i + 1))))
    pares_negativos = [n for n in lista if n < 0 and n % 2 == 0]
    zeros = [n for n in lista if n == 0]
    print("Qt pares negativos: {0}\nLista pares negativos: {1}\nQt zeros: {2}".format(len(pares_negativos), pares_negativos, len(zeros)))
'''
5)  Receba K números positivos. Cada número recebido deverá ser 
armazenado na variável Num e a variável K representa a quantidade de 
números solicitada pelo usuário. Exiba a quantidade de números divisíveis 
por 2 e 3 ao mesmo tempo.  
'''
def lista2_ex5():
    lista = []
    for i in range(int(input("Digite qt de elementos: "))):
        lista.append(int(input("Elemento %d: " %(i + 1))))
    divisivel_por_6 = [n for n in lista if n % 6 == 0 and n != 0]
    print("Qt elementos divisíveis por 6:", len(divisivel_por_6))
'''
6)  Receba  via  teclado  um  número  X,  onde  este  número  representa  a 
quantidade de termos que o usuário deseja. H representa cada um desses 
números, calcule o produto dos X números. 
OBS: H deve ser maior ou igual a 15. 
'''
def lista2_ex6():
    prod = 1
    x = int(input("Digite qt de elementos: "))
    if x <= 0:
        return
    for i in range(x):
        while(True):
            h = int(input(f"Digite elemento {i + 1}: "))
            if h >= 15:
                prod *= h
                break
        # "*=": multiplicação com atribuição; executa a multiplicação e atribui o novo valor à variável
    print(f"Produto dos números: {prod}")
'''
7)  Receba  a  quantidade  de  pesos de N  pessoas.  N  representa  essa 
quantidade  e  deve  ser  digitada  pelo  usuário.  A  variável Peso armazena 
cada  um  do  K  pesos  digitados.  Calcule  e  mostre a  média  dos  pesos 
digitados.. 
'''
def lista2_ex7():
    pesos = []
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return
    for i in range(k):
        pesos.append(float(input(f"Peso {i + 1}: ")))
    print("Média dos pesos: %.2f." %(sum(pesos) / k))
    
def lista2_ex7_alt():
    pesos = []
    for i in range(int(input("Digite qt de elementos: "))):
        pesos.append(float(input(f"Peso {i + 1}: ")))
    print("Média dos pesos: %.2f." %(sum(pesos) / len(pesos) if pesos != [] else 0))
'''
8)  Mostre na tela a soma e o produto dos K primeiros naturais.  
OBS: K representa a quantidade de números naturais solicitado  
via teclado   pelo usuário. Os números naturais deverão  
ser gerados pelo programador. 
0, 1, 2, 3, 4, 5, 6,.... 
'''
def lista2_ex8():
    produto = 1
    lista = []
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return
    for i in range(k):
        lista.append(i + 1)
        produto *= (i + 1)
    print(f"Lista: {lista}\nSoma: {sum(lista)}\nProduto: {produto}")
'''
9)  Receba  a  quantidade K  de  números  quaisquer.  K  representa  essa 
quantidade  e  deve  ser  digitada  pelo  usuário.  A  variável Num armazena 
cada uma dos K números digitados e  deverá ser alimentada pelo usuário. 
Verifique e exiba a quantidade de números negativos superiores ou igual a 
-23 e inferiores a -16.  
'''
def lista2_ex9():
    lista = []
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return
    for i in range(k):
        lista.append(int(input(f"Digite elemento {i + 1}: ")))
    lista_verificada = [n for n in lista if n > -23 and n < -16]
    print(lista_verificada, "\nQt elementos:", len(lista_verificada))
    
def lista2_ex9_alt():
    lista = []
    for i in range(int(input("Digite qt de elementos: "))):
        lista.append(int(input(f"Digite elemento {i + 1}: ")))
    lista_verificada = [n for n in lista if n > -23 and n < -16]
    print(lista_verificada, "\nQt elementos:", len(lista_verificada))
'''
10) Calcule e mostre a média dos K primeiros pares e múltiplos de  cinco..  
OBS: K representa a quantidade de números pares solicitado via teclado pelo 
usuário. Os números pares deverão ser gerados pelo programador. 
2, 4, 6, 8, 10,...   
'''
def lista2_ex10():
    pares = []
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return
    for i in range(1, k + 1): # "range(valor_inicial, valor_final_exclusivo)"
        pares.append(2 * i)
    par_multiplo_5 = [n for n in pares if n % 5 == 0]
    print(pares, "\nMédia dos pares múltiplos de 5:", sum(par_multiplo_5) / len(par_multiplo_5) if par_multiplo_5 != [] else 0)

def lista2_ex10_alt():
    pares = [2 * n for n in range(1, int(input("Digite qt de elementos: ")) + 1)]
    par_multiplo_5 = [n for n in pares if n % 5 == 0]
    print(pares, "\nMédia dos pares múltiplos de 5:", sum(par_multiplo_5) / len(par_multiplo_5) if par_multiplo_5 != [] else 0)
'''
11) Receba K  números  inteiros  quaisquer,  K  representa  a  quantidade  de 
termos  solicitada  pelo  usuário  e  cada  termo  pode  ser  representado  pela 
variável N.  Exiba  a  quantidade  de  números  positivos  recebidos  e  a média 
dos números ímpares. 
'''
def lista2_ex11():
    lista = []
    k = int(input("Digite quantidade de elementos: "))
    if k <= 0:
        return
    for i in range(k):
        lista.append(int(input(f"Digite elemento {i + 1}: ")))
    impares = [n for n in lista if n % 2 != 0]
    print(f"Qt positivos: {len([n for n in lista if n > 0])}\nMédia ímpares: {sum(impares) / len(impares) if len(impares) > 0 else 0:.2f}")

def lista2_ex11_alt():
    lista = []
    for i in range(int(input("Digite quantidade de elementos: "))):
        lista.append(int(input(f"Digite elemento {i + 1}: ")))
    impares = [n for n in lista if n % 2 != 0]
    print(f"Qt positivos: {len([n for n in lista if n > 0])}\nMédia ímpares: {sum(impares) / len(impares) if len(impares) > 0 else 0:.2f}")
''' 
12) Leia um número inteiro representado pela variável N até que N seja igual a 
zero. Exiba uma mensagem informando se o número é par ou ímpar.
'''
def lista2_ex12():
    while(True):
        n = int(input("Digite um número: "))
        if not n != 0: # "not" inverte valor lógico da expressão
            print("Saindo...")
            break
        else:
            print("Par" if n % 2 == 0 else "Ímpar", end="\n\n")
''' 
13) Receba K  números  quaisquer,  K  representa  a  quantidade  de  termos 
solicitada pelo usuário e cada termo pode ser representado pela variável N. 
Exiba o  maior número digitado.
'''
def lista2_ex13():
    lista = []
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return
    for i in range(k):
        lista.append(int(input(f"Digite elemento {i + 1}: ")))
    print("O maior é:", max(lista)) # max() (função de listas) retorna o maior valor da lista
    
def lista2_ex13_alt():
    lista = []
    for i in range(int(input("Digite qt de elementos: "))):
        lista.append(int(input(f"Digite elemento {i + 1}: ")))
    print("O maior é:", max(lista) if lista != [] else "lista vazia")
''' 
14) Receba  a  quantidade  de  salários  de K  indivíduos.  K  representa  essa 
quantidade  e  deve  ser  digitada  pelo  usuário.  A variável Salário armazena 
cada  uma  dos  K  salários  digitados.  Calcule  e  mostre  a  somatória  dos 
salários  superiores  a  3  salários  mínimos  e  inferior  ou  igual  a  7  salários 
mínimos. Exiba também o maior e o menor salário encontrado.
'''
def lista2_ex14():
    SALARIO_MINIMO = 1100 # notação de constantes; "uppercase" (maiúsculos) por convenção
    lista = []
    k = int(input("Digite qt de salários: "))
    if k <= 0:
        return
    for i in range(k):
        while(True):
            aux = float(input(f"Digite salário {i + 1}: "))
            if aux > 0:
                lista.append(aux)
                break
    soma_intervalo = [n for n in lista if n > 3 * SALARIO_MINIMO and n <= 7 * SALARIO_MINIMO]
    print("Soma dos salários maiores que 3x o mínimo e menores que 7x o mínimo: {0:.2f}\nMaior: {1:.2f}\nMenor: {2:.2f}".format(sum(soma_intervalo), max(lista), min(lista)))
    # min() (função de listas) retorna o menor valor da lista
    
'''  
15) Receba  a  quantidade  de  pesos  de N  pessoas.  N  representa  essa 
quantidade  e  deve  ser  digitada  pelo  usuário.  A  variável Peso armazena 
cada  um  do  K  pesos  digitados.  Calcule  e  mostre  a  média  dos  pesos 
superiores ou iguais a 70 quilos e inferiores ou iguais a 85,5 e a quantidade 
de pessoas que apresentam pesos superiores a 75 quilos. Exiba também o 
menor e o maior peso encontrado.  
'''
def lista2_ex15():
    pesos = []
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return
    for i in range(k):
        pesos.append(float(input(f"Peso {i + 1}: ")))    
    pesos_intervalo = [n for n in pesos if n >= 70 and n <= 85.5]
    print("A média dos pesos 70 <= n <= 85.5 é: {0:.2f}.\nQt pesos > 75: {1}\nMaior: {2:.2f}\nMenor: {3:.2f}".format(sum(pesos_intervalo) / len(pesos_intervalo) if len(pesos_intervalo) != 0 else 0, len([n for n in pesos if n > 75]), max(pesos), min(pesos)))
    print("\nTeste abaixo")
    print([n for n in pesos if n > 75])
'''
16) Receba  a  quantidade K  de  números  positivos.  K  representa  essa 
quantidade  e  deve  ser  digitada  pelo  usuário.  A  variável Num armazena 
cada  uma  dos  K  números  digitados.  Calcule  e  mostre  a  quantidade  de 
números ímpares e a média dos números pares superiores a 20.  
'''
def lista2_ex16():
    lista = []
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return
    for i in range(k):
        while(True):
            n = int(input(f"Digite elemento {i + 1}: "))
            if n >= 0:
                lista.append(n)
                break
    pares_maiores_20 = [n for n in lista if n > 20]
    print(f"Qt ímpares: {len([n for n in lista if n % 2 != 0])}\nMédia dos > 20: {sum(pares_maiores_20) / len(pares_maiores_20) if len(pares_maiores_20) > 0 else 0}")
'''
17) Receba  a  quantidade K  de  números  quaisquer.  K  representa  essa 
quantidade  e  deve  ser  digitada  pelo  usuário.  A  variável Num armazena 
cada  uma  dos  K  números  digitados.  Calcule  e  mostre  a  quantidade  de 
números positivos divisíveis por 3, a média dos números negativos. Exiba 
também o maior número encontrado e quantas vezes ele apareceu.
'''
def lista2_ex17():
    lista = []
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return
    for i in range(k):
        lista.append(int(input(f"Digite elemento {i + 1}: ")))
    negativos = [n for n in lista if n < 0]
    print(f"Qt positivos divisíveis por 3: {len([n for n in lista if n > 0 and n % 3 == 0])}\nMédia dos negativos: {sum(negativos) / len(negativos) if len(negativos) > 0 else 0}\nMaior: {max(lista)}\nQt ocorrências do maior: {lista.count(max(lista))}")
    # count() (função de listas); conta número de ocorrências de um parâmetro
'''  
18) Gere  a  seguinte  seqüência  abaixo  para  K  termos.  K  representa  a 
quantidade  de  números  que  o  usuário  gostaria  quer  fosse  exibida  dessa 
seqüência. Mostre também a somatória apenas dos números divisíveis por 
3 dessa seqüência. 
1, 1, 2, 3, 5, 8, 13, 21,..... 
'''
def lista2_ex18():
    a = 1
    lista = []
    k = int(input("Digite qt de elementos: "))
    if k <= 0:
        return
    for i in range(k):
        lista.append(a) if i <= 1 else lista.append(lista[i - 1] + lista[i - 2])
    print(f"{lista}\nSoma dos divisíveis por 3: {sum([n for n in lista if n % 3 == 0])}")

def lista2_ex18_alt_0(): # fibonacci inicial 0, 1
    lista = []
    for i in range(int(input("Digite qt de elementos: "))):
        lista.append(i) if i <= 1 else lista.append(lista[i - 1] + lista[i - 2])
    print(f"{lista}\nSoma dos divisíveis por 3: {sum([n for n in lista if n % 3 == 0])}")
    
def lista2_ex18_alt_1(): # fibonacci inicial 1, 1
    lista = []
    for i in range(int(input("Digite qt de elementos: "))):
        lista.append(1) if i <= 1 else lista.append(lista[i - 1] + lista[i - 2])
    print(f"{lista}\nSoma dos divisíveis por 3: {sum([n for n in lista if n % 3 == 0])}")
'''
19) Solicite ao usuário um número maior ou igual a zero e inteiro representado 
pela variável Num. Calcular o fatorial desse número. 
OBS: O Fatorial de zero e de um é um. 
Exemplo de cálculo do Fatorial:  
5! =5 * 4 * 3 * 2 * 1     ou 
5! =1 * 2 * 3 * 4 *5  
 '''
def lista2_ex19():
    fatorial = 1
    for i in range(2, 1 + int(input("Digite um positivo: "))):
        fatorial *= i
    print(f"Fatorial: {fatorial}")
    
import functools # importa biblioteca "functools"
                 # bibliotecas são importadas nas primeiras linhas por convenção

def lista2_ex19_alt():
    k = int(input("Digite um positivo: "))
    print("Fatorial:", functools.reduce(lambda x, y: x * y, range(2, k + 1)) if k > 1 else 1)
    # "reduce()" (função de lista) agrega valores de uma lista

if __name__ == '__main__':
    lista2_ex1_iii_alt()