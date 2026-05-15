# # # import streamlit as st
# # # import pandas as pd
# # # import numpy as np
# # # from sklearn.linear_model import LinearRegression

# # # # -----------------------------------------------------------------------------
# # # # 1. CONFIGURAÇÃO DA PÁGINA E CAMADA DE DADOS
# # # # -----------------------------------------------------------------------------
# # # st.set_page_config(page_title="Preditor de Cansaço Gamer", layout="centered")

# # # @st.cache_data
# # # def carregar_dados() -> pd.DataFrame:
# # #     """
# # #     Retorna o DataFrame inicial com o histórico de horas jogadas e cansaço.
# # #     """
# # #     return pd.DataFrame({
# # #         'horas_jogo': [1, 2, 4, 6, 8, 10],
# # #         'cansaco': [1, 2, 3, 5, 8, 10]
# # #     })

# # # # -----------------------------------------------------------------------------
# # # # 2. CAMADA DE MODELAGEM E INFERÊNCIA
# # # # -----------------------------------------------------------------------------
# # # def treinar_modelo(df: pd.DataFrame) -> LinearRegression:
# # #     """
# # #     Treina um modelo de Regressão Linear Simples.
# # #     """
# # #     X = df[['horas_jogo']].values
# # #     y = df['cansaco'].values
    
# # #     modelo = LinearRegression()
# # #     modelo.fit(X, y)
# # #     return modelo

# # # def realizar_inferencia(modelo: LinearRegression, horas: float) -> float:
# # #     """
# # #     Executa a predição e garante que o valor de cansaço permaneça no escopo lógico.
# # #     """
# # #     X_novo = np.array([[horas]])
# # #     predicao = modelo.predict(X_novo)[0]
# # #     # Restringe o resultado ao intervalo lógico de 0 a 10
# # #     return float(np.clip(predicao, 0, 10))

# # # # -----------------------------------------------------------------------------
# # # # 3. INTERFACE DO USUÁRIO (STREAMLIT)
# # # # -----------------------------------------------------------------------------
# # # def main():
# # #     st.title("🔬 Preditor de Nível de Cansaço Gamer")
# # #     st.markdown(
# # #         """
# # #         Este laboratório demonstra a aplicação de um modelo de **Regressão Linear** 
# # #         para correlacionar a carga horária de jogos eletrônicos com o nível de fadiga autodeclarado.
# # #         """
# # #     )
    
# # #     # Inicialização dos dados e modelo
# # #     df_gamer = carregar_dados()
# # #     modelo = treinar_modelo(df_gamer)
    
# # #     # Seção lateral: Visualização dos dados de treino
# # #     st.sidebar.header("Dados de Treinamento")
# # #     st.sidebar.dataframe(df_gamer, use_container_width=True)
    
# # #     st.header("Simulação de Inferência")
    
# # #     # Input do usuário
# # #     horas_usuario = st.slider(
# # #         label="Selecione a quantidade de horas jogadas continuamente:",
# # #         min_value=0.0,
# # #         max_value=12.0,
# # #         value=5.0,
# # #         step=0.5
# # #     )
    
# # #     # Processamento e Saída
# # #     if st.button("Calcular Fadiga Prevista", type="primary"):
# # #         cansaco_previsto = realizar_inferencia(modelo, horas_usuario)
        
# # #         # Exibição dos resultados com formatação métrica
# # #         st.subheader("Resultado da Predição")
        
# # #         col1, col2 = st.columns(2)
# # #         with col1:
# # #             st.metric(label="Horas Inseridas", value=f"{horas_usuario} h")
# # #         with col2:
# # #             st.metric(label="Nível de Cansaço Estimado", value=f"{cansaco_previsto:.2f} / 10")
            
# # #         # Feedback visual baseado no limiar de cansaço
# # #         if cansaco_previsto >= 7.0:
# # #             st.warning("⚠️ Alerta: Nível de fadiga elevado. Recomenda-se pausa para descanso.")
# # #         elif cansaco_previsto >= 4.0:
# # #             st.info("💡 Nota: Fadiga moderada detectada.")
# # #         else:
# # #             st.success("✅ Nível de energia estável para a jornada informada.")

# # # if __name__ == "__main__":
# # #     main()


# # # #-----------------------------------------------------------------------------------------------






# # #atividade 3

# # import streamlit as st
# # import pandas as pd
# # import numpy as np
# # from sklearn.linear_model import LinearRegression

# # # -----------------------------------------------------------------------------
# # # 1. CONFIGURAÇÃO DA PÁGINA E CAMADA DE DADOS
# # # -----------------------------------------------------------------------------
# # st.set_page_config(page_title="Predição de Vendas de Sorvete", layout="centered")

# # st.title("🍦 Predição de Vendas de Sorvete via Regressão Linear")
# # st.write(
# #     "Este sistema utiliza um modelo de Regressão Linear Simples para estimar "
# #     "a quantidade de sorvetes vendidos com base na temperatura ambiente."
# # )

