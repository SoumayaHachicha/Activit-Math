# lotka_volterra_modele.py

import numpy as np
import matplotlib.pyplot as plt

# Modèle de Lotka-Volterra (proie-prédateur)

def lotka_volterra_model(alpha, beta, delta, gamma, x0, y0, t):
dt = t[1] - t[0]
x = np.zeros_like(t)
y = np.zeros_like(t)
x[0] = x0
y[0] = y0
for i in range(1, len(t)):
dx = alpha * x[i-1] - beta * x[i-1] * y[i-1]
dy = delta * x[i-1] * y[i-1] - gamma * y[i-1]
x[i] = x[i-1] + dt * dx
y[i] = y[i-1] + dt * dy
if x[i] < 0 or y[i] < 0 or np.isnan(x[i]) or np.isnan(y[i]):
return np.full_like(t, np.nan), np.full_like(t, np.nan)
return x, y

# Simulation avec paramètres réalistes

def simuler_et_afficher():
x0 = 40 # lapins
y0 = 9 # renards
t = np.linspace(0, 30, 300) # 30 jours, 300 points

# Paramètres du modèle
alpha = 1.0 # taux de reproduction des lapins
beta = 0.1 # taux de prédation
delta = 0.1 # conversion des proies en prédateurs
gamma = 1.5 # mortalité des prédateurs

# Simulation
x, y = lotka_volterra_model(alpha, beta, delta, gamma, x0, y0, t)

# Affichage
plt.figure(figsize=(10, 5))
plt.plot(t, x, label="Lapins", color='green')
plt.plot(t, y, label="Renards", color='red')
plt.xlabel("Temps (jours)")
plt.ylabel("Population")
plt.title("Modèle de Lotka-Volterra : Proies et Prédateurs")
plt.legend()
plt.grid(True)
plt.show()

# Lancement principal

if __name__ == "__main__":
simuler_et_afficher()
