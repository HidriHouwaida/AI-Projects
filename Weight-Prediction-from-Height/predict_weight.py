import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool

# Chargement des données
df = pd.read_csv('WeightHeight.csv')

# Préparation des données
X = df['Hauteur (m)'].values.reshape(-1, 1)
y = df['Poids (kg)'].values

# Entraînement du modèle
model = LinearRegression()
model.fit(X, y)

# Prédictions
x_range = np.linspace(X.min(), X.max(), 100)
y_pred = model.predict(x_range.reshape(-1, 1))

# Création du graphique 
source = ColumnDataSource(df)
plot = figure(title="Prédiction du poids à partir de la taille", 
              x_axis_label='Hauteur (m)', 
              y_axis_label='Poids (kg)')

# Nuage de points
plot.circle('Hauteur (m)', 'Poids (kg)', source=source, size=8, alpha=0.5, 
           color='blue', legend_label='Données réelles')

# Droite de régression
plot.line(x_range, y_pred, line_width=2, color='red', 
         legend_label=f'Régression: Poids = {model.coef_[0]:.2f}*Taille + {model.intercept_:.2f}')

# Ajout d'outils interactifs
plot.add_tools(HoverTool(tooltips=[("Taille", "@{Hauteur (m)} m"), 
                                  ("Poids", "@{Poids (kg)} kg")]))

plot.legend.location = "top_left"

show(plot)
