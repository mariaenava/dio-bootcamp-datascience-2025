'''
DESAFIO

Você foi contratado para desenvolver um sistema que determine a quantidade de paletes necessária para armazenar a produção diária de caixas. Cada palete possui uma capacidade fixa de caixas, e o objetivo é calcular o número total de paletes requeridos para acomodar toda a produção do dia.

ENTRADA
- O número total de caixas produzidas.
- A capacidade de caixas que um palete pode suportar.

SAÍDA
- Deverá retornar uma string que representa o número total de paletes necessários, sem espaços ou caracteres especiais.
'''

import math
from tabulate import tabulate

# Leitura do total de caixas
while True:
    try:
        total_caixas = int(input("Total de caixas (unid): "))
        break
    except ValueError:
        print("Quantidade inválida. Insira um número.\n")

# Leitura da capacidade de paletes
while True:
    try:
        capacidade_palete = int(input("Capacidade do palete (unid): "))
        break
    except ValueError:
        print("Capacidade inválida. Insira um número.\n")

# Calculo do número de paletes necessários (arredondando para cima)
paletes_necessarios = math.ceil(total_caixas/capacidade_palete)

# Dados para a tabela
armazenamento = [
    [total_caixas, capacidade_palete, paletes_necessarios]
]

# Cabeçalho
cabecalho = ["Total de Caixas (unid)", "Capacidade de Paletes (unid)", "Paletes Necessários (unid)"]

# Saída formatada
print("\n>>> RESUMO DO CÁLCULO DE ARMAZENAGEM\n")
print(tabulate(armazenamento, headers=cabecalho, tablefmt="grid", floatfmt=".2f"))
