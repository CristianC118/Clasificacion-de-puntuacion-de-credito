
"""
    En esta primera fase observamos y analizamos datos
  para ver sí no hay algún cabo suelto el cuál deba ser corregido."""


# Importar Librerías
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = 'plotly_white'


print('\nVisualización de Datos:\n')


# Lectura del archivo y Visualizamos los Datos
data= pd.read_csv('Datos/Credit_Score_Data/train.csv')
print(data)


print('\nObservación de Datos:\n')


# Observamos la información
print(data.info())


print('\nValores Nulos(?:\n')


# Vistazo para ver valores nulos en caso de que existan
print(data.isnull().sum())
# El conjunto no tiene ningún valor nulo


print('\nValores de Columna:\n')


# Vistazo a los valores de la columna
print(data['Credit_Score'].value_counts())