# Python

## Instalação

Para instalar o python basta acessar a [página oficial](https://www.python.org/downloads/) e seguir os passos conforme seu sistema operacional.

- Caso estaja usando linux ou mac, o python já vem instalado de forma nativa.
Para verificar se você já possui o python instalado, abra um terminal e execute o seguinte comando.
```bash
python --version
```
Caso receba um erro tente:
```bash
python3 --version
```

# Começando

Python é uma linguaguem de programação interpretada e de tipagem dinâmica, por isso não é necessário informar o tipo de uma variável. (Porém é uma boa prática)

## Hello World
Toda linguagem de progrmação tem o bom e velho Olá Mundo.

Crie um um arquivo chamado `main.py` e dentro dele escreva o seguinte código.

```python
print('Olá mundo')
```
Agora para executar o seu código abra o terminal dentro da mesma pasta que contém seu arquivo `main.py` e rode o seguinte comando:
```bash
python main.py
```
ou
```bash
python3 main.py
```

## Comentários
Para adicionar um comentário em um código python você deve usar o caractere de hashtag (jogo da velha #) para comentarios em linha, ou três aspas duplas para comentários em mais de uma linha.
exemplos:
```python
# Uma linha
```
```python
"""
    Mais de uma linha
"""
```

## Variáveis

### Declarando uma variável
Para declarar uma variável em python não é necessário o uso de qualquer palavra reservada como `var`, `const`, `let` etc... <br> Assim como vemos em outras linguágens como o `JavaScript` por exemplo.

Dessa forma basta somente atribuir um nome e valor para sua variável.

```python
minha_primeira_variavel_em_python = 'Meu primeiro código Python'
```

Note que utilizei um `underline` para separar as palavras, isso acontece por que o python utiliza o padrão [Snake case](https://en.wikipedia.org/wiki/Snake_case) para separar palavras em variáveis e funções. <br>

Mas então o que acontece se você tentar usar o padrão [Camel Case](https://pt.wikipedia.org/wiki/CamelCase) comum no `JAVA`e `JavaScript`? <br>
A resposta é **Nada!** Você não receberá nenhum erro, porém por convenção não é uma boa prática.

Exemplos de variáveis válidas:
```python
numero = 0
numero1 = 0
numero_1 = 0

Numero = 0 # Não recomendado
numeroZero = 0 # Não recomendado
```
Exemplos de variáveis inválidas:
```python
1numero = 0 # Não é permitido iniciar com número
numero% = 0 # Não é permitido usar caracteres especiais em qualquer parte
numero.dois = 0 # Não é permitido usar ponto
numero-dois = 0 # Não é permitido usar traço (-)
```

### Tipos variável

```python
# Tipos primitivos

texto = 'Um texto qualquer' # String com aspas simples
texto = "Um texto qualquer" # String com aspas duplas
numero = 1 # Int
numero_decimal = 1.0 # Float
verdadeiro = True # Boolean
lista = [] # Array
tupla = () # Tuple
dicionario = {} # Dict

```
## Operadores matemáticos

```python

numero_1 = 5
numero_2 = 2

soma = numero_1 + numero_2 # Adição
print(soma) # 7

subtracao = numero_1 - numero_2 # Subtração
print(subtracao) # 3

multiplicacao = numero_1 * numero_2 # Muiltiplicação
print(multiplicacao)  # 10

divisao = numero_1 / numero_2 # Divisão
print(divisao) # 2.5

divisao_inteira = numero_1 // numero_2 # Divisão Inteira
print(divisao_inteira) # 2

modulo = numero_1 % numero_2 # Modulo ou Resto
print(modulo)  # 1

exponenciacao = numero_1 ** numero_2 # Exponenciação
print(exponenciacao) # 25

```

## Operadores lógicos

```python
==	# Igual 
!=	# Diferente
>	# Maior que
>=	# Maior ou igual
<	# Menor que	
<=	# Menor ou igual
```

Operadores pythônicos
```python
and # e
or  # ou
in  # em
not # negação 
```
Exemplos:

```python
if 5 == 5:
    # True
if 5 != 5:
    # False
if 6 > 5:
    # True
if 6 >= 5:
    # True
if 6 < 5:
    # False
if 6 <= 5:
    # False
if 5 == 5 and 6 == 6:
    # True
if  5 != 5 or 6 == 6:
    # True
if  'a' in 'abc':
    # True
if not 'a' == 'b':
    # True
```

### Importante!!!
Python não usa (parenteses) ou {chaves} para delimitar escopo, ao invés disso a propria identação do código é usada para delimitar o escopo de condições, funções, classes e métodos.

## Laços de repetição

Na maioria das linguagens de programação de computador, um laço é uma instrução de fluxo de controle que permite que o código seja executado repetidamente com base em uma determinada condição booleana.

### **While**
```python
# Nesse exemplo o laço executará 5 vezes
count = 0
while count < 5:
    count += 1
```

Exemplo de loop infinito

```python
# Nesse exemplo o laço executará enquanto não for forçada a parada do mesmo
count = 0
while True:
    count += 1
```


### **For**
Na maioria das linguágens o `for` funciona semelhante ao `while` a diferença é que ao usar o `for` já se sabe quantos loops são necessários para realizar a tafefa desejada.

Imagine que temos o seguinte array [10, 20, 30, 40, 50] e queremos printar seus valores na tela.
### Como fariamos isso?

Se estivessemos programando em `C++` teriamos algo como:
```c++
int contador; //variável de controle do loop
int numeros[5] = {10, 20, 30, 40, 50}; // lista
for(contador = 1; contador <= 10; contador++) {
    printf("%d\n", numeros[contador]);
}
```
Em python o `for` da mesma forma, porém agindo diretamente como um [iterador](https://cienciaprogramada.com.br/2021/08/iteradores-e-iteraveis-em-python/), isso só facilita nossa vida pois não há necessidade de declarar um contador.

```python
lista = [10, 20, 30, 40, 50]
for numero in lista:
    print(numero)
```
Dessa forma ao executar o código acima o resultado seria o mesmo que:
```python
print(lista[0]) # 10
print(lista[1]) # 20
print(lista[2]) # 30
print(lista[3]) # 40
print(lista[4]) # 50
```

## Convertendo dados

* Convertendo string para inteiro
```python
numero_em_texto = '1'
numero_inteiro = int(numero_em_texto)
print(numero_inteiro) # 1
```

* Convertendo string para float
```python
numero_em_texto = '1'
numero_decimal = float(numero_em_texto)
print(numero_decimal)  # 1.0
```

* Convertendo string para boolean
```python
numero_em_texto = '1'
numero_boolean = bool(numero_em_texto)
print(numero_boolean) # True
```

* Convertendo inteiro para boolean
```python
numero_em_texto = 1
numero_boolean = bool(numero_em_texto)
print(numero_boolean) # True
```
```python
numero_em_texto = 0
numero_boolean = bool(numero_em_texto)
print(numero_boolean) # False
```

## Entrada e Saída de dados:

### Entrada
Para fazer uma entrada de dados use a palavra reservada `input` da seguinte forma:

```python
nome = input('Digite seu nome') # João
```
Importante a função `input` retorna uma string, por isso é preciso converter a entrada de dados para outros tipos caso necessário

Exemplo:

```python
idade = int(input('Digite sua idade')) # 28
nota = float(input('Digite a nota')) # 7.5
```
### Saída
Para sáida de dados já vimos usamos a função `print`, ela imprime um valor na tela.

```python
print('Exibe um texto na tela')
```
```python
print('Exibe um texto na tela', 'outro texto')
```
```python
print('Exibe um texto na tela', 0, 'com número')
```
```python
print('Exibe um texto na tela', False, 'com boolean')
```


# Agora que já sabe o básico

## Tente fazer o seguinte desafio

```python

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
```