#atividade 1

import nltk
from nltk.tokenize import word_tokenize

# Na primeira vez que rodar, você precisará baixar o recurso 'punkt'
# Ele contém os modelos matemáticos necessários para identificar os limites das palavras
nltk.download('punkt')

# Exemplo de mensagem recebida pela empresa
mensagem_cliente = "Olá! Gostaria de saber o status do meu pedido #1234. Aguardo retorno, obrigado."

# Aplicando a tokenização por palavras
palavras_tokenizadas = word_tokenize(mensagem_cliente, language='portuguese')

# Exibindo o resultado
print("Texto Original:")
print(mensagem_cliente)
print("\nPalavras Individualizadas:")
print(palavras_tokenizadas)

#atividade 2

import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Garanta que o recurso 'punkt' esteja baixado
nltk.download('punkt')

# Exemplo de avaliações de clientes acumuladas pelo sistema
avaliacoes = """
O produto é excelente, entrega muito rápida e o produto veio bem embalado. 
Muito satisfeito com a compra, excelente custo benefício. Recomendo o produto!
"""

# 1. Tokenização: Separando o texto em palavras (colocando tudo em minúsculo)
# Deixar em minúsculo (lower) evita que 'Produto' e 'produto' sejam contados como coisas diferentes
palavras = word_tokenize(avaliacoes.lower(), language='portuguese')

# 2. Contagem de Frequência
distribuicao_frequencia = FreqDist(palavras)

# 3. Exibindo os resultados
print("Frequência total de algumas palavras chave:")
print(f"A palavra 'produto' apareceu: {distribuicao_frequencia['produto']} vezes")
print(f"A palavra 'excelente' apareceu: {distribuicao_frequencia['excelente']} vezes")

print("\n--- As 5 palavras/pontuações mais comuns no texto ---")
# O método most_common() traz as palavras mais frequentes em ordem decrescente
for palavra, frequencia in distribuicao_frequencia.most_common(5):
    print(f"'{palavra}': {frequencia} vezes")

#atividade 3
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer

# Download dos recursos necessários do NLTK
nltk.download('punkt')
nltk.download('rslp') # Stemmer específico para o idioma português

def verificar_prioridade(mensagem):
    # 1. Inicializa o stemmer para o português
    stemmer = RSLPStemmer()
    
    # 2. Define a lista de palavras que disparam o alerta
    # Colocamos também os radicais para pegar variações (ex: "erros", "péssima")
    palavras_alerta = ["ruim", "péssimo", "pessimo", "erro", "errado", "defeito", "problema", "falha"]
    # Geramos os radicais das palavras de alerta para a comparação ideal
    radicais_alerta = [stemmer.stem(palavra.lower()) for item in palavras_alerta]
    
    # 3. Tokeniza a mensagem do cliente e passa para minúsculo
    palavras_cliente = word_tokenize(mensagem.lower(), language='portuguese')
    
    # 4. Verifica se algum radical da mensagem bate com os nossos alertas
    for palavra in palavras_cliente:
        radical_palavra = stemmer.stem(palavra)
        if radical_palavra in radicais_alerta:
            return True # Mensagem negativa detectada!
            
    return False # Nenhuma palavra de alerta encontrada

# --- Testando o Sistema ---

mensagens_teste = [
    "Olá, meu aplicativo está dando um erro na hora de fazer o login.",
    "A entrega foi super rápida, obrigado pelo atendimento!",
    "O serviço prestado foi péssimo, estou muito insatisfeito.",
    "Gostaria de saber se vocês abrem aos sábados."
]

print("--- Triagem de Mensagens de Atendimento ---\n")
for msg in mensagens_teste:
    prioridade_alta = verificar_prioridade(msg)
    status = "🚨 PRIORIDADE ALTA (Palavra negativa detectada)" if prioridade_alta else "✅ Fluxo Normal"
    print(f"Mensagem: \"{msg}\"")
    print(f"Status: {status}\n")



#atividade 4
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download dos recursos necessários (apenas na primeira execução)
nltk.download('punkt')
nltk.download('stopwords')

# 1. Definindo o texto de exemplo
texto_cliente = "O produto chegou antes do prazo, mas a embalagem veio com um rasgo para o lado de fora."

# 2. Carregando as stopwords em português
stopwords_portugues = set(stopwords.words('portuguese'))

# 3. Tokenizando o texto e convertendo para minúsculo
palavras = word_tokenize(texto_cliente.lower(), language='portuguese')

