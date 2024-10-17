import streamlit as st
import pandas as pd
import pickle
from PIL import Image

with open('model_rf.pkl', 'rb') as file:
    model_rf = pickle.load(file)

def run():
    st.title('Weather Prediction')

    #load gambar
    image = Image.open('weather.jpg')
    st.image(image, caption = 'photo: weathering with you')

    with st.form('form_weather'):
        temperature = st.slider('Temperature: ', value=24, min_value=-50, max_value=150)
        humidity = st.slider('Humidity: ', value=50, min_value=0, max_value=120)
        wind_speed = st.slider('Wind Speed: ', value=50, min_value=0, max_value=100)
        precipitation = st.slider('Precipitation: ', value=0, min_value=0, max_value=100)
        cloud_cover = st.selectbox('Cloud Cover: ', ['clear', 'partly cloudy', 'cloudy', 'overcast'])
        atmospheric_pressure = st.slider('Atmospheric Pressure: ', min_value=700, max_value=1500)
        uv_index = st.number_input('UV Index: ', value=0, min_value=0, max_value=20)
        season = st.selectbox('Season: ', ['Spring', 'Summer', 'Fall', 'Winter'])
        visibility = st.number_input('Visibility: ', value=3.0, min_value=0.0, max_value=30.0)
        location = st.selectbox('Location: ', ['inland', 'mountain', 'coastal'])
        
        submitted = st.form_submit_button('Predict')

    st.write('## Submitted Data')
    data_inf = {
        'Temperature': temperature,
        'Humidity': humidity,
        'Wind Speed': wind_speed,
        'Precipitation': precipitation,
        'Cloud Cover': cloud_cover,
        'Atmospheric Pressure': atmospheric_pressure,
        'UV Index': uv_index,
        'Season': season,
        'Visibility': visibility,
        'Location': location
    }

    data_inf_df = pd.DataFrame([data_inf])
    st.dataframe(data_inf_df)

    if submitted:
        y_pred_inf = model_rf.predict(data_inf_df)
        value_predict = y_pred_inf[0]
        st.write(f'## Weather Today: ', value_predict)

if __name__ == '__main__':
    run()

   
