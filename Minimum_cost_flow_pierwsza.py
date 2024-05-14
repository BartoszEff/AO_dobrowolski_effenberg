import numpy as np
import random

# Fitness
def koszt_przeplywu_z_zasobami(przeplyw, koszty, zasoby):
    koszt = 0
    for i in range(len(przeplyw)):
        if przeplyw[i] > zasoby[i]:  
            koszt += (przeplyw[i] - zasoby[i]) * koszty[i]  
    return koszt

#Generacja losowego osobnika
def generuj_osobnika(dlugosc_osobnika, zasoby):
    return [random.randint(0, zasoby[i]) for i in range(dlugosc_osobnika)]

# Mutacja
def mutacja(osobnik, prawdopodobienstwo_mutacji, zasoby):
    for i in range(len(osobnik)):
        if random.random() < prawdopodobienstwo_mutacji:
            osobnik[i] = random.randint(0, zasoby[i])
    return osobnik


def algorytm_ewolucyjny_z_zasobami(liczba_genow, liczba_osobnikow, liczba_iteracji, koszty, capacities, zasoby):
    najlepszy_osobnik = None
    najlepszy_koszt = float('inf')
    for _ in range(liczba_iteracji):
        populacja = [generuj_osobnika(liczba_genow, capacities) for _ in range(liczba_osobnikow)]
        for osobnik in populacja:
            koszt = koszt_przeplywu_z_zasobami(osobnik, koszty, zasoby)
            if koszt < najlepszy_koszt:
                najlepszy_koszt = koszt
                najlepszy_osobnik = osobnik
                populacja = [mutacja(osobnik, 0.1, capacities) for osobnik in populacja]
    
    return najlepszy_osobnik, najlepszy_koszt


# Dane wejściowe
start_nodes = np.array([0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 0, 1, 2])
end_nodes = np.array([1, 2, 2, 3, 4, 3, 4, 4, 2, 0, 1, 2, 5, 3, 4])
capacities = np.array([15, 8, 20, 4, 10, 15, 4, 20, 5, 15, 10, 8, 100, 100, 100])
unit_costs = np.array([4, 4, 2, 2, 6, 1, 3, 2, 3, 4, 4, 2, 0, 0, 0]) 
supplies = [20, 0, 0, -5, -15, 0]
if len(supplies) < len(unit_costs):
    while len(supplies) < len(unit_costs):
        supplies.append(0)

liczba_genow = len(unit_costs)
liczba_osobnikow = 100
liczba_iteracji = 1000
najlepszy_osobnik, najlepszy_koszt = algorytm_ewolucyjny_z_zasobami(liczba_genow, liczba_osobnikow, liczba_iteracji, unit_costs, capacities, supplies)

print("Minimum cost:", najlepszy_koszt)
print("Flow:")
for i in range(len(start_nodes)):
    flow = najlepszy_osobnik[i]
    capacity = capacities[i]
    cost = flow * unit_costs[i]
    print(f"From node {start_nodes[i]} to node {end_nodes[i]}: flow {flow} / capacity {capacity}  Cost: {cost}")

