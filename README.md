## Sprint-7
# Proyecto Sprint 7 de TripleTen

# Tablero Interactivo de Listados de Vehículos

![Streamlit Badge](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly Badge](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)
![Render Badge](https://img.shields.io/badge/Render-46E0B3?style=for-the-badge&logo=render&logoColor=white)
![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## Tabla de Contenidos

- [Acerca del Proyecto](#acerca-del-proyecto)
- [Características](#características)
- [Datos y Gráficas](#datos-y-gráficas)
- [Primeros Pasos](#primeros-pasos)
  - [Requisitos Previos](#requisitos-previos)
  - [Instalación](#instalación)
- [Despliegue](#despliegue)
- [Uso](#uso)
- [Desarrollado con](#desarrollado-con)
- [Agradecimientos](#agradecimientos)

---

## Acerca del Proyecto

Esta es una aplicación web desarrollada con Streamlit que ofrece un tablero interactivo para analizar datos de listados de vehículos.  
El proyecto demuestra un flujo completo de desarrollo y despliegue, desde la configuración de un entorno virtual y control de versiones con Git, hasta la implementación en la plataforma en la nube Render.

---

## Características

- **Visualización Dinámica de Gráficas**: Selección y renderizado de tres gráficas distintas de Plotly (Histograma, Dispersión y Barras) mediante un menú interactivo.
- **Visualización de Datos**: Explora aspectos clave como el millage, la relación entre precio y odómetro, y el precio promedio según los cilindros.

---

## Datos y Gráficas

El conjunto de datos `vehicle_listings.csv` se visualiza mediante:

- **Histograma del Odómetro**: Distribución del kilometraje de los vehículos.
- **Dispersión Precio vs. Odómetro**: Relación entre el precio y el uso del vehículo.
- **Gráfico de Barras de Cilindros y Precio Promedio**: Comparación del precio medio según el número de cilindros.

---

## Primeros Pasos

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes)

### Instalación

1. **Clona el repositorio**:

```bash
git clone https://github.com/tenshi360/Sprint-7
cd Sprint-7
```

2. **Crea y activa un entorno virtual:**:

```bash
python -m venv vehicles_env
source vehicles_env/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instala las dependencias:**:

```bash
pip install -r requirements.txt
```

## Despliegue

Esta aplicación está desplegada utilizando Render.com. El proceso de despliegue está configurado para compilar e implementar automáticamente la app cada vez que se realicen cambios en la rama principal del repositorio en GitHub.


**Configuración en Render:**
- Tipo de Servicio: Web Service
- Comando de Build:

```bash
pip install -r requirements.txt
```

```bash
streamlit run app.py
```


## Uso

Para ejecutar la app localmente, asegúrate de tener tu entorno virtual activo y ejecuta el siguiente comando en tu terminal:

```bash
streamlit run app.py
```


## Desarrollado con

- [Streamlit](https://streamlit.io/)  
- [Plotly](https://plotly.com/python/)  
- [Pandas](https://pandas.pydata.org/)  
- [Render](https://render.com/)


## Agradecimientos

Agradesco a TripleTen por enseñarme todo lo que he aprendido hasta ahora en el Bootcamp de Data Science.