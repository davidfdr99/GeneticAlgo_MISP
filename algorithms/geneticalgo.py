from random import choices, randint, randrange, random
from typing import List, Callable, Tuple

Genome = List[int]
Population = List[Genome]
FitnessFunc = Callable[[Genome], int]
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]

def generate_genome(length: int) -> Genome:
    return choices([0, 1], k=length)

def generate_population(size: int, genome_length: int) -> Population:
    return [generate_genome(genome_length) for _ in range(size)]

def roulette_wheel_selection(population: Population, fitness_func: FitnessFunc) -> Population:
    return choices(
            population=population,
            weights=[fitness_func(genome) for genome in population],
            k=2
    )

def by_rank(population: Population, fitness_func: FitnessFunc) -> Population:
    population = sorted(
        population,
        key=lambda genome: fitness_func(genome),
        reverse=True
    )

    return population[:2]

def tournament(population: Population, fitness_func: FitnessFunc) -> Population:
    t1 = sorted(choices(population, k=2), key=lambda genome: fitness_func(genome))
    p1 = t1.pop()

    t2 = sorted(choices(population, k=2), key=lambda genome: fitness_func(genome))
    p2 = t2.pop()

    return [p1, p2]


def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("a and b must be of same lengths!")

    length = len(a)
    if length < 2:
        return a, b

    p = randint(1, length - 1)
    return a[0:p] + b[p:], b[0:p] + a[p:]

def mutation(genome: Genome, num: int = 1, probability: int = 0.5) -> Genome:
    for _ in range(num):
        index = randrange(len(genome))
        genome[index] = genome[index] if random() > probability else abs(genome[index] - 1)
    return genome


def run_evolution(
        populate_func=Population,
        fitness_func=FitnessFunc,
        fitness_limit=int,
        selection_func: SelectionFunc = roulette_wheel_selection,
        mutation_func: MutationFunc = mutation,
        generation_limit: int = 100,
        elitism = False,
) -> Tuple[Population, int]:
    population = populate_func()

    counter = 0

    for i in range(generation_limit):


        if fitness_limit is not None:
            if fitness_func(population[0]) >= fitness_limit:
                break

        if elitism == True:

            population = sorted(
                population,
                key=lambda genome: fitness_func(genome),
                reverse=True
            )

            next_generation = population[0:2]

            for j in range(int(len(population) / 2) - 1):
                parents = selection_func(population, fitness_func)
                offspring_a, offspring_b = single_point_crossover(parents[0], parents[1])
                offspring_a = mutation_func(offspring_a)
                offspring_b = mutation_func(offspring_b)
                next_generation += [offspring_a, offspring_b]

        elif not elitism:

            next_generation = []

            for j in range(int(len(population) / 2)):
                parents = selection_func(population, fitness_func)
                offspring_a, offspring_b = single_point_crossover(parents[0], parents[1])
                offspring_a = mutation_func(offspring_a)
                offspring_b = mutation_func(offspring_b)
                next_generation += [offspring_a, offspring_b]

        population = next_generation

        counter += 1

    population = sorted(
        population,
        key=lambda genome: fitness_func(genome),
        reverse=True
    )

    return population, counter

