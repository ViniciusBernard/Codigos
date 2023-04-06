
faturamento_diario = [2000, 1000, 1500, 3000, 2500, 1833, 1200, 2200, 1600, 1900, 2800, 2300, 2777, 4400, 2166, 3900, 1200, 1600, 2344, 1400, 1750, 2800, 1200, 1100, 2010, 2900, 2300, 2511, 3477, 2700, 3600]


menor_faturamento = min(faturamento_diario)


maior_faturamento = max(faturamento_diario)


media_mensal = sum(faturamento_diario) / len(faturamento_diario)


dias_acima_da_media = 0
for faturamento in faturamento_diario:
    if faturamento > media_mensal:
        dias_acima_da_media += 1


print(f"Menor valor de faturamento diário: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento diário: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento diário acima da média mensal: {dias_acima_da_media}")