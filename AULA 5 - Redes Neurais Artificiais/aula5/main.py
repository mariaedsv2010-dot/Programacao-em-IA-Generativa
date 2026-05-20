"""
💡 PREVISÃO DA CONTA DE LUZ - APP STREAMLIT COM SCIKIT-LEARN
=============================================================
Projeto didático para aprender:
  - Streamlit: criação de interfaces web com Python
  - scikit-learn MLPRegressor: rede neural leve para regressão
  - Visualização de dados: gráficos de linha interativos

POR QUE SCIKIT-LEARN EM VEZ DE TENSORFLOW?
  TensorFlow foi projetado para modelos gigantes em produção (GPT, visão computacional).
  Para um problema simples como este (1 entrada → 1 saída), ele é como usar
  um caminhão para entregar uma carta.

  scikit-learn é a escolha certa para:
    ✅ Modelos menores e mais simples
    ✅ Aprendizado de conceitos de ML
    ✅ Instalação rápida e leve
    ✅ API consistente e bem documentada
"""

# ─────────────────────────────────────────────
# 1. IMPORTAÇÕES
# ─────────────────────────────────────────────
import streamlit as st                              # Interface web interativa
import numpy as np                                  # Manipulação de arrays numéricos
import pandas as pd                                 # Estrutura de dados (para o gráfico)
from sklearn.neural_network import MLPRegressor     # ← Substituto leve do TensorFlow
from sklearn.preprocessing import MinMaxScaler      # Normalização dos dados (igual ao que fazíamos manualmente)


# ─────────────────────────────────────────────
# 2. CONFIGURAÇÃO DA PÁGINA
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Previsão Conta de Luz ⚡",
    page_icon="⚡",
    layout="centered"
)


# ─────────────────────────────────────────────
# 3. TREINAMENTO DO MODELO
#
# @st.cache_resource: garante que o modelo seja treinado
# apenas UMA VEZ, mesmo quando o usuário move o slider.
# Sem isso, re-treinaria a cada interação — lento e desnecessário.
# ─────────────────────────────────────────────
@st.cache_resource
def treinar_modelo():
    """
    Gera dados simulados e treina uma rede neural leve com scikit-learn.

    DIFERENÇA CHAVE vs. TensorFlow:
      - TF: você define camadas manualmente com keras.Sequential
      - scikit-learn: você passa hidden_layer_sizes=(16, 8) e ele monta a rede

    Ambos resultam na mesma arquitetura:
      Entrada(1) → Camada(16 neurônios) → Camada(8 neurônios) → Saída(1)
    """

    # --- Dados de treinamento simulados ---
    np.random.seed(42)
    horas = np.linspace(0, 12, 200).reshape(-1, 1)  # reshape(-1,1): transforma lista em coluna

    potencia_kw = 1.5
    tarifa      = 0.75
    dias_mes    = 30
    ruido       = np.random.normal(0, 15, size=horas.shape)

    custo = (horas * potencia_kw * tarifa * dias_mes) + ruido

    # --- Normalização com MinMaxScaler ---
    # Antes fazíamos manualmente: X = horas / horas_max
    # MinMaxScaler faz isso automaticamente para qualquer faixa de dados
    scaler_X = MinMaxScaler()
    scaler_y = MinMaxScaler()

    X_norm = scaler_X.fit_transform(horas)           # fit_transform: aprende o máx/mín E transforma
    y_norm = scaler_y.fit_transform(custo).ravel()   # .ravel(): transforma coluna em vetor 1D

    # --- Criação e treinamento da rede neural ---
    # hidden_layer_sizes=(16, 8): duas camadas ocultas com 16 e 8 neurônios
    # activation='relu': mesma função de ativação que usávamos no TF
    # max_iter=500: equivalente a epochs=500 no TF
    # random_state=42: reprodutibilidade
    modelo = MLPRegressor(
        hidden_layer_sizes=(16, 8),
        activation='relu',
        max_iter=500,
        random_state=42
    )
    modelo.fit(X_norm, y_norm)

    # Retornamos o modelo E os scalers (precisamos deles para prever depois)
    return modelo, scaler_X, scaler_y


