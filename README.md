 # Modèle de Régression Linéaire

Ce référentiel contient un programme Python qui démontre comment utiliser la classe **LinearRegression** de la bibliothèque **scikit-learn** pour effectuer une régression linéaire sur un ensemble de données d'exemple.

## Dépendances
- scikit-learn
- numpy
- matplotlib

Assurez-vous d'avoir installé ces dépendances avant d'exécuter le programme.

## Utilisation

1. Clonez le référentiel :

   ```
   git clone https://github.com/votre-nom-utilisateur/regression-lineaire.git
   ```

2. Accédez au répertoire du projet :

   ```
   cd regression-lineaire
   ```

3. Exécutez le programme :

   ```
   python regression_lineaire.py
   ```

## Exemple

Le programme ajuste un modèle de régression linéaire sur un ensemble de données d'exemple et prédit une nouvelle valeur en utilisant le modèle entraîné. Les données d'exemple sont définies comme suit :

```python
# Import des bibliothèques
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Données d'exemple
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 4.2, 6.1, 8.0, 10.1])
```

Le programme crée ensuite un objet **LinearRegression** et l'entraîne sur les données d'exemple :

```python
# Création d'un objet LinearRegression
model = LinearRegression()

# Apprentissage sur les données
model.fit(x.reshape(-1, 1), y)
```

Après l'entraînement, le programme effectue une prédiction pour une nouvelle valeur de `x` :

```python
# Prédiction pour une nouvelle valeur de x
new_x = np.array([6])
predicted_y = model.predict(new_x.reshape(-1, 1))
```
Le programme affiche ensuite les coefficients de la droite de régression et la prédiction pour la nouvelle valeur de `x` :

```python
# Affichage des coefficients de la droite de régression
print('Coefficients : a =', model.coef_[0], ' b =', model.intercept_)

# Affichage de la prédiction pour la nouvelle valeur de x
print('Prediction for x =', new_x[0], ' : y =', predicted_y[0])
```
Enfin, le programme trace les points des données d'exemple, la droite de régression et le point prédit :

```python
# Affichage des données et de la droite de régression
plt.scatter(x, y)
plt.plot([min(x), max(x)], [model.predict([[min(x)]])[0], model.predict([[max(x)]])[0]], color='red')

# Placement du point prédit en violet
plt.scatter(new_x, predicted_y, color='purple')
plt.show()
```

Vous verrez un graphique avec les points des données d'exemple, la droite de régression et le point prédit pour la nouvelle valeur de `x`.

N'hésitez pas à modifier les données d'exemple ou à expérimenter avec différents ensembles de données pour observer la régression linéaire en action.


 

