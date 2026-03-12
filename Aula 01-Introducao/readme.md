# 🧮 Calculadora em Python com Histórico

Este é um projeto simples de **calculadora feita em Python** que permite realizar operações matemáticas básicas e armazenar um **histórico das contas realizadas**.

O programa funciona no terminal e utiliza estruturas básicas da linguagem Python.

---

## ⚙️ Funcionalidades

A calculadora possui as seguintes opções:

* **1 - Fazer conta**
* **2 - Ver histórico**
* **3 - Sair do programa**

Operações disponíveis:

* ➕ Adição
* ➖ Subtração
* ✖️ Multiplicação
* ➗ Divisão

Todas as contas realizadas são armazenadas em uma lista chamada `historico`.

---

## 📋 Como funciona o código

### 1️⃣ Lista de histórico

```python
historico = []
```

Essa lista armazena todas as operações feitas pelo usuário.

---

### 2️⃣ Loop principal do programa

```python
while True:
```

Esse loop mantém o programa rodando até o usuário escolher a opção **3 (Sair)**.

---

### 3️⃣ Registro das operações

Após cada conta, o resultado é salvo no histórico:

```python
historico.append(f"{numero1} + {numero2} = {resultado}")
```

---

### 4️⃣ Exibição do histórico

Quando o usuário escolhe a opção **2**, o programa percorre a lista:

```python
for conta in historico:
    print(conta)
```

---

## ▶️ Como executar o programa

1. Instale o **Python** no computador
2. Baixe ou clone o repositório
3. Execute o arquivo no terminal

```bash
python calculadora.py
```

---

## 💻 Exemplo de uso

```
Você desejaria realizar na calculadora?:

1- Fazer conta | 2- Ver Histórico | 3- Sair

1

Escolha a operação que vai ser realizada:

+ = Adicao | - = Subtracao | * = Multiplicacao | / = Divisao

+

Insira o primeiro número:
10

Insira o segundo número:
5

O resultado da soma será de:
15
```

---

## 📚 Conceitos de Python utilizados

* `while`
* `if / elif`
* `for`
* listas (`list`)
* `input()` e `print()`
* conversão de tipo (`float`)
* **f-strings**

---

## 🚀 Possíveis melhorias

* ✔️ Tratar erro de **divisão por zero**
* ✔️ Permitir **limpar histórico**
* ✔️ Criar **funções para cada operação**
* ✔️ Criar **interface gráfica**
* ✔️ Salvar histórico em **arquivo**

---

## 👨‍💻 Autor

Projeto desenvolvido por **Ryan Oliveira**
Estudante iniciante em **Python**.
