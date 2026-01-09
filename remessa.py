''' 
DESAFIO:

Uma produtora e exportadora de papéis para embalagens precisa calcular o valor final de suas exportações. Cada remessa possui um peso em toneladas e um preço por tonelada em dólares. Além disso, dependendo do tipo de cliente, a empresa oferece descontos:

- Novo cliente: sem desconto
- Cliente fidelizado: 5% de desconto
- Cliente premium: 10% de desconto

O programa deve calcular o valor total da remessa considerando o peso, o preço por tonelada e o desconto aplicável, retornando o valor final a ser pago pelo cliente.

ENTRADA:
- Um número decimal representando o peso da carga em toneladas.
- Um número decimal representando o preço por tonelada em dólares.
- Uma string representando o tipo de cliente ("Novo cliente", "Cliente fidelizado", "Cliente premium").

SAÍDA:
- O programa deverá retornar o valor final da exportação (em dólares), já com o desconto aplicado, formatado com duas casas decimais.
'''

from tabulate import tabulate

# Leitura do peso da carga
while True:
    try:
        peso = float(input("Peso da carga (t): "))
        break
    except ValueError:
        print("Peso inválido. Insira um número.\n")

# Leitura do preço por tonelada
while True:
    try:
        preco_por_tonelada = float(input("Preço por tonelada ($): "))
        break
    except ValueError:
        print("Preço inválido. Insira um número.\n")

# Leitura do tipo de cliente
while True:
    try:
        tipo_cliente = int(input("Tipo de cliente (1- Novo, 2- Fidelizado, 3- Premium): "))
        if tipo_cliente not in (1, 2, 3):
            raise ValueError
        break
    except ValueError:
        print("Tipo de cliente inválido. Escolha 1, 2 ou 3.\n")

# Cálculo do valor total
valor_total = peso * preco_por_tonelada

# Aplicação do desconto
descontos = [
    {'id': 1, 'tipo_cliente': 'Novo', 'desconto': 0},
    {'id': 2, 'tipo_cliente': 'Fidelizado', 'desconto': 0.05},
    {'id': 3, 'tipo_cliente': 'Premium', 'desconto': 0.10}
]

for d in descontos:
    if tipo_cliente == d["id"]:
        cliente = d["tipo_cliente"]
        desconto = d["desconto"]

valor_final = valor_total * (1 - desconto)

# Dados para a tabela
exportacoes = [
    [peso, preco_por_tonelada, cliente, desconto * 100, valor_final]
]

# Cabeçalho
cabecalho = ["Peso (t)", "Preço ($/t)", "Cliente", "Desconto (%)", "Valor Final ($)"]

# Saída formatada
print("\n>>> RESUMO DA EXPORTAÇÃO\n")
print(tabulate(exportacoes, headers=cabecalho, tablefmt="grid", floatfmt=".2f"))
