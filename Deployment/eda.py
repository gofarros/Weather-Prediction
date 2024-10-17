import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def run():
    # define pallette
    custom = ['#D1F6CA', '#9BD7F7', '#54ADEB', '#AFE4FC', '#127CDD']

    #buka title
    st.title ('Weather Classification')

    #buat subheader
    st.subheader ('Exploratory Data Analysis (EDA) Klasifikasi Cuaca')

    #load gambar
    image = Image.open('weather.jpg')
    st.image(image, caption = 'photo: weathering with you')

    #buat teks
    st.write ('Berikut adalah Exploratory Data Analysis dari dataset weather classification. Dalam eksplorasi data ini, akan diperoleh beberapa insight mengenai cuaca pada beberapa kondisi.')
    st.markdown ('---') 

    #buka dataframe
    st.write ('## **Dataframe**')
    DF = pd.read_csv('weather_classification_data.csv')
    st.dataframe(DF)
    st.write ('Dataset berisi informasi mengenai metrik-metrik yang berkaitan dengan cuaca, seperti temperatur, kelembapan, dll. Data memiliki 13200 baris dan 11 kolom, dengan target dari data ini adalah "Weather Type". Eksplorasi sederhana menunjukkan tidak ditemukan data kosong maupun data duplikasi, dan data type sudah sesuai masing-masing kolom.')

    # pie chart
    st.write ('## **Persentase Cuaca pada Dataset**')
    st.markdown ('---') 

    total = DF['Weather Type'].value_counts()
    weather_percentage = (total / total.sum()) * 100
    fig = plt.figure(figsize=(5,5))
    palette = sns.color_palette(custom, len(weather_percentage))
    plt.pie(weather_percentage, labels=weather_percentage.index, autopct='%1.1f%%', colors=palette)
    st.pyplot(fig)
    st.write ('Data menunjukkan jumlah yang seimbang antara berawan, hujan, cerah, dan bersalju. Ketika ingin memprediksi cuaca (sebagai target), data yang balance mendukung pembelajaran model machine learning lebih konsisten dan mengurangi bias.')

    # perbedaan cuaca berdasarkan lokasi
    st.write ('## **Perbedaan cuaca berdasarkan lokasi**')
    st.markdown ('---')
    DX = pd.DataFrame(DF.groupby(["Location",'Weather Type']).size()).reset_index()
    DX.columns = ['Location', 'Weather Type', 'Total']
    coastal = DX.query('Location == "coastal"')
    inland = DX.query('Location == "inland"')
    mountain = DX.query('Location == "mountain"')
    fig = plt.figure(figsize=(16, 4))
    plt.subplot(1, 3, 1)
    sns.barplot(data=coastal, x='Weather Type', y='Total', hue='Weather Type', palette=custom)
    plt.title('Weather in coastal')
    plt.subplots_adjust(wspace=0.3)
    plt.subplot(1, 3, 2)
    sns.barplot(data=inland, x='Weather Type', y='Total', hue='Weather Type', palette=custom)
    plt.title('Weather in inland')
    plt.subplots_adjust(wspace=0.3)
    plt.subplot(1, 3, 3)
    sns.barplot(data=mountain, x='Weather Type', y='Total', hue='Weather Type', palette=custom)
    plt.title('Weather in mountain')
    plt.subplots_adjust(wspace=0.3)
    st.pyplot(fig)
    st.write ('Wilayah pegunungan memiliki cuaca bersalju yang paling banyak disusul dengan daratan, sementara wilayah bersalju paling sedikit terletak di pesisir. Kejadian hujan, berawan, dan cerah tidak berbeda jauh pada setiap lokasinya')

    # Perbandingan Indeks UV pada setiap tutupan awan
    st.write ('## **UV Indeks setiap Kondisi Awan**')
    st.markdown ('---')

    fig = plt.figure(figsize=(5,3))
    sns.barplot(data=DF, x='UV Index', y='Cloud Cover', palette=custom)
    st.pyplot(fig)
    st.write ('Jenis tutupan awan dengan UV index paling tunggi terdapat pada saat clear (cerah), sementara UV index yang paling rendah berada ketika awan overcast (tertutup keseluruhan).')

    #Frekuensi cuaca pada setiap musimnya
    st.write ('## **Frekuensi cuaca pada setiap musim**')
    st.markdown ('---')

    heatmap_data = pd.crosstab(DF['Season'], DF['Weather Type'])
    fig = plt.figure(figsize=(7, 5))
    sns.heatmap(heatmap_data, annot=True, cmap=custom, fmt='d')
    plt.title('Weather by Season')
    st.pyplot(fig)
    st.write ('Perbedaan musim mempengaruhi jenis cuaca yang terjadi di daerah tersebut. Perbedaan nilai signifikan ditunjukkan cuaca snowy yang jumlahnya tinggi pada saat "Winter", dan juga sangat sedikit ketika musim-musim lainnya. Cuaca lainnya terjadi relatif konstan.')

if __name__== "__main__":
    run()