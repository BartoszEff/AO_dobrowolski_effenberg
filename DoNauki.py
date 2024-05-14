import random


population_size = 100
gnome_length = 20
mutation_rate = 0.01
crosoover_rate = 0.7
generations= 200

def random_genome(length):
    return [random.randint(0, 1) for _ in range(length)]


def init_population(population_size, gnome_length):
    return [random_genome(gnome_length) for _ in range(population_size)]

def fitness(genome):
    return sum(genome)



def select_parent(population, fitness_values):
    total_fitness = sum(fitness_values)
    pick = random.uniform( 0, total_fitness)
    current = 0
    for individudal, fitness_values in zip(population, fitness_values):
        current += fitness_values
        if current > pick:
            return individudal
        
    
    
def crossover(parent1, parent2):
    if random.random() < crosoover_rate:
        crossoverpoint = random.randint(1,len(parent1) - 1)
        return parent1[:crossoverpoint] + parent2 [crossoverpoint:], parent2[:crossoverpoint] + parent1[crossoverpoint:]
    else:
        return parent1, parent2
    
    
def mutation(genome):
    for i in range(len(genome)):
        if random.random() < mutation_rate:
            genome[i] =abs(genome[i] - 1 )
        return genome
    
def genetic_algorytm():
    population = init_population(population_size,gnome_length)
    for generatrion in range(generations):
        fitness_values = [fitness(genome) for genome in population]
        
        new_population = []
        for _ in range(population_size // 2):
            parent1 = select_parent(population, fitness_values)
            parent2 = select_parent(population, fitness_values)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.extend([mutation(offspring1), mutation(offspring2)])
            
        population = new_population
        fitness_values = [fitness(genome) for genome in population]
        best_fitness = max(fitness_values)
        print(f"generation {generatrion} best {best_fitness}")
    best_index = fitness_values.index(max(fitness_values))
    best_solution = population[best_index]
    print(f"Best sol: {best_solution}")
    print(f"Best fintes: {fitness(best_solution)}")
    
if __name__ =='__main__':
    genetic_algorytm()
