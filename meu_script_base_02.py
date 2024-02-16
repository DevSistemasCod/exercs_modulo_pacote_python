#### Manipulação de String ####
# Segmentar uma mensagem em uma lista de palavras.
def segmentar_mensagem(mensagem):
    palavras = mensagem.split()
    return palavras

# Substituir o caractere 'A' pelo caractere 'a' em uma frase.
def substituir_caracter(frase):
    frase_substituida = frase.replace('A', 'a')
    return frase_substituida

# Obter o tamanho de uma string.
def tamanho_da_string(frase):
    tamanho = len(frase)
    return tamanho

#################################################################
#### Exibir Conteúdo ####
# Exibir o tipo de uma variável.
def exibir_tipo(variavel):
    print(type(variavel))

# Exibir o conteúdo de uma variável.
def exibir_conteudo(variavel):
    print(variavel)
#################################################################
    
#### Validar Números ####
#Identifica números pares em uma lista.
def identificar_pares(lista):
    pares = []
    for num in lista:
        resto = num % 2
        if resto == 0:
            pares.append(num)
    return pares

#Identifica números ìmpares em uma lista.
def identificar_pares(lista):
    impares = []
    for num in lista:
        resto = num % 2
        if resto != 0:
            impares.append(num)
    return impares

# maior entre 3 números
def classificar_maior_entre_tres_numeros(num1, num2, num3):
    return max(num1, num2, num3)

# menor entre 3 números
def classificar_menor_entre_tres_numeros(num1, num2, num3):
    return min(num1, num2, num3)

# verificar se é número primo
def verificar_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False  # Se o número for divisível por i, não é primo
    return True  # Se nenhum divisor foi encontrado, o número é primo

