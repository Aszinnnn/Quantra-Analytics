import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visualizations(data):
    os.makedirs("outputs/plots", exist_ok=True)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data['empresas'], x='ramo', y='faturamento_anual')
    plt.savefig("outputs/plots/faturamento_por_ramo.png")
    plt.close()