# 4. Filtrando as palavras (Removendo stopwords e pontuações simples)
palavras_filtradas = [
    palavra for palavra in palavras 
    if palavra not in stopwords_portugues and palavra.isalnum()
]

# --- Resultados ---
print("Texto Original:")
print(texto_cliente)

print("\nStopwords que foram detectadas e removidas:")
stopwords_encontradas = [p for p in palavras if p in stopwords_portugues]
print(set(stopwords_encontradas))

print("\nTexto Filtrado (Apenas palavras com significado real):")
print(palavras_filtradas)

#ATIVIDADE 5
import nltk
from nltk.tokenize import word_tokenize

# Garanta o recurso de tokenização instalado
nltk.download('punkt')

def analisar_sentimento(comentario):
    # 1. Nossos dicionários de palavras-chave
    palavras_positivas = {"ótimo", "otimo", "bom", "excelente", "maravilhoso", "perfeito", "amei", "recomendo", "rápido", "rapido"}
    palavras_negativas = {"ruim", "péssimo", "pessimo", "horrível", "horrivel", "defeito", "atrasou", "lento", "odiei", "quebrado"}
    
    # 2. Tokenizar o texto e colocar em minúsculo
    palavras_comentario = word_tokenize(comentario.lower(), language='portuguese')
    
    # 3. Contagem dos pontos
    score_positivo = 0
    score_negativo = 0
    
    for palavra in palavras_comentario:
        if palavra in palavras_positivas:
            score_positivo += 1
        elif palavra in palavras_negativas:
            score_negativo += 1
            
    # 4. Regra condicional para classificar o sentimento
    if score_positivo > score_negativo:
        return "POSITIVO 🟢"
    elif score_negativo > score_positivo:
        return "NEGATIVO 🔴"
    else:
        return "NEUTRO 🟡"

# --- Testando com comentários de marketing ---

comentarios_teste = [
    "O produto é excelente e a entrega foi muito rápida! Recomendo.",
    "Achei o atendimento péssimo e o sistema é muito lento.",
    "O produto é bom, mas o prazo de entrega foi apenas ok.",
    "Gostaria de saber se o produto já está disponível no estoque."
]

print("--- Análise de Sentimento de Comentários ---\n")
for comentario in comentarios_teste:
    resultado = analisar_sentimento(comentario)
    print(f"Comentário: \"{comentario}\"")
    print(f"Sentimento: {resultado}\n")

#ATIVIDADE 6
import nltk
from nltk.tokenize import word_tokenize

# Garanta que o recurso de tokenização esteja baixado
nltk.download('punkt')

def direcionar_atendimento(mensagem_usuario):
    # 1. Tokeniza a frase e padroniza para letras minúsculas
    palavras = word_tokenize(mensagem_usuario.lower(), language='portuguese')
    
    # 2. Define os mapeamentos de palavras-chave para cada setor
    chaves_financeiro = {"pagamento", "boleto", "cartão", "cartao", "fatura", "cobrança", "cobrança"}
    chaves_cancelamento = {"cancelar", "cancelamento", "encerrar", "desistir"}
    chaves_suporte_tecnico = {"erro", "falha", "bug", "problema", "travou", "ajuda"}

    # 3. Lógica condicional de detecção e roteamento
    # Usamos a interseção de conjuntos para checar rapidamente se há palavras em comum
    set_palavras = set(palavras)
    
    if set_palavras.intersection(chaves_cancelamento):
        return "Setor de Retenção e Cancelamentos ❌"
    
    elif set_palavras.intersection(chaves_financeiro):
        return "Setor Financeiro e Faturamento 💳"
        
    elif set_palavras.intersection(chaves_suporte_tecnico):
        return "Suporte Técnico 🛠️"
        
    else:
        return "Atendimento Geral / Transbordo Humano 👤"

# --- Simulando Interações com o Chatbot ---

mensagens_clientes = [
    "Quero cancelar minha assinatura, por favor.",
    "O aplicativo está dando erro na tela de login.",
    "Não recebi o boleto para o pagamento deste mês.",
    "Gostaria de falar com um atendente para tirar uma dúvida rápida."
]

print("--- Roteamento Automático do Chatbot ---\n")
for msg in mensagens_clientes:
    setor_destino = direcionar_atendimento(msg)
    print(f"Cliente: \"{msg}\"")
    print(f"Direcionando para ➡️ {setor_destino}\n")


