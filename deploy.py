import streamlit as st
import joblib
import pandas as pd

features_numericas = {'Time': 0, 'V1': 0, 'V2': 0, 'V3': 0, 'V4': 0, 'V5': 0, 'V6': 0, 'V7': 0, 'V8': 0, 'V9': 0, 'V10': 0,
                      'V11': 0, 'V12': 0, 'V13': 0, 'V14': 0, 'V15': 0, 'V16': 0, 'V17': 0, 'V18': 0, 'V19': 0, 'V20': 0,
                      'V21': 0, 'V22': 0, 'V23': 0, 'V24': 0, 'V25': 0, 'V26': 0, 'V27': 0, 'V28': 0, 'Amount': 0}


st.title('Detecção de Fraude em cartões de crédito')

# iterando sobre as features para criar caixa de input para cada
for feature in features_numericas:
    # diferenciando para mudar a formatação para cada feature
    if feature == 'Time':
        resposta = st.number_input(f'{feature}', step=1)

    elif feature == 'Amount':
        resposta = st.number_input(
            f'{feature}', step=0.01, value=0.0, format="%.2f")

    else:
        resposta = st.number_input(
            f'{feature}', step=0.000000000000000001, value=0.0, format="%.18f")

    features_numericas[feature] = resposta

# criando um botão para o processo
botao = st.button('Fazer previsão de Fraudes')

# como só tem um tipo de feature não é necessário um dicionário geral junto por um dicionario.update(feature_categoricas)
if botao:

    X = pd.DataFrame(features_numericas, index=[0])
    modelo = joblib.load('modelo.joblib')
    resposta_fraude = modelo.predict(X)
    if resposta_fraude == 0:
        resposta_fraude = 'Fraude não detectada'
    elif resposta_fraude == 1:
        resposta_fraude = 'Fraude detectada'
    st.write(resposta_fraude)
