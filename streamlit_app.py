import streamlit as st 
import requests
from requests.exceptions import ConnectionError

ip_api = "127.0.0.1"
port_api = "5000"

# Заголовок приложения
st.title("Оценка стоимости дома")

# Ввод данных
st.write("Введите данные для оценки")

# Выпадающее меню для выбора класса билета
bulding_type = st.selectbox("Тип строения", ["Кирпичный", "Монолитный", "Панельный"])

# Текстовое поле для ввода возраста с проверкой на число
age = st.text_input("Age", value=10)
if not age.isdigit():
    st.error("Please enter a valid number for Age.")

# Текстовое поле для ввода стоимости билета с проверкой на число
fare = st.text_input("Fare", value=100)
if not fare.isdigit():
    st.error("Please enter a valid number for Fare.")

# Кнопка для отправки запроса
if st.button("Predict"):
    # Проверка, что все поля заполнены
    if age.isdigit() and fare.isdigit():
        # Подготовка данных для отправки
        data = {
            "Pclass": int(bulding_type),
            "Age": float(age),
            "Fare": float(fare)
        }

        try:
            # Отправка запроса к Flask API
            response = requests.post(f"http://{ip_api}:{port_api}/predict_model", json=data)

            # Проверка статуса ответа
            if response.status_code == 200:
                prediction = response.json()["prediction"]
                st.success(f"Prediction: {prediction}")
            else:
                st.error(f"Request failed with status code {response.status_code}")
        except ConnectionError as e:
            st.error(f"Failed to connect to the server")
    else:
        st.error("Please fill in all fields with valid numbers.")