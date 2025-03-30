import numpy as np

#Script pour obtenir x et y

# Définition de la matrice A et du vecteur b
A = np.array([[10, 5], [-4, 1]])
b = np.array([9000, 50])

# Calcul de la solution
x = np.linalg.inv(A).dot(b)

# Arrondi de x à l'entier inférieur
x_rounded = np.floor(x)

# Arrondi de y à 2 décimales supérieures
y_rounded = np.ceil(x * 100) / 100

print(f"Nombre d'unités x (arrondi inférieur) : {x_rounded}")
print(f"Quantité de matière première y (arrondi supérieur à 2 décimales) : {y_rounded}")
