import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Configuração inicial da página Streamlit
st.set_page_config(page_title="Preditor de Notas", layout="centered")

st.title("📊 Preditor de Notas com Regressão Linear")
st.markdown("""
Esta aplicação utiliza a biblioteca **scikit-learn** para treinar um modelo de Regressão Linear Simples.
O objetivo é prever a nota de um aluno com base nas horas dedicadas ao estudo.
""")

# 1. Carga e Estruturação dos Dados (Encapsulada em cache para performance)
@st.cache_data
def carregar_dados():
    return pd.DataFrame({
        'notas': [1, 2, 4, 6, 8, 10],
        'horas': [2, 4, 5, 7, 9, 10]
    })

df_estudos = carregar_dados()

# Exibição dos dados históricos na barra lateral (Sidebar)
st.sidebar.header("Dados Históricos de Treinamento")
st.sidebar.dataframe(df_estudos)

# 2. Treinamento do Modelo (Executado nos bastidores)
X = df_estudos['horas'].to_frame()
y = df_estudos['notas']

modelo = LinearRegression()
modelo.fit(X, y)

# 3. Interface de Interação do Usuário
st.subheader("Simular Novo Cenário")
horas_inseridas = st.slider(
    "Selecione a quantidade de horas de estudo:",
    min_value=0.0,
    max_value=12.0,
    value=6.0,
    step=0.5
)

# 4. Predição em Tempo Real
# O Streamlit reexecuta o script sempre que o estado do slider muda
novo_dado = pd.DataFrame({'horas': [horas_inseridas]})
nota_prevista = modelo.predict(novo_dado)[0]

# Tratamento para evitar notas maiores que 10 ou menores que 0 (Regra de Negócio)
nota_final = max(0.0, min(10.0, nota_prevista))

# 5. Apresentação dos Resultados
st.metric(
    label="Nota Prevista", 
    value=f"{nota_final:.2f} / 10.00",
    delta=f"{nota_final - df_estudos['notas'].mean():.2f} em relação à média"
)

# Visualização gráfica dos dados e da predição atual
st.subheader("Gráfico de Dispersão e Correlação")
# Criando uma coluna de predição para plotar a linha de tendência
df_estudos['Previsão (Linha)'] = modelo.predict(X)

st.scatter_chart(data=df_estudos, x='horas', y='notas', color="#ff4b4b")
st.line_chart(data=df_estudos, x='horas', y='Previsão (Linha)')