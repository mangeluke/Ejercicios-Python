#Ejercicio de grupo de 10 estudiantes que presentan examen de algoritmia.
calificacion1=int(input("Ingrese su calificación:"))
calificacion2=int(input("Ingrese su calificación:"))
calificacion3=int(input("Ingrese su calificación:"))
calificacion4=int(input("Ingrese su calificación:"))
calificacion5=int(input("Ingrese su calificación:"))
calificacion6=int(input("Ingrese su calificación:"))
calificacion7=int(input("Ingrese su calificación:"))
calificacion8=int(input("Ingrese su calificación:"))
calificacion9=int(input("Ingrese su calificación:"))
calificacion10=int(input("Ingrese su calificación:"))

calificacionMenor50=0
calificacionMayor50Menor70=0
calificacionMayor70Menor80=0
calificacionMayor80=0

if calificacion1>=1 and calificacion1<=49:
    calificacionMenor50 +=1
elif calificacion1>=50 and calificacion1<=69:
    calificacionMayor50Menor70 +=1
elif calificacion1>=70 and calificacion1<=79:
    calificacionMayor70Menor80 +=1
elif calificacion1>=80 and calificacion1<=100:
    calificacionMayor80 +=1

if calificacion2>=1 and calificacion2<=49:
    calificacionMenor50 +=1
elif calificacion2>=50 and calificacion2<=69:
    calificacionMayor50Menor70 +=1
elif calificacion2>=70 and calificacion2<=79:
    calificacionMayor70Menor80 +=1
elif calificacion2>=80 and calificacion2<=100:
    calificacionMayor80 +=1

if calificacion3>=1 and calificacion3<=49:
    calificacionMenor50 +=1
elif calificacion3>=50 and calificacion3<=69:
    calificacionMayor50Menor70 +=1
elif calificacion3>=70 and calificacion3<=79:
    calificacionMayor70Menor80 +=1
elif calificacion3>=80 and calificacion3<=100:
    calificacionMayor80 +=1

if calificacion4>=1 and calificacion4<=49:
    calificacionMenor50 +=1
elif calificacion4>=50 and calificacion4<=69:
    calificacionMayor50Menor70 +=1
elif calificacion4>=70 and calificacion4<=79:
    calificacionMayor70Menor80 +=1
elif calificacion4>=80 and calificacion4<=100:
    calificacionMayor80 +=1
    
if calificacion5>=1 and calificacion5<=49:
    calificacionMenor50 +=1
elif calificacion5>=50 and calificacion5<=69:
    calificacionMayor50Menor70 +=1
elif calificacion5>=70 and calificacion5<=79:
    calificacionMayor70Menor80 +=1
elif calificacion5>=80 and calificacion5<=100:
    calificacionMayor80 +=1
    
if calificacion6>=1 and calificacion6<=49:
    calificacionMenor50 +=1
elif calificacion6>=50 and calificacion6<=69:
    calificacionMayor50Menor70 +=1
elif calificacion6>=70 and calificacion6<=79:
    calificacionMayor70Menor80 +=1
elif calificacion6>=80 and calificacion6<=100:
    calificacionMayor80 +=1

if calificacion7>=1 and calificacion7<=49:
    calificacionMenor50 +=1
elif calificacion7>=50 and calificacion7<=69:
    calificacionMayor50Menor70 +=1
elif calificacion7>=70 and calificacion7<=79:
    calificacionMayor70Menor80 +=1
elif calificacion7>=80 and calificacion7<=100:
    calificacionMayor80 +=1

if calificacion8>=1 and calificacion8<=49:
    calificacionMenor50 +=1
elif calificacion8>=50 and calificacion8<=69:
    calificacionMayor50Menor70 +=1
elif calificacion8>=70 and calificacion8<=79:
    calificacionMayor70Menor80 +=1
elif calificacion8>=80 and calificacion8<=100:
    calificacionMayor80 +=1

if calificacion9>=1 and calificacion9<=49:
    calificacionMenor50 +=1
elif calificacion9>=50 and calificacion9<=69:
    calificacionMayor50Menor70 +=1
elif calificacion9>=70 and calificacion9<=79:
    calificacionMayor70Menor80 +=1
elif calificacion9>=80 and calificacion9<=100:
    calificacionMayor80 +=1
    
if calificacion10>=1 and calificacion10<=49:
    calificacionMenor50 +=1
elif calificacion10>=50 and calificacion10<=69:
    calificacionMayor50Menor70 +=1
elif calificacion10>=70 and calificacion10<=79:
    calificacionMayor70Menor80 +=1
elif calificacion10>=80 and calificacion10<=100:
    calificacionMayor80 +=1

print("La cantidad de estudiantes que obtuvieron calificación menor a 50 es: ", calificacionMenor50)
print("La cantidad de estudiantes que obtuvieron calificación entre 50 y 70 es: ", calificacionMayor50Menor70)
print("La cantidad de estudiantes que obtuvieron calificación entre 70 y 80 es: ", calificacionMayor70Menor80)
print("La cantidad de estudiantes que obtuvieron calificación mayor a 80 es: ", calificacionMayor80)