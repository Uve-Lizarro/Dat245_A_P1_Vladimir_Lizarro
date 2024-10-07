import numpy as np
import pandas as pd
#Vladimir Ariel Lizarro Velásquez
#CI 13348515
url='https://raw.githubusercontent.com/Uve-Lizarro/Datasets/main/Student_Performance_Factors.csv'
datos=pd.read_csv(url)
columnas=datos.select_dtypes(include=[np.number]).columns
for i in columnas:
    min=datos[i].min()
    may=datos[i].max()
    datos[i]=(datos[i]-min)/(may-min)

def penalizacion_L1(coeficiente, alpha):
    return alpha*sum(abs(i) for i in coeficiente)

def penalizacion_L2(coeficiente, alpha):
    return alpha*sum(i**2 for i  in coeficiente)

class RegresionLinealSimple:
    def __init__(self, penalty='l2', alpha=0.1):
        self.penalizacion=penalty
        self.alpha=alpha
        self.coeficiente=None
    def entrenamiento(self, X, y):
        ind=[[1]+list(x) for x in X]
        self.coeficiente=[0.0]*len(ind[0])
        tazaAprendizaje=0.01
        generaciones=500
        for _ in range(generaciones):
            pre=[self.prediccion(x) for x in ind]
            error=[y[i]-pre[i] for i in range(len(y))]
            for j in range(len(self.coeficiente)):
                gradiente=-sum(error[i]*ind[i][j] for i in range(len(ind)))/len(y)
                if (self.penalizacion=='l1'):
                    self.coeficiente[j]-=tazaAprendizaje*(gradiente+penalizacion_L1(self.coeficiente, self.alpha))
                elif (self.penalizacion=='l2'):
                    self.coeficiente[j]-=tazaAprendizaje*(gradiente+penalizacion_L2(self.coeficiente, self.alpha))
                else:
                    self.coeficiente[j]-=tazaAprendizaje*gradiente
    def prediccion(self, x):
        return sum(i*j for i, j in zip(self.coeficiente, [1]+x))

if __name__ == '__main__':
    X=datos[['Hours_Studied', 'Sleep_Hours', 'Internet_Access']].values
    y=datos['Exam_Score'].values 
    modelo=RegresionLinealSimple(penalty='l2', alpha=0.1)
    modelo.entrenamiento(X, y)
    pre=[modelo.prediccion(x) for x in X]
    print("Coeficientes del modelo:", modelo.coeficiente)
    print("Predicciones:", pre[:5])
