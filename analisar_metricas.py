import pandas as pd

# Lê o arquivo mesclado
df = pd.read_csv('metricas_finais.csv')

# Remove colunas inúteis se tiver
colunas_validas = ['repo', 'stars', 'releases', 'idade', 'loc', 'comentarios', 'cbo', 'dit', 'lcom']
df = df[[col for col in colunas_validas if col in df.columns]]

# Renomeia colunas se necessário
df = df.rename(columns={
    'stars': 'popularidade',
    'releases': 'atividade',
    'idade': 'maturidade',
    'loc': 'tamanho'
})

# Exibe resumo estatístico geral
estatisticas_gerais = df.describe().transpose()[['mean', '50%', 'std']]
estatisticas_gerais.columns = ['Média', 'Mediana', 'Desvio Padrão']
print("\nResumo Estatístico Geral (Todas as métricas):\n")
print(estatisticas_gerais)

# Exibe por métrica de qualidade individualmente
metricas_qualidade = ['cbo', 'dit', 'lcom']
for metrica in metricas_qualidade:
    if metrica in df.columns:
        print(f"\nResumo da métrica: {metrica.upper()}")
        resumo = df[metrica].describe()[['mean', '50%', 'std']]
        print(resumo)

# Exporta resultados se quiser salvar no disco
estatisticas_gerais.to_csv('resumo_estatistico_geral.csv')


