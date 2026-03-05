estudiantes= int(input("cuantos estudiantes van a ingresar"))
aprobados  = 0
reprobados = 0
suma_promedios = 0
for i in range (estudiantes):
    nombre= input("cual es el nombre del estudiante")
    nota_1= float(input("cual es su primera nota (1/5)"))
    nota_2= float(input("cual es su segunda nota (1/5)"))
    nota_3= float(input("cual es su tercera nota (1/5)"))
    promedio = (nota_1 + nota_2 + nota_3)/3
    print("el nombre del estudiante es:",nombre)
    print("el promedio de nota es:",round(promedio,2))
    suma_promedios += promedio
    if promedio >= 3:
        print("el estudiante aprobo")
        aprobados +=1

    else :
        print("el estudiante no aprobo")    
        reprobados +=1
promedio_general = suma_promedios / estudiantes

print("\n= RESULTADOS FINALES ")
print("Promedio general del grupo:", round(promedio_general, 2))
print("Cantidad de estudiantes que aprobaron:", aprobados)
print("Cantidad de estudiantes que no aprobaron:", reprobados)