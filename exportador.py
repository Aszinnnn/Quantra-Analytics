import pandas as pd
import os

def exportar_empresas(df):
    os.makedirs("outputs/detalhes", exist_ok=True)
    
    cols = [
        "id", "nome_fantasia", "razao_social", "cnpj", 
        "telefone", "email", "endereco", "cidade", 
        "estado", "faturamento_anual", "funcionarios", "site"
    ]
    
    df[cols].to_csv(
        "outputs/detalhes/empresas_detalhadas.csv", 
        index=False,
        encoding='utf-8-sig'
    )