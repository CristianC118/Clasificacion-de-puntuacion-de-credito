
"""
    El conjunto de datos tiene muchas características que pueden entrenar un modelo de Machine Learning
  para la clasificación de puntajes crediticios.

    Exploración de las características una por una."""


# Importar Librerías
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = 'plotly_white'



# Lectura del archivo
data= pd.read_csv('Datos/Credit_Score_Data/train.csv')



# Exploración de la función ocupación para saber si afecta o no a los puntajes crediticios.
fig = px.box(data,
            x='Occupation',
            color='Credit_Score',
            title='Puntajes de crédito basadas en la ocupación',
            color_discrete_map={'Poor':'red',
                                'Standard':'yellow',
                                'Good':'green'})

fig.show()
# Diferencias prácticamente nulas a la hora de ver las puntuaciones de todas las ocupaciones vistas en los datos.



# Afecta o no los ingresos anuales a los puntajes crediticios.
fig = px.box(data,
            x='Credit_Score',
            y='Annual_Income',
            color='Credit_Score',
            title='Puntajes de crédito basadas en ingresos anuales',
            color_discrete_map={'Poor':'red',
                                'Standard':'yellow',
                                'Good':'green'})

fig.update_traces(quartilemethod='exclusive')
fig.show()
# Mientras más gane anualmente, mejor será su puntaje crediticio.



# Exploración para saber si el salario mensual bruto afecta o no los puntajes de crédito.
fig = px.box(data,
            x='Credit_Score',
            y='Monthly_Inhand_Salary',
            color='Credit_Score',
            title='Puntajes de crédito basadas en el salario mensual bruto',
            color_discrete_map={'Poor':'red',
                                'Standard':'yellow',
                                'Good':'green'})

fig.update_traces(quartilemethod='exclusive')
fig.show()
# Al igual que los ingresos anuales, cuanto más salario mensual gane, mejor será su puntaje crediticio.



# Analisis de si tener más cuentas bancarias afecta los puntajes de crédito o no.
fig = px.box(data,
            x='Credit_Score',
            y='Num_Bank_Accounts',
            color='Credit_Score',
            title='Puntajes de crédito basadas en el número de cuentas bancarias',
            color_discrete_map={'Poor':'red',
                                'Standard':'yellow',
                                'Good':'green'})

fig.update_traces(quartilemethod='exclusive')
fig.show()
#    Mantener más de 5 cuentas no es bueno para tener un buen puntaje crediticio. Una persona debe tener...
#  de 2 - 3 cuentas bancarias solamente. Por lo tanto, tener más cuentas no tiene un impacto positivo en los puntajes.



# Impacto en el puntaje de acuerdo a la cantidad de tarjetas de crédito que posee.
fig = px.box(data,
            x='Credit_Score',
            y='Num_Credit_Card',
            color='Credit_Score',
            title='Puntajes de crédito basadas en el número de tarjetas de crédito',
            color_discrete_map={'Poor':'red',
                                'Standard':'yellow',
                                'Good':'green'})

fig.update_traces(quartilemethod='exclusive')
fig.show()
#    Al igual que las cuentas bancarias, tener más tarjetas de crédito no tendrá un impacto positivo...
#  en sus puntajes crediticios. Tener de 3 a 5 tarjetas es bueno para su puntaje de crédito.



# Impacto en los puntajes de crédito en función de cuánto interés promedio paga en préstamos y EMI (Tasa Mensual Equivalente)
fig = px.box(data,
            x="Credit_Score",
            y="Interest_Rate",
            color="Credit_Score",
            title="Puntajes de crédito basadas en las tasas de interés promedio",
            color_discrete_map={'Poor':'red',
                                'Standard':'yellow',
                                'Good':'green'})

fig.update_traces(quartilemethod="exclusive")
fig.show()
#    Si la tasa de interés promedio es de 4 a 11%, el puntaje de crédito es bueno. Tener una tasa de interés promedio...
#  de más de 15% es malo para el puntaje crediticio.



# Cuántos préstamos debe tener a la vez para tener un buen puntaje crediticio.
fig = px.box(data,
            x="Credit_Score",
            y="Num_of_Loan",
            color="Credit_Score",
            title="Puntajes de crédito basadas en la cantidad de préstamos tomadas por la persona",
            color_discrete_map={'Poor':'red',
                                'Standard':'yellow',
                                'Good':'green'})

fig.update_traces(quartilemethod="exclusive")
fig.show()
#    Para tener un buen puntaje de crédito, no debe tomar más de 1 a 3 préstamos a la vez. Tener más de tres préstamos a la vez...
#  tendrá un impacto negativo en sus puntajes de crédito.



