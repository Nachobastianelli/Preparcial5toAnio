""" 
Realize el siguiente sistema de notas para un profesor:

En un parcial hay una cantidad desconocida de alumnos, el profesor va a ingresar sus respectivas notas al 
programa. Para cerrar va a tener que ingresar un 0.


Facil:
 
indique: 
    El promedio total de las notas del curso
    La cantidad de alumnos que realizaron al parcial
    
Maomeno:

indique:
    La cantidad de alumnos que desaprobaron
    La cantidad de alumnos que aprobaron


""" 
notaDeAlumnos = int(input("Ingrese la nota del primer alumno (diferente de 0): \n")) 
#El while de abajo es para validar que la nota sea menor a 10 y mayor a 0.
while (notaDeAlumnos < 0 or notaDeAlumnos > 10):
        #Le muestra que ocurrio un error y le pide la nota de nuevo
        print("Ocurrio un error. La nota debe estar entre 0 y 10")
        notaDeAlumnos = int(input("Ingrese la nota del alumno: \n"))
#incializar las variables
#Contadores o acumuladores
cantidadTotalDeAlumnos = 0
totalDeNotasDeLosAlumnos = 0
cantidadTotalDeAlumnosQueAprobaron = 0
cantidadTotalDeAlumnosQueDesaprobaron = 0

#Solo va a entrar y repetir el bucle MIENTRAS que la nota sea diferente de 0
while(notaDeAlumnos != 0):
    #Acumulador de notas del curso (Ingresa una nota y se le suma)
    totalDeNotasDeLosAlumnos = totalDeNotasDeLosAlumnos + notaDeAlumnos 
    print(f"El total de las notas es de {totalDeNotasDeLosAlumnos}") 
    #Contador de cantidad de alumnos que hicieron el parcial (Aumenta en 1 cada vez que entra en un bucle)
    cantidadTotalDeAlumnos = cantidadTotalDeAlumnos + 1
    #pide la nota de vuelta
    notaDeAlumnos = int(input(f"Ingrese la nota del alumno {cantidadTotalDeAlumnos + 1}: \n"))
    #condicion aca NO VA
    #De vuelta valida que la nota sea correcta
    while (notaDeAlumnos < 0 or notaDeAlumnos > 10):
        print("Ocurrio un error. La nota debe estar entre 0 y 10")
        notaDeAlumnos = int(input("Ingrese la nota del alumno: \n"))
    #CONDICION SI VA ACA
    if (notaDeAlumnos >= 6):
        cantidadTotalDeAlumnosQueAprobaron = cantidadTotalDeAlumnosQueAprobaron + 1
    else:
        cantidadTotalDeAlumnosQueDesaprobaron = cantidadTotalDeAlumnosQueDesaprobaron + 1
    
    #Al final del bucle va a ver si la ultima nota que ingreso es 0. 
    #Si es 0 va a salir del bucle y va a mostrar la informacion almacenada hasya el momento
    #Si es un numero entre 1 y 10 va a seguir juntando informacion

    
#La f antes de las comillas del print sirven para mostrar variables adentro (SE MUESTRAN ADENTRO DE LAS COMILLAS Y CON CORCHETE)
print(f"La cantidad de alumnos que aprobaron son : {cantidadTotalDeAlumnosQueAprobaron}.")
print(f"La cantidad de alumnos que desaprobaron son : {cantidadTotalDeAlumnosQueDesaprobaron}.")

# Esto es si no tenes la cantidad de alumnos que desaprobaron: print(f"La cantiadd de alumnos que desaprobaron es de: {cantidadTotalDeAlumnos - cantidadTotalDeAlumnosQueAprobaron}")
print(f"La cantidad de alumnos que tomaron el parcial es de: {cantidadTotalDeAlumnos} \nEl promedio total de los alumnos es: {totalDeNotasDeLosAlumnos / cantidadTotalDeAlumnos}")
        
