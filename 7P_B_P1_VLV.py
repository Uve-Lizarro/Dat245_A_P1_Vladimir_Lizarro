import numpy as np
import random
#Vladimir Ariel Lizarro Velásquez
#CI 13348515
NB_DISTANCE=10
def funcion(individual):
    x=individual[0]
    return x**(2*x)-1

def iniciarPoblacion(n, tam):
    return [[random.randint(1, 16) for _ in range(tam)] for _ in range(n)]

def evaluarPoblacion(poblacion):
    return [funcion(i) for i in poblacion]

def seleccion(poblacion, fitness, k=3):
    mejorResultado=[]
    for _ in range(len(poblacion)):
        aux=random.sample(range(len(poblacion)), k)
        mejor=min(aux, key=lambda i: fitness[i])
        mejorResultado.append(poblacion[mejor])
    return mejorResultado

def cruce(x, y):
    x1=x[:]
    y1=y[:]
    if (len(x)>1):
        p1=random.randint(1, len(x)-1)
        p2=random.randint(p1, len(x)-1)
        x1[p1:p2]=y[p1:p2]
        y1[p1:p2]=x[p1:p2]
    return x1, y1

def mutacion(individuo, probMutar):
    for i in range(len(individuo)):
        if (random.random()<probMutar):
            individuo[i]=random.randint(1, 16)
    return individuo

def algGen():
    generaciones=100
    inciCruce=0.5
    inciMutacion=0.2
    poblacion=iniciarPoblacion(300, NB_DISTANCE)
    solOpt=0
    mejorFitness=float('inf')
    print(f'Generacion Media Desviación estándar Valor mínimo Valor máximo')
    for i in range(generaciones):
        fitness=evaluarPoblacion(poblacion)
        for j, k in zip(poblacion, fitness):
            if (k<mejorFitness):
                mejorFitness=k
                solOpt=j
        print(f"{i} {np.mean(fitness)} {np.std(fitness)} {np.min(fitness)} {np.max(fitness)}")
        mejoresSol=seleccion(poblacion, fitness)
        cruces=[]
        for j in range(0, len(mejoresSol), 2):
            if (j+1<len(mejoresSol) and random.random()<inciCruce):
                x, y=cruce(mejoresSol[i], mejoresSol[i+1])
                cruces.append(x)
                cruces.append(y)
            else:
                cruces.append(mejoresSol[i])
                if (j+1<len(mejoresSol)):
                    cruces.append(mejoresSol[i+1])
        poblacion=[mutacion(i, inciMutacion) for i in cruces]
    print(f"Mejor solución: {solOpt}")

if __name__ == "__main__":
    algGen()