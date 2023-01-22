import subprocess
import Bibliotheque as b
d="b"
projectpath = f"C:\Program Files\gnuplot\{d}in\wgnuplot.exe" 
subprocess.check_call( ('start',projectpath) , shell=True )

def moyenne(x:list):
    contenu=0
    for i in x:
        contenu+=i
    return contenu/len(x)

def ecart_type(x):
    pass