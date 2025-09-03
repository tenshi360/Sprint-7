import pandas as pd
import streamlit as st
import plotly.graph_objects as go

car_data = pd.read_csv('vehicles_us.csv')

st.header('Venta de vehículos')
st.subheader('Análisis de las distintas publicaciones de venta para vehículos usados y nuevos\nMarca alguna de las casillas para generar alguno de los 3 gráficos.')

# Tratamiento de datos
# Cambio price a float ya que el dinero suele tener decimales
# Los tipo objetos los cambio a string
car_data['price'] = car_data['price'].astype('float')
car_data['model'] = car_data['model'].astype('string')
car_data['condition'] = car_data['condition'].astype('string')
car_data['fuel'] = car_data['fuel'].astype('string')
car_data['transmission'] = car_data['transmission'].astype('string')
car_data['type'] = car_data['type'].astype('string')
car_data['paint_color'] = car_data['paint_color'].astype('string')

# Cambio a datetime
car_data['date_posted'] = pd.to_datetime(car_data['date_posted'])

# En is 4wd lleno los NaN con 0.0 y luego cambio el tipo de dato a Int
car_data['is_4wd'].fillna(0.0,inplace=True)
car_data['is_4wd'] = car_data['is_4wd'].astype('int64')

# Lógica a ejecutar cuando se hace clic en la casilla de verificación
# Casilla de verificación para generar histograma del odometro
odometer_hist = st.checkbox('Construir un histograma', key="hist")
if odometer_hist: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    fig.update_xaxes(title_text='Cantidad de millas en el odómetro') # Agrega subtitulo al eje X
    fig.update_yaxes(title_text='Cantidad total de vehículos') # Agrega subtitulo al eje Y

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


# Casilla de verificación para generar scatter plot del odometro en relacion al precio
odometer_disp = st.checkbox('Construir un histograma', key="sct")
if odometer_disp:

    st.write('Construir un grafico de dispercion para mostrar la relacion entre precio y odómetro')

    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre Odómetro y Precio')

    fig.update_xaxes(title_text='Cantidad de millas en el odómetro') # Agrega subtitulo al eje X
    fig.update_yaxes(title_text='Precio en dólares') # Agrega subtitulo al eje Y

    st.plotly_chart(fig, use_container_width=True)


# Casilla de verificación para generar grafico de barras del numero de cilindros en relacion al precio
cylinder_bar = st.checkbox('Construir un grafico de barra', key="bar")

# Agrupar sobre cylindros y mostrar precio promedio
avg_price_cylinders = car_data.groupby(['cylinders'])['price'].mean().reset_index(name='average_price')

if cylinder_bar:

    st.write('Construir un grafico de barras para mostrar en promedio cuanto cuesta un vehiculo dependiendo la cantidad de cilindros')

    fig = go.Figure(data=[go.Bar(x=avg_price_cylinders['cylinders'], y=avg_price_cylinders['average_price'])])

    # Titulo
    fig.update_layout(title_text='Relación entre numero de cilindros y Precio (Promedio)')
    fig.update_xaxes(type='category', title_text='Número de cilindros') # Convierte eje X a tipo categórico y agrega subtitulo al eje X
    fig.update_yaxes(title_text='Precio promedio en dólares') # Agrega subtitulo al eje Y

    st.plotly_chart(fig, use_container_width=True)
