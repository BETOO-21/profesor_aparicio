Alumno=[]
Notas=[]
Edades=[]
maximo=0
minimo=11
Pmax=0
Pmin=0
Lista=[]
nombre_minimo=""
nombre_maximo=""
nombre=""



n=int(input("Ingrese la cantidad de alumnos: "))

print(".........................")





for i in range(n):
    nombre=input("Ingrese el nombre del alumno: ")    
    Alumno.append(nombre)
    print("...........................")
    
    
for i in range(n):
    nota=int(input("Ingrese la nota del alumno: "))
    Notas.append(nota)
    print("............................")
    
    
for i in range(n):
    edad=int(input("Ingrese la edad del alumno: "))
    Edades.append(edad)
    print("..............................")
    
for i in range(n):
    print("Nombre: ", Alumno[i], "  ", "Nota: ", Notas[i], "  ", "edad: ", Edades[i] )
  




promedioE=sum(Edades)/n




promedioN=sum(Notas)/n






for i in range (n):
    if Notas[i]<minimo:
        minimo=Notas[i]
        nombre_minimo=Alumno[i]
        print(".............................")
        
        
    if Notas[i]>maximo:
        maximo=Notas[i]
        nombre_maximo=Alumno[i]
        print("..........................")
        
        
        
Lista.append(f"Promedio de edades: {promedioE}")
print("........................")


Lista.append(f"Promedio de Notas: {promedioN}")
print("......................")

for i in range(len(Lista)):
    print(Lista[i])
    print("............................")
    
    
print("La nota maxima es: ", maximo, "Alumno: ", nombre_maximo)

print("..................................................")

print("La nota minima es: ", minimo, "Alumno: ", nombre_minimo)

print("...................................................")
