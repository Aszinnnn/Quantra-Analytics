import pandas as pd

def process_data(df):
    df = df.dropna(subset=['cnpj', 'razao_social'])
    df['tamanho'] = pd.cut(df['funcionarios'],
                          bins=[0, 10, 50, 200, 500],
                          labels=['Micro', 'Pequena', 'Média', 'Grande'])
    return {
        'empresas': df,
        'metricas': df.groupby('ramo').agg({'faturamento_anual': 'mean'})
    }