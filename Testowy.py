import numpy as np
import random

# Funkcja celu - koszt przepływu z uwzględnieniem zasobów
def koszt_przeplywu_z_zasobami(przeplyw, koszty, zasoby):
    koszt = sum(przeplyw[i] * koszty[i] for i in range(len(przeplyw)))
    for i in range(len(przeplyw)):
        if przeplyw[i] > zasoby[i]:  
            # Zamiast przypisywać inf, dodajemy koszt przekroczenia zasobów do kosztu całkowitego
            koszt += (przeplyw[i] - zasoby[i]) * koszty[i]  
    return koszt

# Generacja losowego osobnika
def generuj_osobnika(dlugosc_osobnika, maksymalna_wartosc):
    return [random.randint(0, maksymalna_wartosc) for _ in range(dlugosc_osobnika)]

# Mutacja - zmiana losowego genu
def mutacja(osobnik, prawdopodobienstwo_mutacji, maksymalna_wartosc):
    for i in range(len(osobnik)):
        if random.random() < prawdopodobienstwo_mutacji:
            osobnik[i] = random.randint(0, maksymalna_wartosc)
    return osobnik

# Algorytm ewolucyjny z uwzględnieniem zasobów
def algorytm_ewolucyjny_z_zasobami(liczba_genow, liczba_osobnikow, liczba_iteracji, koszty, maksymalna_wartosc, zasoby):
    najlepszy_osobnik = None
    najlepszy_koszt = float('inf')
    licznik_braku_poprawy = 0  # Licznik iteracji bez poprawy
    for _ in range(liczba_iteracji):
        populacja = [generuj_osobnika(liczba_genow, maksymalna_wartosc) for _ in range(liczba_osobnikow)]
        for osobnik in populacja:
            koszt = koszt_przeplywu_z_zasobami(osobnik, koszty, zasoby)
            if koszt < najlepszy_koszt:
                najlepszy_koszt = koszt
                najlepszy_osobnik = osobnik
                licznik_braku_poprawy = 0
            else:
                licznik_braku_poprawy += 1
        if licznik_braku_poprawy >= 100:  # Warunek stopu: brak poprawy przez 100 iteracji
            break
        populacja = [mutacja(osobnik, 0.1, maksymalna_wartosc) for osobnik in populacja]
    
    return najlepszy_osobnik, najlepszy_koszt


# Dane wejściowe
start_nodes = np.array([0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 0, 1, 2])
end_nodes = np.array([1, 2, 2, 3, 4, 3, 4, 4, 2, 0, 1, 2, 5, 3, 4])
capacities = np.array([15, 8, 20, 4, 10, 15, 4, 20, 5, 15, 10, 8, 100, 100, 100])
unit_costs = np.array([4, 4, 2, 2, 6, 1, 3, 2, 3, 4, 4, 2, 0, 0, 0]) 
supplies = [20, 0, 0, -5, -15, 0]
if len(supplies) < len(unit_costs):
    # Dopasowanie długości supplies poprzez dodanie brakujących wartości jako 0
    while len(supplies) < len(unit_costs):
        supplies.append(0)

liczba_genow = len(unit_costs)  # Liczba genów odpowiada liczbie krawędzi
liczba_osobnikow = 100
liczba_iteracji = 1000
maksymalna_wartosc = max(capacities)  # Maksymalna możliwa wartość przepływu

# Wywołanie algorytmu ewolucyjnego
najlepszy_osobnik, najlepszy_koszt = algorytm_ewolucyjny_z_zasobami(liczba_genow, liczba_osobnikow, liczba_iteracji, unit_costs, maksymalna_wartosc, supplies)

print("Koszt przepływu:", najlepszy_koszt)
for i in range(len(start_nodes)):
    flow = najlepszy_osobnik[i]
    capacity = capacities[i]
    cost = flow * unit_costs[i]
    print(f"From node {start_nodes[i]} to node {end_nodes[i]}: flow {flow} / capacity {capacity}  Cost: {cost}")

