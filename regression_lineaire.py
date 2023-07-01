# Import des Bibliothéques :
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
# Données d'exemple : x et y sont deux vecteurs numpy de même taille
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 4.2, 6.1, 8.0, 10.1])

# Création d'un objet LinearRegression
model = LinearRegression()

# Apprentissage sur les données
model.fit(x.reshape(-1, 1), y)

# Prédiction pour une nouvelle valeur de x
new_x = np.array([6])
predicted_y = model.predict(new_x.reshape(-1, 1))

# Affichage des coefficients de la droite de régression
print('Coefficients : a =', model.coef_[0], ' b =', model.intercept_)

# Affichage de la prédiction pour la nouvelle valeur de x
print('Prediction for x =', new_x[0], ' : y =', predicted_y[0])

# Affichage des données et de la droite de régression
plt.scatter(x, y)
plt.plot([min(x), max(x)], [model.predict([[min(x)]])[0],
model.predict([[max(x)]])[0]], color='red')

# on place la prédiction en violet
plt.scatter(new_x, predicted_y, color='purple')
plt.show()
