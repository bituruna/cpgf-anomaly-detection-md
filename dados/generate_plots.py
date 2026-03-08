import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import hdbscan

# Configurando o estilo visual das plotagens
sns.set_theme(style="whitegrid", palette="muted")

data_path = 'cpgf_normalizado.csv'
df = pd.read_csv(data_path, sep=';', index_col=0)

kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
df['Cluster_KMeans'] = kmeans.fit_predict(df)
distancias = kmeans.transform(df)
df['Distancia_Centroide_KMeans'] = distancias.min(axis=1)

clusterer = hdbscan.HDBSCAN(min_cluster_size=5, min_samples=3, gen_min_span_tree=True)
df['Cluster_HDBSCAN'] = clusterer.fit_predict(df)
df['HDBSCAN_Outlier_Score'] = clusterer.outlier_scores_

# Carregar a base de dados limpa (que contém a informação do órgão)
df_limpo_aux = pd.read_csv('cpgf_limpo.csv', sep=';', encoding='utf-8')

# Mapear o órgão mais frequente / primário de cada CPF para o nosso dataframe principal da mineração
cpf_ug_map = df_limpo_aux.groupby('CPF PORTADOR')['NOME UNIDADE GESTORA'].first()
df['NOME UNIDADE GESTORA'] = df.index.map(cpf_ug_map)

ug1 = 'COORDENACAO GERAL DE ADMINISTRACAO CGAD/DLOG/'
ug2 = 'SECRETARIA DE ADMINISTRACAO/PR'

df_ug1 = df[df['NOME UNIDADE GESTORA'] == ug1]
df_ug2 = df[df['NOME UNIDADE GESTORA'] == ug2]

def plot_comparativo_ug(df_subset, nome_ug, filename):
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle(f'Análise Comparativa de Anomalias: {nome_ug}', fontsize=16, fontweight='bold', y=1.05)
    
    # --- Gráfico 1: K-MEANS ---
    sns.scatterplot(
        ax=axes[0],
        data=df_subset, 
        x='qtd_transacoes', 
        y='total_gasto',
        hue='Cluster_KMeans', 
        palette='tab10', 
        s=50, 
        alpha=0.6
    )
    
    # Top 10 anomalias do K-Means neste órgão
    top_anomalias_kmeans = df_subset.nlargest(10, 'Distancia_Centroide_KMeans')
    axes[0].scatter(
        top_anomalias_kmeans['qtd_transacoes'], 
        top_anomalias_kmeans['total_gasto'],
        color='red', 
        marker='x', 
        s=150, 
        linewidths=2,
        label='Top 10 Anomalias'
    )
    axes[0].set_title('K-Means: Distância ao Centróide', fontsize=14, pad=10)
    axes[0].set_xlabel('Quantidade de Transações (Normalizada)', fontsize=12)
    axes[0].set_ylabel('Total Gasto (Normalizado)', fontsize=12)
    axes[0].legend()

    # --- Gráfico 2: HDBSCAN ---
    sns.scatterplot(
        ax=axes[1],
        data=df_subset, 
        x='qtd_transacoes', 
        y='total_gasto',
        hue='Cluster_HDBSCAN', 
        palette='Set2', 
        s=50, 
        alpha=0.6
    )
    
    # Score de anomalia ≥ 0.8 neste órgão
    anomalias_hdbscan = df_subset[df_subset['HDBSCAN_Outlier_Score'] >= 0.8]
    axes[1].scatter(
        anomalias_hdbscan['qtd_transacoes'], 
        anomalias_hdbscan['total_gasto'],
        color='red', 
        marker='x', 
        s=150, 
        linewidths=2,
        label='Score ≥ 0.8'
    )
    axes[1].set_title('HDBSCAN: Score de Detecção de Outliers', fontsize=14, pad=10)
    axes[1].set_xlabel('Quantidade de Transações (Normalizada)', fontsize=12)
    axes[1].set_ylabel('Total Gasto (Normalizado)', fontsize=12)
    axes[1].legend()
    
    plt.tight_layout()
    plt.savefig(filename)

plot_comparativo_ug(df_ug1, ug1, 'out_ug1.png')
plot_comparativo_ug(df_ug2, ug2, 'out_ug2.png')
