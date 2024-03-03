#Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades. En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.
#Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.
#Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
#Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla.

dimension_temperaturas = [# Ciudades

    [#semana1
        ["Quito", "temperatura",17],
        ["Guayaquil","temperatura",18],
        ["Cuenca","temperatura",20],
        ["Machala","temperatura",26],
        ["Riobamba","temperatura",26],
        ["Ambato","temperatura",19],
        ["Loja","temperatura",23]
    ],
    [#semana2
    ["Quito", "temperatura", 19],
    ["Guayaquil", "temperatura", 26],
    ["Cuenca", "temperatura", 18],
    ["Machala", "temperatura", 29],
    ["Riobamba", "temperatura", 18],
    ["Ambato", "temperatura", 122],
    ["Loja", "temperatura",19]
    ],
[#semana3
    ["Quito", "temperatura", 20],
    ["Guayaquil", "temperatura", 25],
    ["Cuenca", "temperatura", 19],
    ["Machala", "temperatura", 28],
    ["Riobamba", "temperatura", 22],
    ["Ambato", "temperatura", 17],
    ["Loja", "temperatura",18]
]
]

print(dimension_temperaturas[0][6][0])
for fila in range(len(dimension_temperaturas)):
     for columna in range(len(dimension_temperaturas[fila])):

        for doc in range(len(dimension_temperaturas[fila][columna])):
            print("fila",fila, "columna", "doc", doc, "=", dimension_temperaturas[fila][columna][doc])



