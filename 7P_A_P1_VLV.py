import numpy as np
import random
from deap import algorithms, base, creator, tools
#Vladimir Ariel Lizarro Velásquez
#CI 13348515
NB_DISTANCE=10
def funcion(individual):
    x=individual[0]
    return x**(2*x)-1,

def estadisticas(ind):
        return ind.fitness.values

def algGenDEAP():
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)
    toolbox=base.Toolbox()
    toolbox.register("attr_int", random.randint, 1, 16)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, NB_DISTANCE)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", funcion)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutUniformInt, low=1, up=16, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)
    random.seed(0)
    poblacion=toolbox.population(300)
    solOpt=tools.HallOfFame(1)
    datosEst=tools.Statistics(key=estadisticas)
    datosEst.register("Media", np.mean)
    datosEst.register("Desviación estándar", np.std)
    datosEst.register("Valor mínimo", np.min)
    datosEst.register("Valor máximo", np.max)
    algorithms.eaSimple(poblacion, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=datosEst, halloffame=solOpt, verbose=True)
    print(f'Mejor solución{solOpt}')

if __name__ == "__main__":
    algGenDEAP()