# # # Dataset fornecido
# # dados_sorvete = pd.DataFrame({
# #     'temperatura': [18, 20, 24, 27, 30, 35],
# #     'vendas': [20, 25, 40, 55, 70, 100]
# # })

# # # -----------------------------------------------------------------------------
# # # 2. TREINAMENTO DO MODELO (BACKEND)
# # # -----------------------------------------------------------------------------
# # # Separação das variáveis: X (independente/preditora) e y (dependente/alvo)
# # # O Scikit-Learn espera que X seja uma matriz bidimensional (Dataframe ou 2D Array)
# # X = dados_sorvete[['temperatura']]
# # y = dados_sorvete['vendas']

# # # Instanciação e ajuste do modelo de Regressão Linear
# # modelo = LinearRegression()
# # modelo.fit(X, y)

# # # -----------------------------------------------------------------------------
# # # 3. INTERFACE DE USUÁRIO (FRONTEND) E PREDIÇÃO
# # # -----------------------------------------------------------------------------
# # st.header("1. Simulação de Predição")

# # # Define os limites do slider com base nos dados históricos
# # temp_min = int(dados_sorvete['temperatura'].min()) - 5
# # temp_max = int(dados_sorvete['temperatura'].max()) + 5

# # # Input do usuário via Slider
# # temperatura_usuario = st.slider(
# #     "Selecione a temperatura ambiente (°C):",
# #     min_value=temp_min,
# #     max_value=temp_max,
# #     value=25
# # )

# # # Realizando a predição para o valor selecionado
# # # É necessário passar o input no mesmo formato bidimensional usado no treino
# # input_modelo = np.array([[temperatura_usuario]])
# # vendas_preditas = modelo.predict(input_modelo)[0]

# # # Exibição do resultado formatado
# # st.metric(
# #     label="Quantidade Estimada de Vendas", 
# #     value=f"{int(round(vendas_preditas))} sorvetes"
# # )

# # # -----------------------------------------------------------------------------
# # # 4. VISUALIZAÇÃO DOS DADOS E DA LINHA DE TENDÊNCIA
# # # -----------------------------------------------------------------------------
# # st.header("2. Análise Gráfica e Dados Históricos")

# # tab1, tab2 = st.tabs(["Gráfico de Tendência", "Dados Brutos"])

# # with tab1:
# #     st.subheader("Dispersão dos Dados")
# #     # Gerando os pontos da linha de regressão para plotagem gráfica
# #     X_linha = pd.DataFrame({'temperatura': range(temp_min, temp_max + 1)})
# #     X_linha['vendas_estimadas'] = modelo.predict(X_linha)
    
# #     # Unificando os dados reais e a linha de predição para o gráfico do Streamlit
# #     grafico_df = pd.merge(X_linha, dados_sorvete, on='temperatura', how='left')
    
# #     # Exibição do gráfico utilizando a biblioteca nativa do Streamlit (alternativa ao Matplotlib)
# #     st.scatter_chart(
# #         data=grafico_df,
# #         x='temperatura',
# #         y=['vendas', 'vendas_estimadas'],
# #         color=["#FF4B4B", "#0068C9"]
# #     )
# #     st.caption("Legenda: Pontos isolados representam os dados reais. A linha contínua representa a tendência linear.")

# # with tab2:
# #     st.subheader("Dataset de Treino")
# #     st.dataframe(dados_sorvete, use_container_width=True)

# # # -----------------------------------------------------------------------------
# # # 5. MÉTRICAS DO MODELO (INFORMAÇÃO ACADÊMICA)
# # # -----------------------------------------------------------------------------
# # st.header("3. Parâmetros Estatísticos do Modelo")
# # r2_score = modelo.score(X, y)

# # col1, col2 = st.columns(2)
# # col1.metric(label="Coeficiente de Determinação ($R^2$)", value=f"{r2_score:.4f}")
# # col2.metric(label="Coeficiente Angular (Slope)", value=f"{modelo.coef_[0]:.2f}")

# # st.latex(f"f(x) = {modelo.coef_[0]:.2f} \cdot x + ({modelo.intercept_:.2f})")





# #atividade 4


# import streamlit as st
# import pandas as pd
# import numpy as np
# from sklearn.linear_model import LogisticRegression, LinearRegression

# # -----------------------------------------------------------------------------
# # CONFIGURAÇÃO DA PÁGINA E ESTILIZAÇÃO
# # -----------------------------------------------------------------------------
# st.set_page_config(
#     page_title="Detector de Aprovação Ninja",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # -----------------------------------------------------------------------------
# # CONTEXTO E DADOS DE TREINAMENTO
# # -----------------------------------------------------------------------------
# st.title("🥷 Detector de Aprovação Ninja")
# st.markdown("""
# Esta aplicação demonstra a aplicação de modelos de Machine Learning (**Regressão Logística** e **Regressão Linear**) 
# para resolver um problema de classificação binária: prever se um aluno será **Aprovado (1)** ou **Reprovado (0)** 
# com base no seu número de faltas.
# """)

