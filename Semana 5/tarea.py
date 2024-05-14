number = 0;

for num in range(1, 200):
  if(num % 2 == 0):
    number += num;

print(number)

import numpy as np
import pandas as pd

goOut = pd.DataFrame({
    "name": ["Mirtha", "Clara", "Joaquin", "Kiara"],
    "accept": [True, False, True, False],
    "movie": [False, True, True, np.nan],
    "home": [False, True, False, np.nan]
})

accept = sum(goOut.accept)
goOut = goOut.dropna()
movie = sum(goOut.movie)
coffe = accept - movie
home = sum(goOut.home)
inBar = accept - home
bar = False

if movie>=coffe:
  if inBar >=home and bar:
    print("We watch a movie on the cinema")
  else:
    print("We watch a movie at home")
else:
  if inBar >=home and bar:
    print("We have a drink in a bar")
  else:
    print("We have a drink at home")


myObjects = []
def buyObject(object, money):
  if money >= object.precio:
    myObjects.append(object.nombre)

    return True
  else:
    return False

objects = pd.DataFrame({
    "nombre" : ["iPhone", "Notebook", "TV", "PlayStation", "Car"],
    "precio" : [350000, 250000, 100000, 150000, 2000000]
})

money = 2000000

for index,row in objects.iterrows():
  if  buyObject(row, money):
    money = money - row.precio
  else:
    print('Your wallet is empty')