#ATIVIDADE 7
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# Downloads necessários do NLTK (apenas na primeira execução)
nltk.download('punkt')
nltk.download('stopwords')

# Exemplo de banco de reclamações acumuladas pelo analista
reclamacoes_clientes = """
O aplicativo está muito lento. O aplicativo trava toda vez que tento abrir a tela de pagamento. 
O suporte não responde e o serviço está horrível. Quero o estorno do pagamento porque o aplicativo não funciona.
Fiquei esperando o suporte por horas e nada de retorno. O aplicativo precisa melhorar urgente.
"""

def analisar_reclamacoes(texto):
    # 1. Tokenização e conversão para minúsculo
    todas_palavras = word_tokenize(texto.lower(), language='portuguese')
    
    # 2. Carrega as stopwords em português
    stopwords_pt = set(stopwords.words('portuguese'))
    
    # Adicionamos pontuações manuais para garantir uma limpeza perfeita
    pontuacoes = {'.', ',', '!', '?', ';', ':', '...'}
    
    # 3. Filtragem: Mantém apenas palavras com significado real
    palavras_limpas = [
        palavra for palavra in todas_palavras 
        if palavra not in stopwords_pt and palavra not in pontuacoes and palavra.isalnum()
    ]
    
    # 4. Cálculo da Distribuição de Frequência
    frequencia = FreqDist(palavras_limpas)
    
    return frequencia

# --- Executando a Análise ---

resultado_frequencia = analisar_reclamacoes(reclamacoes_clientes)

print("--- TOP 5 PALAVRAS MAIS FREQUENTES NAS RECLAMAÇÕES ---")
print("(Use esses insights para priorizar as melhorias no produto)\n")

# Extrai as 5 palavras mais comuns
for palavra, contagem in resultado_frequencia.most_common(5):
    print(f"💥 Palavra: '{palavra}' -> Apareceu {contagem} vezes")

print("\n-----------------------------------------------------")
# Exemplo de busca específica para o analista testar hipóteses
print(f"Frequência específica de 'suporte': {resultado_frequencia['suporte']} vezes")
print(f"Frequência específica de 'lento': {resultado_frequencia['lento']} vezes")

#ATIVIDADE 8
import nltk
from nltk.tokenize import word_tokenize

# Garanta o recurso de tokenização instalado
nltk.download('punkt')

def classificar_mensagem(texto):
    # 1. Definindo os grupos de palavras-chave (Vocabulário)
    palavras_tecnico = {"erro", "falha", "bug", "travou", "sistema", "senha", "login", "aplicativo", "app", "site"}
    palavras_financeiro = {"boleto", "pagamento", "pago", "fatura", "cartão", "cartao", "cobrança", "reembolso", "estorno", "preço"}
    
    # 2. Tokenizar o texto e padronizar para letras minúsculas
    palavras_mensagem = word_tokenize(texto.lower(), language='portuguese')
    
    # 3. Contagem de pontos por categoria
    pontos_tecnico = 0
    pontos_financeiro = 0
    
    for palavra in palavras_mensagem:
        if palavra in palavras_tecnico:
            pontos_tecnico += 1
        elif palavra in palavras_financeiro:
            pontos_financeiro += 1
            
    # 4. Regras condicionais de classificação
    if pontos_tecnico > pontos_financeiro:
        return "Suporte Técnico 🛠️"
    elif pontos_financeiro > pontos_tecnico:
        return "Financeiro 💳"
    elif pontos_tecnico == 0 and pontos_financeiro == 0:
        return "Indefinido (Encaminhar para triagem geral) 👤"
    else:
        return "Duplo Canal (Contém termos de ambas as áreas) 🔄"

# --- Testando a Classificação Automática ---

caixa_de_entrada = [
    "Não estou conseguindo fazer o login no app, a tela fica branca.",
    "O boleto da minha mensalidade veio com o valor errado, preciso de uma nova via.",
    "Meu aplicativo travou logo após eu confirmar o pagamento do plano.",
    "Gostaria de saber qual é o horário de atendimento de vocês."
]

print("--- Classificador Automático de Mensagens ---\n")
for msg in caixa_de_entrada:
    categoria = classificar_mensagem(msg)
    print(f"Mensagem: \"{msg}\"")
    print(f"Classificação: {categoria}\n")


#ATIVIDADE 9
