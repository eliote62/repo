#ejercicio 7
##for i in range(1, 11):
#    for j in range(1, 11):
#       print(i*j, end="\t")
#    print("")

#ejercicio 8
#n = int(input("Introduce la altura del triángulo (entero positivo): "))
#for i in range(1, n+1, 2):
#    for j in range(i, 0, -2):
#        print(j, end=" ")
#    print("")
    
#ejercicio 9
key = "contraseña"
password =""
while password != key:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")