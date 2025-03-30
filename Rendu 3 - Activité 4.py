# Partie 4: Question ouverte

# Le pôle développement de la SAS souhaite lancer un nouveau produit et veut baser son business modèle sur les résultats du business modèle précédent.
# Vous êtes mandaté pour définir un plan de projection du chiffre d’affaires et des bénéfices réalisés par mois sur l’année de lancement du produit.
# Est-ce que le business modèle est rentable ?
# Est-ce qu’il manque des hypothèses ?
# Voici les informations dont vous disposez:
# - Le nombre d’utilisateurs maximum par serveur: 2000
# - Prix d’un serveur par mois: 1000 euros
# - Estimation du coût marketing marginal d'acquisition par utilisateur 10 euros
# - Budget de campagne marketing corporate branding concentré à 35% au lancement du produit puis réparti équitablement sur le reste du mois: 50 000 euros
# - Coût de l’abonnement mensuel du nouveau produit: 11,99 euros/mois
# - Estimation de la taille du marché: 400 000 utilisateurs
# - Part de marché: 20%
# - Croissance initial moyennement rapide
# - Nombre initial d’utilisateur au lancement: 500

def business_model(P0, r, K, months, subscription_price, server_capacity, server_cost, acquisition_cost, marketing_budget):
    """
    Simule le modèle économique sur une année.

    Args:
        P0: Nombre initial d'utilisateurs.
        r: Taux de croissance.
        K: Capacité maximale (taille du marché * part de marché).
        months: Nombre de mois à simuler.
        subscription_price: Prix de l'abonnement mensuel par utilisateur.
        server_capacity: Nombre d'utilisateurs par serveur.
        server_cost: Coût mensuel par serveur.
        acquisition_cost: Coût marginal d'acquisition par utilisateur.
        marketing_budget: Budget marketing total.

    Returns:
        Un DataFrame Pandas avec les revenus, les coûts et les bénéfices mensuels.
    """

    # Calculer le nombre d'utilisateurs par mois
    time = np.arange(0, months, 1/30)
    users = analytical_logistic(P0, r, K, time*30)
    df = pd.DataFrame({'Users': users})
    df=df.groupby(df.index // 30).agg({'Users':'last'})

    # Calculer les revenus
    df['Revenue'] = df['Users'] * subscription_price

    # Calculer les coûts de serveur
    df['Servers'] = np.ceil(df['Users'] / server_capacity)
    df['ServerCost'] = df['Servers'] * server_cost

    # Calculer les coûts marketing
    df['MarketingCost'] = acquisition_cost * df['Users'] + marketing_budget/months
    df['MarketingCost'][0] = acquisition_cost * df['Users'][0] + marketing_budget*0.35 #Dépense initiale
    df['MarketingCost'][1:] = acquisition_cost * df['Users'][1:] + (marketing_budget*(1-0.35))/(months-1) #Mois restants

    # Calculer les bénéfices
    df['Profit'] = df['Revenue'] - df['ServerCost'] - df['MarketingCost']

    return df

# Paramètres
P0 = 500
r = 0.02  # Ajustement du taux de croissance (moyennement rapide)
K = 400000 * 0.2  # Part de marché de la taille totale du marché
months = 12
subscription_price = 11.99
server_capacity = 2000
server_cost = 1000
acquisition_cost = 10
marketing_budget = 50000

# Exécuter la simulation du modèle économique
results = business_model(P0, r, K, months, subscription_price, server_capacity, server_cost, acquisition_cost, marketing_budget)

# Afficher les résultats
print(results)

# Tracer les résultats
plt.plot(results.index, results['Profit'])
plt.xlabel("Mois")
plt.ylabel("Bénéfice")
plt.title("Bénéfice par mois")
plt.grid(True)
plt.show()

# Est-ce rentable?
cumulative_profit = results['Profit'].sum()
print(f"Bénéfice cumulé après un an: {cumulative_profit}")

# Hypothèses supplémentaires à considérer:
# - Taux de désabonnement (churn): Un pourcentage d'utilisateurs annule son abonnement chaque mois.
# - Coût d'acquisition variable: Le coût d'acquisition d'un utilisateur peut augmenter à mesure que le marché se sature.
# - Différents niveaux d'abonnement: Proposer différents plans tarifaires pourrait augmenter les revenus.
# - Échelonnement des serveurs: Les serveurs ne sont pas toujours ajoutés en parfaite synchronisation avec la croissance des utilisateurs.
