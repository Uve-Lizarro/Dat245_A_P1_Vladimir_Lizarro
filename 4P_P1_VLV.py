import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
#Vladimir Ariel Lizarro Velásquez
#CI 13348515
url='https://raw.githubusercontent.com/Uve-Lizarro/Datasets/main/Student_Performance_Factors.csv'
datos=pd.read_csv(url)
def Etiqueta_OnehotEncoder():
    datosNominalBinario=pd.get_dummies(datos, drop_first=True)
    print(datosNominalBinario)

def Etiqueta_LabelEncoder():
    datosStringNum=datos.copy()
    le=LabelEncoder()
    for i in datosStringNum.select_dtypes(include=['object']).columns:
        datosStringNum[i]=le.fit_transform(datosStringNum[i])
    print(datosStringNum)

def Etiqueta_Discretize():
    datosDiscre=datos.copy()
    limites=[0, 5, 10, 15, 20]
    etiquetas=['0-5', '5-10', '10-15', '15-20']
    columna='Hours_Studied'
    datosDiscre[columna] = pd.cut(datosDiscre[columna], bins=limites, labels=etiquetas, include_lowest=True)
    print(datosDiscre)

def Etiqueta_Normalize():
    datosNorm=datos.copy()
    columnas=datosNorm.select_dtypes(include=[np.number]).columns
    for i in columnas:
        min=datosNorm[i].min()
        may=datosNorm[i].max()
        datosNorm[i]=(datosNorm[i]-min)/(may-min)
    print(datosNorm)

if __name__ == '__main__':
    Etiqueta_Discretize()