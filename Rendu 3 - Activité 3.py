# Partie 3: Application sur des données réels et recalibrage du modèle

# 1. Tracer la courbe du nombre d’utilisateurs.

# Charger les données du fichier CSV
df = pd.read_csv("Dataset_nombre_utilisateurs.csv")
df = df.rename(columns={'Jour': 'Temps', 'Utilisateurs': 'Nombre_utilisateurs'})

# Afficher la courbe du nombre d'utilisateurs
plt.figure(figsize=(12, 6))
plt.plot(df['Temps'], df['Nombre_utilisateurs'])
plt.xlabel("Jour")
plt.ylabel("Nombre d'utilisateurs")
plt.title("Nombre d'utilisateurs au fil du temps")
plt.grid(True)
plt.show()

# 2. Quand est ce qu’on atteint la phase de “saturation” ? Quand est ce qu’on atteint 50% de la saturation ?

# On utilise une valeur proche du max des utilisateurs dans le dataset
K_estime = df['Nombre_utilisateurs'].max()

# Approximation du point de saturation (95% de K)
saturation_threshold = 0.95 * K_estime
saturation_day = df[df['Nombre_utilisateurs'] >= saturation_threshold]['Temps'].min()

# Approximation du jour à 50% de saturation
half_saturation = 0.5 * K_estime
half_saturation_day = df[df['Nombre_utilisateurs'] >= half_saturation]['Temps'].min()

print(f"Jour approximatif de saturation: {saturation_day}")
print(f"Jour approximatif à 50% de saturation: {half_saturation_day}")

# 3. Calculer la MSE pour les 2 solutions sur plusieurs intervalles de temps.

# Intervalles de temps (en jours)
intervals = [(0, 30), (30, 90), (90, 180), (180, 365)]

for start, end in intervals:
    # Sélectionner les données réelles dans l'intervalle
    real_data_interval = df[(df['Temps'] >= start) & (df['Temps'] <= end)]['Nombre_utilisateurs']
    #Euler
    time_interval = time_euler[(time_euler >= start) & (time_euler <= end)]
    P_euler_interval = np.interp(time_interval, time_euler, P_euler)  # Interpoler Euler values
    #Analytical
    P_analytical_interval = analytical_logistic(P0, r, K, time_interval)
    #MSE Calculation
    mse_euler = mean_squared_error(real_data_interval, P_euler_interval[:len(real_data_interval)])
    mse_analytical = mean_squared_error(real_data_interval, P_analytical_interval[:len(real_data_interval)])
    print(f"MSE entre {start} et {end} jours (Euler): {mse_euler}")
    print(f"MSE entre {start} et {end} jours (Analytique): {mse_analytical}")

# 4. Tracer simultanément les 3 courbes.

# Tracer les trois courbes
plt.figure(figsize=(12, 6))
plt.plot(df['Temps'], df['Nombre_utilisateurs'], label="Données réelles")
plt.plot(time_euler, P_euler, label="Approximation d'Euler")
plt.plot(time_euler, P_analytical, label="Solution analytique")
plt.xlabel("Temps (Jours)")
plt.ylabel("Nombre d'utilisateurs")
plt.title("Comparaison des données réelles, de l'approximation d'Euler et de la solution analytique")
plt.legend()
plt.grid(True)
plt.show()

# 5. Expliquer pour quelle(s) raison(s) les écarts sont significatifs ?
# Les écarts peuvent être dus à:
# - Saisonnalité: L'adoption peut varier selon les périodes de l'année.
# - Campagnes marketing: Des pics peuvent être liés à des efforts marketing.
# - Facteurs externes: Événements, concurrence, économie.
# - Limitations du modèle: Le modèle logistique est une simplification.

# 6. Proposer de nouvelles hypothèses pour donner une meilleur approximation
# Hypothèses à considérer:
# - Taux de croissance variable (r): Influencé par le marketing ou la saisonnalité.
# - Capacité maximale variable (K): La taille du marché peut évoluer.
# - Incorporer des facteurs externes: Ajouter des termes pour le marketing ou autres.

# 7. Recalculer la MSE et retracer les courbes

# Exemple de modèle modifié (Taux de croissance variable)
def modified_logistic(P0, r_func, K, t):
    """
    Équation logistique avec un taux de croissance variable.
    r_func doit être une fonction qui prend le temps (t) en entrée et renvoie le taux de croissance à ce moment.
    """
    return K / (1 + (K - P0) / P0 * np.exp(-np.cumsum([r_func(ti) for ti in t])))

# Exemple de fonction de taux de croissance (peut être ajustée)
def r_func(t):
    """
    Exemple: Un taux de croissance qui diminue avec le temps.
    """
    return 0.05 * np.exp(-t / 100)  # Décroissance exponentielle du taux de croissance

# Recalculer en utilisant le modèle modifié
P_modified = modified_logistic(P0, r_func, K, time_euler)

# Calculer la MSE
mse_modified = mean_squared_error(df['Nombre_utilisateurs'], P_modified[:len(df['Nombre_utilisateurs'])])
print(f"MSE avec le modèle modifié: {mse_modified}")

# Tracer les résultats
plt.figure(figsize=(12, 6))
plt.plot(df['Temps'], df['Nombre_utilisateurs'], label="Données réelles")
plt.plot(time_euler, P_euler, label="Approximation d'Euler (Original)")
plt.plot(time_euler, P_analytical, label="Solution analytique (Original)")
plt.plot(time_euler, P_modified, label="Modèle modifié")
plt.xlabel("Temps (Jours)")
plt.ylabel("Nombre d'utilisateurs")
plt.title("Comparaison des modèles")
plt.legend()
plt.grid(True)
plt.show()
