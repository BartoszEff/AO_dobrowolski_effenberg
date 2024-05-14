import numpy as np
import random

# Funkcja celu - koszt przepływu
def koszt_przeplywu(przeplyw, koszty):
    return sum(przeplyw[i] * koszty[i] for i in range(len(przeplyw)))

# Generacja losowego osobnika
def generuj_osobnika(dlugosc_osobnika, maksymalna_wartosc):
    return [random.randint(0, maksymalna_wartosc) for _ in range(dlugosc_osobnika)]

# Mutacja - zamiana losowego genu
def mutacja(osobnik, prawdopodobienstwo_mutacji, maksymalna_wartosc):
    for i in range(len(osobnik)):
        if random.random() < prawdopodobienstwo_mutacji:
            osobnik[i] = random.randint(0, maksymalna_wartosc)
    return osobnik
# Krzyżowanie - losowe punkty
def krzyzowanie(rodzic1, rodzic2):
    punkty_krzyzowania = sorted(random.sample(range(len(rodzic1)), random.randint(1, len(rodzic1) - 1)))
    dziecko1 = []
    dziecko2 = []
    rodzic1_ptr = 0
    rodzic2_ptr = 0
    for punkt in punkty_krzyzowania:
        dziecko1.extend(rodzic1[rodzic1_ptr:punkt])
        dziecko2.extend(rodzic2[rodzic2_ptr:punkt])
        dziecko1_ptr, dziecko2_ptr = punkt, punkt
        rodzic1_ptr = punkt if rodzic1_ptr == 0 else 0
        rodzic2_ptr = punkt if rodzic2_ptr == 0 else 0
    dziecko1.extend(rodzic1[rodzic1_ptr:])
    dziecko2.extend(rodzic2[rodzic2_ptr:])
    return dziecko1, dziecko2


# Algorytm ewolucyjny
def algorytm_ewolucyjny(liczba_genow, liczba_osobnikow, liczba_iteracji, koszty, maksymalna_wartosc):
    najlepszy_osobnik = None
    najlepszy_koszt = float('inf')
    
    for _ in range(liczba_iteracji):
        # Generowanie populacji początkowej
        populacja = [generuj_osobnika(liczba_genow, maksymalna_wartosc) for _ in range(liczba_osobnikow)]
        
        for osobnik in populacja:
            # Ocena osobnika
            koszt = koszt_przeplywu(osobnik, koszty)
            # Aktualizacja najlepszego osobnika
            if koszt < najlepszy_koszt:
                najlepszy_koszt = koszt
                najlepszy_osobnik = osobnik
        
        # Selekcja najlepszych osobników
        populacja.sort(key=lambda x: koszt_przeplywu(x, koszty))
        najlepsi_osobnicy = populacja[:liczba_osobnikow // 2]
        
        # Krzyżowanie
        nowa_populacja = []
        for i in range(0, len(najlepsi_osobnicy), 2):
            dziecko1, dziecko2 = krzyzowanie(najlepsi_osobnicy[i], najlepsi_osobnicy[i + 1])
            nowa_populacja.extend([dziecko1, dziecko2])
        
        # Mutacja
        nowa_populacja = [mutacja(osobnik, 0.1, maksymalna_wartosc) for osobnik in nowa_populacja]
        
        # Aktualizacja populacji
        populacja = najlepsi_osobnicy + nowa_populacja
    
    return najlepszy_osobnik, najlepszy_koszt

# Dane wejściowe
start_nodes = np.array([0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 0, 1, 2])
end_nodes = np.array([1, 2, 2, 3, 4, 3, 4, 4, 2, 0, 1, 2, 5, 3, 4])
capacities = np.array([15, 8, 20, 4, 10, 15, 4, 20, 5, 15, 10, 8, 100, 100, 100])
unit_costs = np.array([4, 4, 2, 2, 6, 1, 3, 2, 3, 4, 4, 2, 0, 0, 0]) 
supplies = [20, 0, 0, -5, -15, 0]
liczba_genow = len(unit_costs)
liczba_osobnikow = 100
liczba_iteracji = 1000
maksymalna_wartosc = max(capacities)  # Maksymalna możliwa wartość przepływu

# Wywołanie algorytmu ewolucyjnego
najlepszy_osobnik, najlepszy_koszt = algorytm_ewolucyjny(liczba_genow, liczba_osobnikow, liczba_iteracji, unit_costs, maksymalna_wartosc)
print("Najlepszy osobnik:", najlepszy_osobnik)
print("Koszt przepływu:", najlepszy_koszt)
