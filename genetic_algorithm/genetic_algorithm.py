# genetic_algorithm.py

import numpy as np

class GeneticAlgorithm:
    def __init__(self, fitness_function, search_space, population_size=50, generations=100, crossover_rate=0.8, mutation_rate=0.1):
        self.fitness_function = fitness_function
        self.search_space = search_space
        self.population_size = population_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            individual = {}
            for param, param_range in self.search_space.items():
                individual[param] = np.random.uniform(param_range[0], param_range[1])
            population.append(individual)
        return population

    def crossover(self, parent1, parent2):
        child = {}
        for param in self.search_space.keys():
            if np.random.rand() < self.crossover_rate:
                child[param] = parent1[param]
            else:
                child[param] = parent2[param]
        return child

    def mutate(self, individual):
        for param, param_range in self.search_space.items():
            if np.random.rand() < self.mutation_rate:
                individual[param] = np.random.uniform(param_range[0], param_range[1])
        return individual

    def run(self):
        population = self.initialize_population()
        for _ in range(self.generations):
            # Calculate fitness for each individual
            fitness_scores = [self.fitness_function(individual) for individual in population]

            # Select parents for crossover (tournament selection)
            selected_indices = np.random.choice(len(population), size=self.population_size, replace=True)
            selected_population = [population[i] for i in selected_indices]

            new_population = []
            for _ in range(self.population_size // 2):
                parent1, parent2 = np.random.choice(selected_population, size=2, replace=False)
                child1 = self.crossover(parent1, parent2)
                child2 = self.crossover(parent2, parent1)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                new_population.extend([child1, child2])

            population = new_population

        # Return the best individual
        best_individual = max(population, key=self.fitness_function)
        return best_individual
