import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error

# Partie 1: Modélisation et compréhension mathématique du problème

# 1. Écrire l’équation différentielle avec les valeurs du problème.
# dP/dt = r * P * (1 - P/K)
# où:
# P = population (nombre de clients) au temps t
# r = taux de croissance
# K = capacité maximale (taille du marché total)
# Avec les valeurs fournies:
# dP/dt = 0.05 * P * (1 - P/100000)

# 2. Expliquer pourquoi l’interprétation fonctionne au début de l’activité et à la fin de l’activité.
# Début: Au début, P est petit, donc P/K est proche de 0. L'équation se rapproche de dP/dt = r * P, ce qui est une croissance exponentielle.
# Fin: Lorsque P approche K, P/K approche 1, et (1 - P/K) approche 0. Cela signifie que dP/dt approche 0, la croissance ralentit.

# 3. Utiliser la méthode de discrétisation pour obtenir l’équation d’Euler qui permet d’approximer la valeur de la solution.
# P(t + dt) = P(t) + dt * dP/dt
# En substituant l'équation logistique:
# P(t + dt) = P(t) + dt * r * P(t) * (1 - P(t)/K)

# 4. Implémenter en Python cette équation en choisissant un pas approprié.
def euler_logistic(P0, r, K, dt, num_steps):
    """
    Approximation de la solution de l'équation différentielle logistique en utilisant la méthode d'Euler.

    Args:
        P0: Population initiale.
        r: Taux de croissance.
        K: Capacité maximale.
        dt: Pas de temps.
        num_steps: Nombre de pas à effectuer.

    Returns:
        Un tuple contenant les valeurs de temps et les valeurs de population à chaque pas.
    """
    time = np.arange(0, num_steps * dt, dt)
    P = np.zeros(num_steps)
    P[0] = P0

    for i in range(1, num_steps):
        P[i] = P[i-1] + dt * r * P[i-1] * (1 - P[i-1]/K)

    return time, P

# Paramètres
P0 = 1000
r = 0.05
K = 100000
dt = 1  # Pas de temps (1 jour)
num_steps = 365  # Nombre de jours dans l'année

# Exécuter la méthode d'Euler
time_euler, P_euler = euler_logistic(P0, r, K, dt, num_steps)

# Afficher les résultats
plt.plot(time_euler, P_euler)
plt.xlabel("Temps (jours)")
plt.ylabel("Population")
plt.title("Approximation de la croissance logistique par la méthode d'Euler")
plt.grid(True)
plt.show()
