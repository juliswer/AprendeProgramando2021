import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files
import io
filesUploaded = files.upload()
trees = pd.read_csv(io.BytesIO(filesUploaded["arbolado-publico-lineal-2017-2018.csv"]))
trees
trees.describe()
print("Arboles de menor altura")
print(trees.loc[trees["altura_arbol"] == trees["altura_arbol"].min(),"nombre_cientifico"].drop_duplicates())
print("\nArboles de mayor altura")
print(trees.loc[trees["altura_arbol"] == trees["altura_arbol"].max(),"nombre_cientifico"].drop_duplicates())
trees["nombre_cientifico"].value_counts()
species = trees["nombre_cientifico"].value_counts()
sns.barplot(
    x = species, # El parámetro x representa lo que queremos gráficar en este eje, la cantidad de repeticiones de la especie 
    y = species.index  # El parámetro y representa lo que queremos gráficar en este eje, cada una de las especies. 
)
sns.barplot(
    x = species[:10],  
    y = species.index[:10]
)
(species >= 50).sum()
commonSpecies = trees.loc[(trees["nombre_cientifico"].isin(species.index[species > 50])) & (trees["nombre_cientifico"] != "No identificado")]
commonSpecies.shape
commonSpecies["comuna"] = commonSpecies["comuna"].astype("category")
sns.barplot(
    x = "nombre_cientifico", y = "comuna",
    data = commonSpecies[["comuna", "nombre_cientifico"]].groupby("comuna").nunique().reset_index(drop = False)
)
heightDiameter = commonSpecies[["nombre_cientifico", "diametro_altura_pecho", "altura_arbol"]].groupby("nombre_cientifico").mean()
heightDiameter.reset_index(drop = False, inplace = True)
plot = sns.lmplot(
    data = heightDiameter, x = "diametro_altura_pecho", y = "altura_arbol", hue = "nombre_cientifico" 
)
plot._legend.remove()
plt.annotate(heightDiameter.nombre_cientifico[48], xy=(heightDiameter.diametro_altura_pecho[48]+0.2, heightDiameter.altura_arbol[48]), xytext=(heightDiameter.diametro_altura_pecho[48]+0.3, heightDiameter.altura_arbol[48]))
plt.annotate(heightDiameter.nombre_cientifico[97], xy=(heightDiameter.diametro_altura_pecho[97]+0.2, heightDiameter.altura_arbol[97]), xytext=(heightDiameter.diametro_altura_pecho[97]+0.3, heightDiameter.altura_arbol[97]))
sns.barplot(
    data = trees[["comuna", "nro_registro"]].groupby("comuna").count().reset_index(drop = False),
    x = "comuna", y = "nro_registro"
)