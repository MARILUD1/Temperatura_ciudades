#Desarrolla una función en Python que calcule la temperatura promedio de una ciudad durante un período de tiempo. La función debe ser capaz de manejar datos de temperaturas de múltiples ciudades y semanas.

#Utiliza como base el ejemplo anterior, donde tenías datos de 3 ciudades durante 4 semanas.

#Tu función debe recibir estos datos como parámetros y calcular la temperatura promedio de cada ciudad.

1
def calcula_dimensiontemperatura(datos, provincia, ciudades_inicio, ciudades_final):
    num_items = 0
    suma_temperatura = 0
    for i in range(len(datos[provincia])):
        if i>=ciudades_inicio and i<ciudades_final:
            for j in range(len(datos[provincia][i])):
                suma_temperatura = suma_temperatura+datos[provincia][i][j]['temperatura']
                num_items = num_items + 1

                print(datos[provincia][i][j])

    promedio = suma_temperatura/num_items
    return promedio


datostemperaturas = [
    [   # Provincia 1
      [  # Ciudades 1
        {"city": "Quito", "temperatura": 17},
        {"city": "Guayaquil", "temperatura": 18},
        {"city": "Cuenca", "temperatura": 20},
        {"city": "Machala", "temperatura": 26},
        {"city": "Riobamba", "temperatura": 26},
        {"city": "Ambato", "temperatura": 19},
        {"city": "Loja", "temperatura": 23}
      ],

      [  # Ciudades 2
        {"city": "Azuay", "temperatura": 19},
        {"city": "Cañar", "temperatura": 26},
        {"city": "Cuenca", "temperatura": 8},
        {"city": "Bolivar", "temperatura": 29},
        {"city": "Riobamba", "temperatura": 18},
        {"city": "Carchi", "temperatura": 12},
        {"city": "Galapagos", "temperatura": 19}
      ],

      [  # Ciudades 3
        {"city": "Quito", "temperatura": 20},
        {"city": "Guayaquil", "temperatura": 25},
        {"city": "Cuenca", "temperatura": 19},
        {"city": "Machala", "temperatura": 28},
        {"city": "Riobamba", "temperatura": 22},
        {"city": "Ambato", "temperatura": 17},
        {"city": "Cotopaxi", "temperatura": 18}
      ]
    ],
    [  # Provincia 2
      [  # Ciudades 1
        {"city": "Chimborazo", "temperatura": 18},
        {"city": "Esneraldas", "temperatura": 18},
        {"city": "Imbabura", "temperatura": 22},
        {"city": "Babahoyo", "temperatura": 29},
        {"city":"Riobamba", "temperatura": 18},
        {"city": "Ambato", "temperatura": 19},
        {"city": "pastaza", "temperatura": 23}
      ],

      [  # Ciudades 2
        {"city": "Manabí", "temperatura": 19},
        {"city": "Zamora Chincipe", "temperatura": 26},
        {"city": "Cuenca", "temperatura": 18},
        {"city": "Los Rios", "temperatura": 29},
        {"city": "El Oro", "temperatura": 18},
        {"city": "Morona Santiago", "temperatura": 12},
        {"city": "Sucumbios", "temperatura": 19}
      ],

      [  # Ciudades 3
        {"city": "Quito", "temperatura": 20},
        {"city": "Guayaquil", "temperatura": 25},
        {"city": "Cuenca", "temperatura": 19},
        {"city": "Machala", "temperatura": 28},
        {"city": "Riobamba", "temperatura": 22},
        {"city": "Ambato", "temperatura": 17},
        {"city": "Loja", "temperatura": 18}
      ]
    ]
]


provincia = input("Ingrese la provincia=")

promedio_calc = calcula_dimensiontemperatura(datostemperaturas, 1, 0, 3)

print(promedio_calc)