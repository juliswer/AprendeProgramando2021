variable1 = 1
variable2 = 2
print(variable1 + 1)
print(variable2 + 2)
print(variable1 - 1)
print(variable2 - 2)
print(variable1 * 1)
print(variable2 * 2)
print(variable1 / 1)
print(variable2 / 2)

grupo1 = ["1", "2", "3", "4"]
grupo2 = ["1", "2", "3", "4"]
grupo3 = []
grupo3.append(grupo1[3])
grupo3.append(grupo2[3])
grupo1.pop()
grupo2.pop()
print(grupo1)
print(grupo2)
print(grupo3)
todos = []
todos.append(grupo1 + grupo2)
print(todos)

NTVG = {
  "nombre_banda" : "No te va a gustar",
  "datos:" : {
    "albumes" : ["Por lo menos hoy", "Este fuerte viento que sopla", "Publico", "Suenan las alarmas"],
    "origen" : "Uruguay",
    "cantante" : "Emiliano Brancciari",
    "cantidad_integrantes" : 15
  },
  "cancion_favorita" : "Angel con campera"
}

print(NTVG)