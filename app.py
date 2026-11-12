import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# 1. Configuração da Página
st.set_page_config(page_title="AgriPredict - Recomendação de Safra", layout="centered")
st.title("🌱 AgriPredict: Recomendação Inteligente de Culturas")
st.markdown("Insira as condições do solo e clima para descobrir a cultura mais adequada.")

# 2. Carregar os dados e treinar o modelo em cache para não travar a tela
@st.cache_resource
def train_model():
    df = pd.read_csv('Crop_recommendation.csv')
    X = df.drop('label', axis=1)
    y = df['label']
    
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y_encoded)
    
    return model, encoder, X.columns

model, encoder, feature_names = train_model()

# 3. Criar os controles deslizantes para o usuário (Sidebar ou Colunas)
st.sidebar.header("Parâmetros do Solo e Clima")

N = st.sidebar.slider("Nitrogênio (N)", 0, 140, 50)
P = st.sidebar.slider("Fósforo (P)", 5, 145, 50)
K = st.sidebar.slider("Potássio (K)", 5, 205, 50)
temp = st.sidebar.slider("Temperatura (°C)", 8.0, 45.0, 25.0)
hum = st.sidebar.slider("Umidade (%)", 14.0, 100.0, 70.0)
ph = st.sidebar.slider("pH do Solo", 3.5, 9.9, 6.5)
rain = st.sidebar.slider("Chuva (mm)", 20.0, 300.0, 100.0)

# 4. Botão de Previsão
if st.button("Recomendar Cultura"):
    # Organizar o input do usuário no mesmo formato do dataset
    user_data = pd.DataFrame([[N, P, K, temp, hum, ph, rain]], columns=feature_names)
    
    # Fazer a previsão
    prediction_encoded = model.predict(user_data)
    prediction_label = encoder.inverse_transform(prediction_encoded)[0]
    
    st.success(f"🌾 A cultura mais recomendada para essas condições é: **{prediction_label.upper()}**")
