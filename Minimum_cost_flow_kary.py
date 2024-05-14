import numpy as np
import random

def calculate_total_flow(node_index, przeplyw, start_nodes, end_nodes):
    inflow = sum(przeplyw[i] for i in range(len(przeplyw)) if end_nodes[i] == node_index)
    outflow = sum(przeplyw[i] for i in range(len(przeplyw)) if start_nodes[i] == node_index)
    return inflow - outflow

#Funkcja fitness
def koszt_przeplywu_z_zasobami(przeplyw, koszty, zasoby, start_nodes, end_nodes, supplies):
    koszt = 0
    penalties = 0
    for i in range(len(przeplyw)):
        if przeplyw[i] > zasoby[i]:
            penalties += (przeplyw[i] - zasoby[i]) * koszty[i] 
        koszt += przeplyw[i] * koszty[i]
    
    for node_index in range(len(supplies)):
        flow_balance = calculate_total_flow(node_index, przeplyw, start_nodes, end_nodes)
        if flow_balance != supplies[node_index]:
            penalties += abs(flow_balance - supplies[node_index])

    return koszt + penalties

#Generowanie osobnika
def generuj_osobnika(dlugosc_osobnika, zasoby):
    return [random.randint(0, zasoby[i]) for i in range(dlugosc_osobnika)]

#Generowanie mutacja
def mutacja(osobnik, prawdopodobienstwo_mutacji, zasoby):
    for i in range(len(osobnik)):
        if random.random() < prawdopodobienstwo_mutacji:
            osobnik[i] = random.randint(0, zasoby[i])
    return osobnik

def algorytm_ewolucyjny_z_zasobami(liczba_genow, liczba_osobnikow, liczba_iteracji, koszty, zasoby, start_nodes, end_nodes, supplies):
    najlepszy_osobnik = None
    najlepszy_koszt = float('inf')
    for _ in range(liczba_iteracji):
        populacja = [generuj_osobnika(liczba_genow, zasoby) for _ in range(liczba_osobnikow)]
        for osobnik in populacja:
            koszt = koszt_przeplywu_z_zasobami(osobnik, koszty, zasoby, start_nodes, end_nodes, supplies)
            if koszt < najlepszy_koszt:
                najlepszy_koszt = koszt
                najlepszy_osobnik = osobnik.copy()
        populacja = [mutacja(osobnik, 0.1, zasoby) for osobnik in populacja]
    
    return najlepszy_osobnik, najlepszy_koszt

# Dane
start_nodes = np.array([0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 0, 1, 2])
end_nodes = np.array([1, 2, 2, 3, 4, 3, 4, 4, 2, 0, 1, 2, 5, 3, 4])
capacities = np.array([15, 8, 20, 4, 10, 15, 4, 20, 5, 15, 10, 8, 100, 100, 100])
unit_costs = np.array([4, 4, 2, 2, 6, 1, 3, 2, 3, 4, 4, 2, 0, 0, 0]) 
supplies = np.array([20, 0, 0, -5, -15, 0])
liczba_genow = len(unit_costs) 
liczba_osobnikow = 100
liczba_iteracji = 1000
najlepszy_osobnik, najlepszy_koszt = algorytm_ewolucyjny_z_zasobami(liczba_genow, liczba_osobnikow, liczba_iteracji, unit_costs, capacities, start_nodes, end_nodes, supplies)

print("Minimum cost:", najlepszy_koszt)
print("Flow:")
for i in range(len(start_nodes)):
    flow = najlepszy_osobnik[i]
    capacity = capacities[i]
    cost = flow * unit_costs[i]
    print(f"From node {start_nodes[i]} to node {end_nodes[i]}: flow {flow} / capacity {capacity}  Cost: {cost}")