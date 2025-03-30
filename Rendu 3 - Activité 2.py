# Partie 2: Etude de la précision de la solution

# 1. Expliquer la cohérence de cette solution avec le lancement exponentiel et la saturation
# La solution analytique capture la croissance exponentielle initiale lorsque P est petit par rapport à K. Lorsque P approche K, la croissance ralentit.

# 2. Implémenter cette fonction
def analytical_logistic(P0, r, K, t):
    """
    Calcul la solution analytique de l'équation différentielle logistique.

    Args:
        P0: Population initiale.
        r: Taux de croissance.
        K: Capacité maximale.
        t: Temps (scalaire ou tableau).

    Returns:
        La population au temps t.
    """
    return K / (1 + (K - P0) / P0 * np.exp(-r * t))

# Calculer la solution analytique pour les mêmes valeurs de temps que Euler
P_analytical = analytical_logistic(P0, r, K, time_euler)

# Afficher les résultats
plt.plot(time_euler, P_analytical)
plt.xlabel("Temps (jours)")
plt.ylabel("Population")
plt.title("Solution analytique de la croissance logistique")
plt.grid(True)
plt.show()

# 3. Comparer les résultats d’approximations avec le résultat de cette fonction pour plusieurs valeurs en vous basant sur la MSE.

# Calculer la MSE
mse = mean_squared_error(P_analytical, P_euler) # Compare la solution analytique et Euler
print(f"Erreur quadratique moyenne (MSE): {mse}")

# 4. Tracez les courbes de votre approximation et de la solution analytique.

# Tracer les deux solutions
plt.plot(time_euler, P_euler, label="Approximation d'Euler")
plt.plot(time_euler, P_analytical, label="Solution analytique")
plt.xlabel("Temps (jours)")
plt.ylabel("Population")
plt.title("Comparaison de l'approximation d'Euler et de la solution analytique")
plt.legend()
plt.grid(True)
plt.show()
