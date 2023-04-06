
faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

#  Faturamento total mensal da distribuidora
faturamento_total = sum(faturamento_estado.values())

# Percentual de representação de cada estado no faturamento total
representacao_por_estado = {}
for estado, faturamento in faturamento_estado.items():
    representacao_por_estado[estado] = (faturamento / faturamento_total) * 100

# Impressão dos resultados
for estado, representacao in representacao_por_estado.items():
    print(f"{estado}: {representacao:.2f}%")