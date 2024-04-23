import random
population_size = 100
gnome_length = 20
mutation_rate = 0.01
crosoover_rate = 0.7
generations= 200

def random_genome(length):
    return[random.randint(0, 1) for _ in range{length}]

def init_population(population_size, genome_length):
    return [random_genome(genome_length) for _ in range(population_size)]

def fitness(genome):
    return sum(genome)



def select_parent(population, fitness):
    total_fitness = sum(fitness)
    pick = random.uniform( 0, total_fitness)
    current = 0
    for individudal, fitness in zip(population, fitness):
        courrent += fitness
        if courrent > pick:
            return individudal
        
    
    
def crossover(parent1, parent2):
    if random.randint() < mutation_rate:
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
    population = init_population(population_size,genome_length)
    for generatrion in range(generations):
        fitness = [fitness(genome) for genome in population]
        
        new_population = []
        for _ in range(population_size // 2):
            parent1 = select_parent(population, fitness)
            parent2 = select_parent(population, fitness)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.extend([mutation(offspring1), mutation(offspring2)])
            
        population = new_population
        fitness = [fitness(genome) for genome in population]
        best_fitness = max(fitness)
        print(f"generation {generatrion} best {best_fitness}")
    best_index = fitness.index(max(fitness))
    best_solution = population[best_index]
    print(f"Best sol: {best_solution}")
    print(f"Best fintes: {fitness(best_solution)}")
    
if __name__ =='__main__':
    genetic_algorytm()