# ─────────────────────────────────────────────
# 4. FUNÇÃO DE PREVISÃO
# ─────────────────────────────────────────────
def prever_custo(modelo, scaler_X, scaler_y, horas_dia):
    """
    Normaliza a entrada → prevê → desnormaliza a saída.
    O scaler cuida de tudo automaticamente — mais seguro que fazer na mão.
    """
    entrada = np.array([[horas_dia]])
    entrada_norm = scaler_X.transform(entrada)                    # Normaliza com o mesmo scaler do treino
    saida_norm = modelo.predict(entrada_norm).reshape(-1, 1)      # Previsão (ainda normalizada)
    custo = scaler_y.inverse_transform(saida_norm)[0][0]          # Desnormaliza → valor em R$
    return max(0.0, custo)


# ─────────────────────────────────────────────
# 5. INTERFACE DO USUÁRIO
# ─────────────────────────────────────────────
st.title("⚡ Previsão da Conta de Luz")
st.markdown("##### Descubra quanto seu ar-condicionado vai custar no verão 🌡️")
st.divider()

with st.spinner("🧠 Treinando modelo de IA... (apenas uma vez)"):
    modelo, scaler_X, scaler_y = treinar_modelo()

st.success("✅ Modelo pronto!")
st.divider()

# --- Slider de entrada ---
st.subheader("📥 Informe seu uso diário")
horas_uso = st.slider(
    label="⏱️ Horas de uso do ar-condicionado por dia:",
    min_value=0.0,
    max_value=12.0,
    value=6.0,
    step=0.5,
    help="Considere a média diária de uso ao longo do mês"
)

# ─────────────────────────────────────────────
# 6. RESULTADO E GRÁFICO
# ─────────────────────────────────────────────
st.divider()
st.subheader("📊 Resultado da Previsão")

custo_previsto = prever_custo(modelo, scaler_X, scaler_y, horas_uso)

st.metric(
    label=f"💰 Custo estimado para {horas_uso:.1f}h/dia",
    value=f"R$ {custo_previsto:.2f}",
    delta=f"Fórmula direta: R$ {horas_uso * 1.5 * 0.75 * 30:.2f}",
    delta_color="off"
)

st.divider()
st.subheader("📈 Curva de Gasto por Horas de Uso")

faixa_horas  = np.arange(0, 12.5, 0.5)
custos_linha = [prever_custo(modelo, scaler_X, scaler_y, h) for h in faixa_horas]

df_grafico = pd.DataFrame(
    {"Custo Previsto (R$)": custos_linha},
    index=[f"{h:.1f}h" for h in faixa_horas]
)
st.line_chart(df_grafico, use_container_width=True)
st.caption(f"📍 Sua seleção: **{horas_uso:.1f}h/dia** → custo previsto de **R$ {custo_previsto:.2f}/mês**")

# ─────────────────────────────────────────────
# 7. SEÇÃO EDUCATIVA
# ─────────────────────────────────────────────
st.divider()
with st.expander("🔍 TensorFlow vs. scikit-learn — qual usar e quando?"):
    st.markdown("""
    | Critério | TensorFlow / Keras | scikit-learn |
    |---|---|---|
    | Instalação | Pesada (~500MB) | Leve (~30MB) |
    | Curva de aprendizado | Alta | Baixa |
    | Ideal para | Visão computacional, NLP, LLMs | Modelos clássicos de ML |
    | Redes neurais simples | Funciona, mas exagero | ✅ Ideal |
    | Suporte a GPU | ✅ Sim | ❌ Não |

    **Regra prática:**
    > Se seus dados cabem em uma planilha e o modelo tem menos de 5 camadas,
    > **scikit-learn** é a escolha mais inteligente.
    > Use TensorFlow quando precisar de poder de fogo real.
    """)

st.divider()
st.caption("⚠️ Valores estimados para fins educacionais.")