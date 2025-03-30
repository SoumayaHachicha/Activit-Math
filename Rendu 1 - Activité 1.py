import numpy as np
import matplotlib.pyplot as plt

#Activité 1
def cout_global(cout_fixe, cout_unitaire, nb_produits):
    return cout_fixe + cout_unitaire * nb_produits

#Paramètres de base
cout_fixe_base = 1000
cout_unitaire_base = 50
nb_produits_max = 100

#1 Variation du coût fixe
cout_fixes = [500, 1000, 1500]
for cf in cout_fixes:
    nb_produits = np.arange(0, nb_produits_max + 1)
    couts = cout_global(cf, cout_unitaire_base, nb_produits)
    plt.plot(nb_produits, couts, label=f'Coût fixe = {cf}')

plt.title("Variation du coût fixe")
plt.xlabel("Nombre de produits")
plt.ylabel("Coût global")
plt.legend()
plt.grid(True)
plt.show()

#2 Variation du coût unitaire
cout_unitaires = [30, 50, 70]
for cu in cout_unitaires:
    nb_produits = np.arange(0, nb_produits_max + 1)
    couts = cout_global(cout_fixe_base, cu, nb_produits)
    plt.plot(nb_produits, couts, label=f'Coût unitaire = {cu}')

plt.title("Variation du coût unitaire")
plt.xlabel("Nombre de produits")
plt.ylabel("Coût global")
plt.legend()
plt.grid(True)
plt.show()

#3 Variation du nombre de produits
nb_produits_max_list = [50, 100, 150]
for npm in nb_produits_max_list:
    nb_produits = np.arange(0, npm + 1)
    couts = cout_global(cout_fixe_base, cout_unitaire_base, nb_produits)
    plt.plot(nb_produits, couts, label=f'Nb produits max = {npm}')

plt.title("Variation du nombre de produits")
plt.xlabel("Nombre de produits")
plt.ylabel("Coût global")
plt.legend()
plt.grid(True)
plt.show()