# # Base de dados original
# df_alunos = pd.DataFrame({
#     'faltas': [0, 1, 2, 5, 7, 10],
#     'resultado': [1, 1, 1, 0, 0, 0]
# })

# # Preparação dos dados para o Scikit-Learn
# X = df_alunos[['faltas']]
# y = df_alunos['resultado']

# # -----------------------------------------------------------------------------
# # TREINAMENTO DOS MODELOS
# # -----------------------------------------------------------------------------
# # 1. Regressão Logística
# modelo_logístico = LogisticRegression()
# modelo_logístico.fit(X, y)

# # 2. Regressão Linear
# modelo_linear = LinearRegression()
# modelo_linear.fit(X, y)

# # -----------------------------------------------------------------------------
# # INTERFACE DE USUÁRIO (SIDEBAR & PREDIÇÃO)
# # -----------------------------------------------------------------------------
# st.sidebar.header("Parâmetros de Entrada")
# input_faltas = st.sidebar.slider(
#     "Número de Faltas do Aluno:", 
#     min_value=0, 
#     max_value=15, 
#     value=3, 
#     step=1
# )

# st.sidebar.markdown("---")
# st.sidebar.markdown("**Legenda do Resultado:**")
# st.sidebar.markdown("- `1` = Aprovado")
# st.sidebar.markdown("- `0` = Reprovado")

# # Predições com base no input do usuário
# X_input = np.array([[input_faltas]])

# # Predição Logística
# pred_logistica = modelo_logístico.predict(X_input)[0]
# prob_logistica = modelo_logístico.predict_proba(X_input)[0][1]

# # Predição Linear (Aplicando limiar de decisão corte de 0.5)
# pred_linear_continua = modelo_linear.predict(X_input)[0]
# pred_linear_classificada = 1 if pred_linear_continua >= 0.5 else 0

# # -----------------------------------------------------------------------------
# # EXIBIÇÃO DOS RESULTADOS
# # -----------------------------------------------------------------------------
# col1, col2 = st.columns(2)

# with col1:
#     st.subheader("Análise via Regressão Logística")
#     st.metric(
#         label="Classificação Final", 
#         value="APROVADO" if pred_logistica == 1 else "REPROVADO"
#     )
#     st.write(f"**Probabilidade calculada de aprovação:** {prob_logistica:.2%}")
#     st.progress(float(prob_logistica))

# with col2:
#     st.subheader("Análise via Regressão Linear")
#     st.metric(
#         label="Classificação Final (Limiar 0.5)", 
#         value="APROVADO" if pred_linear_classificada == 1 else "REPROVADO"
#     )
#     st.write(f"**Valor contínuo predito pelo modelo:** {pred_linear_continua:.4f}")
#     st.caption("Nota: Valores >= 0.5 são classificados como Aprovado (1).")

# st.markdown("---")

# # -----------------------------------------------------------------------------
# # VISUALIZAÇÃO DIDÁTICA DOS DADOS E COMPORTAMENTO DOS MODELOS
# # -----------------------------------------------------------------------------
# st.subheader("Visualização dos Modelos e Dados de Treino")

# # Criação de um espaço amostral contínuo para plotar as linhas dos modelos
# faltas_espaco = np.linspace(0, 15, 100).reshape(-1, 1)
# linha_logistica = modelo_logístico.predict_proba(faltas_espaco)[:, 1]
# linha_linear = modelo_linear.predict(faltas_espaco)

# # DataFrame auxiliar para renderização dos gráficos no Streamlit
# df_visualizacao = pd.DataFrame({
#     'Faltas': faltas_espaco.flatten(),
#     'Regressão Logística (Probabilidade)': linha_logistica,
#     'Regressão Linear (Valor Contínuo)': linha_linear,
#     'Limiar de Decisão (0.5)': 0.5
# }).set_index('Faltas')

# # Exibição dos gráficos nativos do Streamlit
# tab1, tab2, tab3 = st.tabs(["Dados Históricos", "Curva Logística", "Reta Linear"])

# with tab1:
#     st.markdown("**Dispersão dos dados originais de treinamento:**")
#     st.scatter_chart(df_alunos, x='faltas', y='resultado', color="#FF4B4B")

# with tab2:
#     st.markdown("**Comportamento da Regressão Logística (Sigmoide):**")
#     st.line_chart(df_visualizacao[['Regressão Logística (Probabilidade)', 'Limiar de Decisão (0.5)']])

# with tab3:
#     st.markdown("**Comportamento da Regressão Linear:**")
#     st.line_chart(df_visualizacao[['Regressão Linear (Valor Contínuo)', 'Limiar de Decisão (0.5)']])

# # Rodapé com os dados brutos para transparência acadêmica
# with st.expander("Visualizar Dados de Treinamento Brutos"):
#     st.dataframe(df_alunos)



#atividade 5

