'''
Created on 22 nov. 2017

@author: gabri
'''
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages 
from asservissement import ALT_MAX
import math
import numpy as np


resultasCalcul = []

def makeCalculus(X,Y):
    
    
    def erreurStatique():
        MAX = max(Y)
        MIN = min(Y)
        if (math.fabs(ALT_MAX-MIN)/ALT_MAX) >= (math.fabs(ALT_MAX-MAX)/ALT_MAX):
            resultasCalcul.append(("Erreur Statique",math.fabs(ALT_MAX-MIN)/ALT_MAX))
        resultasCalcul.append(("Erreur Statique",math.fabs(ALT_MAX-MAX)/ALT_MAX))
        
    def PolynomialFitting(X,Y):
        L = np.polyfit(X, Y, DEG)
        n = len(L)
        resultasCalcul.append(("équation du polynôme",[L[i] for i in range(n)]))
        plt.plot(X,[sum(L[i]*X**(n-i)) for i in range(n)])  #tracé du polynome de la courbe
        
    erreurStatique()
    PolynomialFitting(X, Y)
        
           
   

def scrapper():    # scrap les données du .DAT et les met sous forme (altitude, temps) (les valeurs sont des strings...)
    
    TIME,ALT =[],[]
    tampTIME,tampALT = [],[]
    i = 0
    file = open('data.dat','r')
    A = file.read()
    
    while i <= len(A)-1:
        if A[i] != '\t' and A[i-1] != '\t':
            tampALT += A[i]
            i+=1
            
        if A[i] == '\t':
            ALT.append(''.join(map(str,tampALT)))
            tampALT = []
            i += 1
            
        if A[i-1] == '\t':
            while A[i] != '\n':
                if i == len(A)-1:
                    TIME.append(''.join(map(str,tampTIME)))
                    elt = A[i]
                    C = TIME[len(TIME)-1]
                    C += elt
                    TIME.remove(TIME[len(TIME)-1])
                    TIME.append(C)
                    return ALT,TIME
                tampTIME += A[i]
                i+=1
            
            TIME.append(''.join(map(str,tampTIME)))
            tampTIME = []
            i += 1
            
   
                
plt.ion()
fig = plt.figure()           #Création du graph
plt.title("Altitude du ballon en fonction du temps", fontsize=20)
plt.xlabel("Temps (en s)",fontsize=20)
plt.ylabel("Altitude (en m)",fontsize=20)
plt.grid(True)
DEG = 10 #degré du polynome voir plus haut dans la fonction de lissage...)


Y,X = scrapper()
for i in range(len(X)):
    plt.scatter(float(X[i]),float(Y[i])) #tracé du nuage de point
    
plt.plot(X,[ALT_MAX]*len(X),'r--')  # tracé de la consigne ( en rouge pointillé)
makeCalculus(X, Y)

pdf = PdfPages('results.pdf') #sauvegarde du graph
pdf.savefig(fig)
pdf.close()
print(resultasCalcul)



    

    
    
