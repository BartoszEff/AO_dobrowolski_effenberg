import numpy as np
import random

# Fitness
def calculate_makespan(schedule, processing_times):
    num_jobs = len(schedule)
    num_machines = len(processing_times)
    job_end_times = np.zeros(num_jobs)
    machine_end_times = np.zeros(num_machines)

    for job in schedule:
        job_start_time = np.max([job_end_times[job], machine_end_times[0]])
        for machine in range(num_machines):
            start_time = max(job_start_time, machine_end_times[machine])
            end_time = start_time + processing_times[machine][job]
            machine_end_times[machine] = end_time
            job_start_time = end_time
        job_end_times[job] = job_start_time

    return max(machine_end_times)

# Generowanie osobnika
def generate_individual(num_jobs):
    individual = list(range(num_jobs))
    random.shuffle(individual)
    return individual

# Mutacja
def mutate_individual(individual, mutation_rate=0.05):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            swap = random.randint(0, len(individual) - 1)
            individual[i], individual[swap] = individual[swap], individual[i]
    return individual

# Krzyżowanie
def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted([random.randint(0, size), random.randint(0, size)])
    child = [-1] * size
    child[start:end] = parent1[start:end]

    p2 = 0
    for i in range(size):
        if child[i] == -1:
            while parent2[p2] in child:
                p2 += 1
            child[i] = parent2[p2]

    return child

# Selekcja turniejowa
def tournament_selection(population, processing_times, k=3):
    selected = random.sample(population, k)
    selected.sort(key=lambda ind: calculate_makespan(ind, processing_times))
    return selected[0]

# Algorytm lokalnego przeszukiwania
def local_search(individual, processing_times):
    best_individual = individual.copy()
    best_makespan = calculate_makespan(individual, processing_times)
    
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            new_individual = individual.copy()
            new_individual[i], new_individual[j] = new_individual[j], new_individual[i]
            new_makespan = calculate_makespan(new_individual, processing_times)
            
            if new_makespan < best_makespan:
                best_individual = new_individual.copy()
                best_makespan = new_makespan
    
    return best_individual

def evolutionary_algorithm(processing_times, num_generations, population_size, mutation_rate):

    population = [generate_individual(num_jobs) for _ in range(population_size)]
    best_individual = None
    best_makespan = float('inf')

    for generation in range(num_generations):
        fitness_values = [calculate_makespan(individual, processing_times) for individual in population]
        
        for i in range(len(population)):
            if fitness_values[i] < best_makespan:
                best_makespan = fitness_values[i]
                best_individual = population[i].copy()

        new_population = [best_individual.copy()]  # Elitism
        while len(new_population) < population_size:
            parent1 = tournament_selection(population, processing_times)
            parent2 = tournament_selection(population, processing_times)
            child = crossover(parent1, parent2)
            child = mutate_individual(child, mutation_rate)
            child = local_search(child, processing_times)
            new_population.append(child)

        population = new_population

    return best_individual, best_makespan

# Dane
processing_times = np.array([
    [54, 83, 15, 71, 77, 36, 53, 38, 27, 87, 76, 91, 14, 29, 12, 77, 32, 87, 68, 94],
    [79, 3, 11, 99, 56, 70, 99, 60, 5, 56, 3, 61, 73, 75, 47, 14, 21, 86, 5, 77],
    [16, 89, 49, 15, 89, 45, 60, 23, 57, 64, 7, 1, 63, 41, 63, 47, 26, 75, 77, 40],
    [66, 58, 31, 68, 78, 91, 13, 59, 49, 85, 85, 9, 39, 41, 56, 40, 54, 77, 51, 31],
    [58, 56, 20, 85, 53, 35, 53, 41, 69, 13, 86, 72, 8, 49, 47, 87, 58, 18, 68, 28]
])
num_jobs = 20
num_machines = 5
num_generations = 100
population_size = 100
mutation_rate = 0.05

best_schedule, best_makespan = evolutionary_algorithm(processing_times, num_generations, population_size, mutation_rate)
print("Najlepszy makespan:", best_makespan)
print("Najlepszy harmonogram:", best_schedule)
