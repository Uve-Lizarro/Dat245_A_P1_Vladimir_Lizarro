import csv
import requests
from io import StringIO
import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
#Vladimir Ariel Lizarro Velásquez
#CI 13348515
url='https://raw.githubusercontent.com/Uve-Lizarro/Datasets/main/Student_Performance_Factors.csv'
respuesta=requests.get(url)
dataset=StringIO(respuesta.text)
datos=[]
def percentilCuartil():
    with dataset as file:
        lector=csv.reader(file)
        next(lector)
        for i in lector:
            datos.append(i)
    nroColumnas=len(datos[0])
    for i in range(nroColumnas):
        columna=[float(fila[i]) for fila in datos]
        columna.sort()
        for j, fila in enumerate(datos):
            fila[i]=columna[j]
    cuartil25=[]
    cuartil50=[]
    cuartil75=[]
    percentil90=[]
    for i in range(nroColumnas):
        columna=[float(row[i]) for row in datos]
        nroDatos=len(columna)
        q1=int(0.25*nroDatos)
        q2=int(0.50*nroDatos)
        q3=int(0.75*nroDatos)
        q4=int(0.90*nroDatos)
        cuartil25.append(columna[q1])
        cuartil50.append(columna[q2])
        cuartil75.append(columna[q3])
        percentil90.append(columna[q4])
    for i in range(nroColumnas):
        print(f"Columna {i+1}:")
        print(f"1er Cuartil (Percentil 25): {cuartil25[i]}")
        print(f"2do Cuartil (Mediana): {cuartil50[i]}")
        print(f"3er Cuartil (Percentil 75): {cuartil75[i]}")
        print(f"Percentil 90: {percentil90[i]}")
        print("")

def graficasDistribuciones():
    with dataset as file:
        lector=csv.reader(file)
        cabeceras = next(lector)
        for i in lector:
            datos.append(i)
    columnaHrsEst=[int(fila[0]) for fila in datos]
    columnaHrsSpleep=[int(fila[5]) for fila in datos]
    columnaAccessWifi=[int(fila[8]) for fila in datos]

    plt.figure(figsize=(10, 6))
    plt.hist(columnaHrsEst, bins=20, density=True, alpha=0.6, color='black')
    media, desEst=norm.fit(columnaHrsEst)
    xmin, xmax=plt.xlim()
    x=np.linspace(xmin, xmax, 100)
    p=norm.pdf(x, media, desEst)
    plt.plot(x, p, 'k', linewidth=2)
    plt.title(f'Distribución de Horas Estudiadas\nMedia = {media:.2f}, Desviación Estándar = {desEst:.2f}')
    plt.xlabel('Horas Estudiadas')
    plt.ylabel('Probabilidad')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.hist(columnaHrsSpleep, bins=20, density=True, alpha=0.6, color='blue')
    media, desEst=norm.fit(columnaHrsSpleep)
    xmin, xmax = plt.xlim()
    x=np.linspace(xmin, xmax, 100)
    p=norm.pdf(x, media, desEst)
    plt.plot(x, p, 'k', linewidth=2)
    plt.title(f'Distribución de Horas de Sueño\nMedia = {media:.2f}, Desviación Estándar = {desEst:.2f}')
    plt.xlabel('Horas de Sueño')
    plt.ylabel('Densidad de probabilidad')
    plt.show()
    
    p=np.mean(columnaAccessWifi)
    plt.figure(figsize=(6, 4))
    valores = [0, 1]
    probabilidades = [1 - p, p]
    plt.bar(valores, probabilidades, color=['red', 'green'], alpha=0.6)
    plt.xticks(valores, ['Sin Internet', 'Con Internet'])
    plt.title(f'Distribución de Acceso a Internet\nProbabilidad de Acceso = {p:.2f}')
    plt.xlabel('Acceso a Internet')
    plt.ylabel('Probabilidad')
    plt.show()

def proMedMo():
    datos=pd.read_csv(url)
    columnas=[14,17,19]
    for i in columnas:
        media=datos[datos.columns[i]].mean()
        mediana=datos[datos.columns[i]].median()
        moda=datos[datos.columns[i]].mode()
        if not moda.empty:
            aux=moda[0]
        else:
            aux='Sin moda'
        print(f"Columna: {i} {datos.columns[i]}")
        print(f"Media: {media}")
        print(f"Mediana: {mediana}")
        print(f"Moda: {moda}")
        print()
        plt.figure(figsize=(6, 4))
        plt.boxplot(datos[datos.columns[i]], vert=False)
        plt.title(f'Diagrama de Boxplot de {datos.columns[i]}')
        plt.xlabel('Valores')
        plt.grid(axis='x')
        plt.show()

if __name__ == '__main__':
    proMedMo()