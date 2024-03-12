nombre = str(input("Ingrese su nombre: ")).capitalize()
edad = int(input("Ingrese su edad:"))
ciudad = str(input("Ingrese su ciudad de residencia: ")).lower()

if  len(ciudad) < 3: # si la ciudad contiene 2 letras 
    print("El nombre de ciudad es muy corto, intente nuevamente")
    ciudad = str(input("Ingrese su ciudad de residencia: ")).lower()

nacionalidad = str(input("¿Tiene nacionalidad si | no?: ")).lower()
genero = str(input("Ingrese su género (M |F | O):")).upper()



if nacionalidad == "si":
    nacionalidad = True
else: 
    nacionalidad = False

# Saludar y mostrar su info personal; edad, residencia y año de nacimiento
print(f'Hola {nombre}')
print("Hola", nombre)

# año de nacimiento
anio_actual = 2023
anio_nacimiento = anio_actual - edad

print("Tienes", edad, "años y naciste en", anio_nacimiento, "y vives en", ciudad)
print(f'Tienes {edad} años y naciste en {anio_nacimiento} y vives en {ciudad}')

# ¿Es mayor de edad?
if edad >= 18:
    print(f'{nombre} eres mayor de edad.')

else: 
    print(f'{nombre} no eres mayor de edad.')


if (edad < 50) and (ciudad == "buenos aires"):
    print(f'Un gusto {nombre} eres menor a 50 y vives en BA')


if edad >= 18:
    # if nacionalida == True:
    # if nacionalidad is True:
    if nacionalidad:
        print("Puede votar")
    else:
        print("No puede votar")

else:
    print("No puede votar")


if genero == "M":
    print(f'Hola {nombre}, su género es masculino.')

elif genero == "F":
    print(f'Hola {nombre}, su género es femenino.')

else:
    print(f'Hola {nombre}, su género es otro.')