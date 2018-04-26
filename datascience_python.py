# -*- coding: utf-8 -*-
"""
Aula Neylson 25/04
Data Science com Pandas
Larissa Fernandes 
"""

import pandas as pd

pnad = pd.read_csv("https://raw.githubusercontent.com/neylsoncrepalde/introducao_ao_python/master/pes_2012.csv")

pnad.shape
pnad.columns

pnad.head()

pnad['V8005'].dtype
pnad["V0302"]
pnad["V4720"]


#ESTUDANDO A IDADE
pnad["V8005"].describe() # VER AS ESTATÍSTICAS DESCRITIVAS
#para areddondar os números colocar : .round() 
pnad["V8005"].describe().round(decimals = 2)
pnad["V8005"].mean()
pnad["V8005"].var()

pnad.describe()

#VARIAVEIS CATEGORICAS
pnad.head()
pnad["V0302"]
pnad["V0302"].value_counts() #contagem para cada categoria (sexo)

tab_sexo = pd.crosstab(index = pnad["V0302"], columns = ["contagem"])

print("Distribuição da frequencia - Sexo" + "\n")
print(tab_sexo)

(tab_sexo / tab_sexo.sum()) * 100

####################################################
#estudando Variavel cor raça
pnad["V0404"].value_counts()
tab_cor = pnad["V0404"].value_counts()

print("Distribuição de Frequencia - Cor" + "\n")
print(tab_cor)

print("Porcentagens - Cor" + "\n")
print( (tab_cor / tab_cor.sum() )*100)


#### CRUZAR VARIAVEIS - sexo x cor
sexo_cor = pd.crosstab(index = pnad["V0404"],
                       columns = pnad["V0302"])

print(sexo_cor)

### ESTUDANDO A RENDA
pnad.columns
renda = pnad["V4720"]
renda = list(renda)
type(renda)
renda









