import math
### Info figuras geometrica ###
# área da Esfera
def calcular_area_esfera(raio):
    area = ((4 * math.pi) * (raio ** 2))
    return area

#Área do triângulo
def area_triangulo(base, altura):
    return (base * altura)/2

# definir o tipo do triângulo
def definir_tipo_triangulo(lado1, lado2, lado3):
    # Validação 1 - Condição de Existência 
    if ((lado1 + lado2) > lado3) and ((lado1 + lado3) > lado2) and ((lado2 + lado3) > lado1):
    
        if(lado1 == lado2 == lado3):
            print("Triângulo equilátero")
        elif((lado1 == lado2) or  (lado1 == lado3) or (lado3 == lado2)):
            print("Triângulo isóceles")
        else:
            print("Triângulo escaleno")
    else:
        print("Condição de Existência para ser um triângulo inválida !!!")

#Calcula a área de um trapézio.
def calcular_area_trapezio(baseMaior, baseMenor, altura):
    area_trapezio = ((baseMaior + baseMenor) * altura) / 2
    return area_trapezio

#Calcula a área de um retângulo.
def calcular_area_retangulo(base, altura):
    area_retangulo = base * altura
    return area_retangulo

#Volume da esfera.
def calcular_volume_esfera(raio):
    volume = (4 / 3) * math.pi * raio ** 3
    return volume
##############################################################

### Minhas Operações ### 
# Realiza adição entre 2 números
def soma(num1, num2):
    return num1 + num2

# Realiza subtração entre 2 números
def subtracao(num1, num2):
    return num1 - num2

# Realiza multiplicação entre 2 números
def multiplicacao(num1, num2):
    return num1 * num2

# Realiza divisão entre 2 números
def divisao(num1, num2):
    if(num2 == 0):
        print("A divisão por Zero não é permitida")
    else:    
        return num1 / num2
    


##############################################################

### Tipos Contagem ### 
# Calcular Fatorial
def calcular_fatorial(numero):
    if numero < 0:
        return "O fatorial não está definido para números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

# Encontra sequência Fibonacci até o parâmetro informado
def sequencia_fibonacci(numero):
    ultimo = 1
    penultimo = 2
    print("1\n2\n2")

    for i in range(3,numero): 
        atual = ultimo + penultimo 
        print(f"{atual}")
        ultimo = penultimo 
        penultimo = atual

    
##############################################################

