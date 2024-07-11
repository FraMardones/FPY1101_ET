import os
import csv
import time
import random

trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandes","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
lista_sueldo = []
solo_sueldo = []

try:
    with open("registro_sueldos.csv", "x",newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])
except FileExistsError:
    pass

def asignar_sueldos():
    for i in range(1):
        for nombre in trabajadores:
            plata = (random.randint(300000,2500000))
            sueldo = plata
            solo_sueldo.append(sueldo)
            lista_sueldos = [
                    [nombre ,sueldo]
                ]
            lista_sueldo.append(lista_sueldos)
        
def reporte_sueldos():
    sueldoB = []
    descuentoS = []
    descuentoaf = []
    sueldoliqui = []
    nombres = []
    
    for nombre in trabajadores:
        nombres.append(nombre)
    
    for i in solo_sueldo:
        sueldobase = i
        sueldoB.append(sueldobase)
        descuentosalud = round(i*0.07)
        descuentoS.append(descuentosalud)
        descuentoafp = round(i*0.12)
        descuentoaf.append(descuentoafp)
        sueldoliquido = round(sueldobase - (descuentoafp + descuentosalud))
        sueldoliqui.append(sueldoliquido)

    with open ("registro_sueldos.csv", "a",newline="") as archivo:
        escritor = csv.writer(archivo)
        for i in range (1):
            escritor.writerows(([trabajadores,sueldoB,descuentoS,descuentoaf,sueldoliqui]))
    print("Datos guardados correctamente en el archivo registro_sueldos.csv")

def clasificar_sueldos():
    sueldo_menor = 0
    sueldo_medio = 0
    sueldo_mayor = 0
    for i in range(1):
        for i in solo_sueldo:
            if sueldo_menor < 800000 and sueldo_menor >= 300000:
                sueldo_menor += 1
            elif sueldo_medio >= 800000 or sueldo_medio == 2000000:
                sueldo_medio += 1
            elif sueldo_mayor > 2000000:
                sueldo_mayor +=1
    print(f"sueldos menores a 800.000: {sueldo_menor}")
    print(f"sueldos entre 800.000 y 2.000.000: {sueldo_medio}")
    print(f"sueldos mayores a 2.000.000: {sueldo_mayor}")

def estadisticas():
    for i in solo_sueldo:
        sueldo_bajo = min(solo_sueldo)
        sueldo_alto = max(solo_sueldo)
        promedio = sum(solo_sueldo) / len(solo_sueldo)
        for producto in solo_sueldo:
            i *= producto
        media = i ** (1/len(solo_sueldo))
    print(f"El sueldo mas bajo es: {sueldo_bajo}")
    print(f"El sueldo mas alto es: {sueldo_alto}")
    print(f"El promedio de los sueldos es: {promedio}")
    print(f"La media geometrica de los sueldos es: {media}")

def salir():
    print("Finalizando programa...")
    print("Desarrollado por Francisco Mardones")
    print("21.866.252-8")
    exit()

def menu():
    print("Bienvenido")
    asignar_sueldos()
    while True:
        opc = int(input("""
Que desea hacer?
1.Clasificar sueldos
2.Estadisticas
3.Reporte de sueldos
4.Salir
Seleccione: """))
        if opc == 1:
            clasificar_sueldos()
        elif opc == 2:
            estadisticas()
        elif opc == 3:
            reporte_sueldos()
        elif opc == 4:
            salir()
        else:
            print("Opcion incorrecta, elija una opcion del 1 al 4")
menu()
