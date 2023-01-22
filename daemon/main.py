import subprocess
import Bibliotheque as b
from math import sqrt
d="b"
projectpath = f"C:\Program Files\gnuplot\{d}in\wgnuplot.exe" 
subprocess.check_call( ('start',projectpath) , shell=True )

def moyenne(x:list):
    contenu=0
    for i in x:
        contenu+=i
    return contenu/len(x)

def variance(data, ddof=0):
    moyenn = moyenne(data)
    return sqrt(sum((x - moyenn) ** 2 for x in data) / (len(data)- ddof))
print(variance([10,0,10,10,0,0]))