# Retrasar o no los pagos en la fecha de vencimiento afecta o no a sus puntajes de crédito?
fig = px.box(data,
            x="Credit_Score",
            y="Delay_from_due_date",
            color="Credit_Score",
            title="Puntajes de crédito basadas en el número promedio de días de retraso en los pagos con tarjeta de crédito",
            color_discrete_map={'Poor':'red',
                                'Standard':'yellow',
                                'Good':'green'})

fig.update_traces(quartilemethod="exclusive")
fig.show()
#    Puede retrasar el pago de sus tarjetas de 5 a 14 díoas a partir de la fecha de vencimiento. Retrasar sus pagos por más de...
#  17 días a partir de la fecha de vencimiento afectará negativamente sus puntajes.



# Retrasar los pagos con frecuencia afectará o no a los puntajes de crédito?
fig = px.box(data,
            x="Credit_Score",
            y="Num_of_Delayed_Payment",
            color="Credit_Score",
            title="Puntajes de crédito basadas en el número de pagos atrasados",
            color_discrete_map={'Poor':'red',
                                'Standard':'yellow',
                                'Good':'green'})

fig.update_traces(quartilemethod="exclusive")
fig.show()
#    Retrasar de 4 a 12 pagos desde la fecha de vencimiento no afectará sus puntajes de crédito. Pero retrasar más de 12 pagos...
#  desde la fecha de vencimiento afectará negativamente sus puntajes de crédito.



# Tener más deudas afectará los puntajes de crédito?
fig = px.box(data,
            x="Credit_Score",
            y="Outstanding_Debt",
            color="Credit_Score",
            title="Puntajes de crédito basadas en la deuda pendiente",
            color_discrete_map={'Poor':'red',
                                'Standard':'yellow',
                                'Good':'green'})

fig.update_traces(quartilemethod="exclusive")
fig.show()
#    Una deuda pendiente de $ 380 – $ 1150 no afectará sus puntajes de crédito. Pero siempre tener una deuda de...
#  más de $ 1338 afectará negativamente sus puntajes de crédito.



# Tener un alto índice de utilización de tarjeta de crédito afectará a los puntajes de crédito o no.
fig = px.box(data,
            x="Credit_Score",
            y="Credit_Utilization_Ratio",
            color="Credit_Score",
            title="Puntaje de crédito basadas en la tasa de utilización de la tarjeta crédito",
            color_discrete_map={'Poor':'red',
                                'Standard':'yellow',
                                'Good':'green'})

fig.update_traces(quartilemethod="exclusive")
fig.show()
#    Índice de utilización de crédito significa su deuda total dividida por su crédito total disponible. De acuerdo con la...
#  cifra anterior, su índice de utilización de crédito no afecta sus puntajes de crédito.



# Cómo la edad del historial de crédito de una persona afecta los puntajes de crédito.
fig = px.box(data,
            x="Credit_Score",
            y="Credit_History_Age",
            color="Credit_Score",
            title="Credit Scores Based on Credit History Age",
            color_discrete_map={'Poor':'red',
                                'Standard':'yellow',
                                'Good':'green'})

fig.update_traces(quartilemethod="exclusive")
fig.show()
#    Tener un largo historial de crédito resulta en mejores puntajes de crédito.



# Cuántos EMI (Tasa Mensual Equivalente) puede tener en un mes para un buen puntaje de crédito:
fig = px.box(data,
            x="Credit_Score",
            y="Total_EMI_per_month",
            color="Credit_Score",
            title="Puntajes crediticias basadas en el número total de EMI por mes",
            color_discrete_map={'Poor':'red',
                                'Standard':'yellow',
                                'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()
#    La cantidad de EMI que está pagando en un mes no afecta mucho los puntajes de crédito.



# Sus inversiones mensuales afectan sus puntajes de crédito o no?
fig = px.box(data,
            x="Credit_Score",
            y="Amount_invested_monthly",
            color="Credit_Score",
            title="Puntajes de crédito basadas en la cantidad invertida mensualmente",
            color_discrete_map={'Poor':'red',
                                'Standard':'yellow',
                                'Good':'green'})

fig.update_traces(quartilemethod="exclusive")
fig.show()
#    La cantidad de dinero que invierte mensualmente no afecta mucho sus puntajes de crédito.



# Tener una cantidad baja al final del mes afecta los puntajes de crédito o no?
fig = px.box(data,
            x="Credit_Score",
            y="Monthly_Balance",
            color="Credit_Score",
            title="Puntajes de crédito basadas en el saldo mensual restante",
            color_discrete_map={'Poor':'red',
                                'Standard':'yellow',
                                'Good':'green'})

fig.update_traces(quartilemethod="exclusive")
fig.show()
#    Tener un saldo mensual alto en su cuenta al final del mes es bueno para sus puntajes de crédito.
#  Un saldo mensual de menos de $250 es malo para los puntajes de crédito.