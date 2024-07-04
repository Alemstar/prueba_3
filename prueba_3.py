from datetime import date
import csv
#date().strftime("%d-%m-%Y %H:%M:%s")

count = 11
datos_usuario = []
habitaciones = []

for piso in range (1, 5):
    for habitacion in range (11, 18):
        count +=1
        if count == 19:
            count = 11

def reservar_habitacion (nombre, apellido, rut, fecha_e, fecha_s, hora_e, hora_s):
    datos_usuario.append ([nombre, apellido, rut, fecha_e,fecha_s,hora_e, hora_s])
    return datos_usuario

def buscar_habitacion ():
    habitacion_n = input ("Ingrese el número de habitacion (debe estar en un rango de 11 a 41)")

#def ver_estado ():

#def ventas_diarias ():

def guardar ():
    with open ('habitaciones.csv', 'w', newline="") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerows([[habitaciones, datos_usuario]])

reservaciones = []

while True:
    op = int (input ("Bienvenido! indique que desea realizar \n 1) Reservar habitación \n 2) buscar habitacion \n 3) estado de habitacion \n 4) Ventas diarias \n 5) guardar \n 6) Salir \n"))

    if op == 1:
        try:
            nombre = input ("ingrese su nombre: ")
            apellido = input ("Ingrese su apellido: ")
        except ValueError:
            print ("Debe ingresar un valor tipo alfabetico")
        try:
            rut = int (input("ingrese su rut: "))
            fecha_e = int (input ("Ingrese la fecha de entrada: "))
            fecha_s = int (input ("Ingrese la fecha de salida: "))
            hora_e = int (input ("Ingrese la hora de entrada: "))
            hora_s = int (input ("Ingrese la hora de salida: "))
        except ValueError:
            print ("Debe ingresar valores numericos")

    reservar_habitacion (nombre, apellido, rut, fecha_e, fecha_s, hora_e, hora_s)

    #if op == 2:

    #if op == 3:

    #if op == 4:

    if op == 5:
        guardar()