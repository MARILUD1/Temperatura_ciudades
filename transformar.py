# crear una funcion para convertir grados centigrados a grados Fahrenheit
#Fahrenheit=(9/5)*(grados_cent)+32
#Kelvin=273.15 + grados_cent

def convertir(grados_cent):
    Fahrenheit= (9/5)*(grados_cent)+32
    Kelvin=273.15 + grados_cent
    return Fahrenheit,Kelvin

centigrados = int(input("ingresar los grados centigrados="))
resp_far, resp_kelvin = convertir(centigrados)
print(centigrados,"grados centigrados" "=", resp_far, "grados Fahrenheit")
print("Kelvin", resp_kelvin)









