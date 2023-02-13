

# Importar Librerías
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = 'plotly_white'



# Lectura del archivo
data= pd.read_csv('Datos/Credit_Score_Data/train.csv')


"""
    Modelo de clasificación de puntaje crediticio.

  Una característica más importante (Credit Mix) en el conjunto de datos es valiosa para determinar los puntajes de crédito.
La función de combinación de crédito informa sobre los tipos de créditos y préstamos que ha tomado.

  Como la columna Credit_Mix es categórica, transformar en una característica numérica para que podamos usarla para entrenar
un modelo de Machine Learning para la tarea de clasificación de puntaje de crédito."""

data["Credit_Mix"] = data["Credit_Mix"].map({"Standard": 1,
                              "Good": 2,
                              "Bad": 0})



# Dividir los datos en características y etiquetas seleccionando las características que consideramos importantes para nuestro modelo:
from sklearn.model_selection import train_test_split
x = np.array(data[["Annual_Income", "Monthly_Inhand_Salary",
                  "Num_Bank_Accounts", "Num_Credit_Card",
                  "Interest_Rate", "Num_of_Loan",
                  "Delay_from_due_date", "Num_of_Delayed_Payment",
                  "Credit_Mix", "Outstanding_Debt",
                  "Credit_History_Age", "Monthly_Balance"]])

y = np.array(data[["Credit_Score"]])



# Dividarlos datos en conjuntos de entrenamiento y prueba y avancemos entrenando un modelo de clasificación de puntaje de crédito:
xtrain, xtest, ytrain, ytest = train_test_split(x, y,
                                                    test_size=0.33,
                                                    random_state=42)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(xtrain, ytrain)



# Hacer predicciones a partir de nuestro modelo dando entradas a nuestro modelo de acuerdo con las características que usamos para entrenar el modelo:
print("Credit Score Prediction : ")
a = float(input("Annual Income: "))
b = float(input("Monthly Inhand Salary: "))
c = float(input("Number of Bank Accounts: "))
d = float(input("Number of Credit cards: "))
e = float(input("Interest rate: "))
f = float(input("Number of Loans: "))
g = float(input("Average number of days delayed by the person: "))
h = float(input("Number of delayed payments: "))
i = input("Credit Mix (Bad: 0, Standard: 1, Good: 3) : ")
j = float(input("Outstanding Debt: "))
k = float(input("Credit History Age: "))
l = float(input("Monthly Balance: "))

features = np.array([[a, b, c, d, e, f, g, h, i, j, k, l]])
print("Predicted Credit Score = ", model.predict(features))
# Así es como podemos usar Machine Learning para la tarea de clasificación de puntaje de crédito usando Python.



"""
    Nota:

  Clasificar a los clientes en función de sus puntajes de crédito ayuda a los bancos y compañías de tarjetas de crédito a emitir préstamos de inmediato a
clientes con buena solvencia. Una persona con un buen puntaje de crédito obtendrá préstamos de cualquier banco e institución financiera."""