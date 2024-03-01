def c_a_f(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def positivo_o_negativo():
    numero = float(input("Ingrese un número: "))
    if numero <= 0:
        print("El número es negativo.")
    else:
        print("El número es positivo.")

def es_par_o_impar():
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")

def numeros_a_letras():
    numero = int(input("Ingrese un número entre 1 y 5: "))
    numeros = ["", "uno", "dos", "tres", "cuatro", "cinco"]
    if 1 <= numero <= 5:
        print(f"El número {numero} en letras es '{numeros[numero]}'")
    else:
        print("Número fuera de rango.")

def numeros_y_suma():
    n = int(input("Ingrese la cantidad de números que desea sumar: "))
    numeros = [float(input(f"Ingrese el número {i + 1}: ")) for i in range(n)]
    suma = sum(numeros)
    print(f"La suma de los números ingresados es: {suma}")

def main():
    while True:
        print("-----------------Menu----------------")
        print("1. Convertir centígrados a Fahrenheit")
        print("2. Positivo o Negativo")
        print("3. Par o Impar")
        print("4. Números a letras")
        print("5. Números y su suma")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            c = float(input("Ingrese cantidad de grados Celsius a convertir a Fahrenheit: "))
            f = c_a_f(c)
            print(f"{c} grados Celsius son {f} grados Fahrenheit")
        elif opcion == "2":
            positivo_o_negativo()
        elif opcion == "3":
            es_par_o_impar()
        elif opcion == "4":
            numeros_a_letras()
        elif opcion == "5":
            numeros_y_suma()
        elif opcion == "6":
            print("Saliendo del programa.")
            break

if __name__ == "__main__":
    main()

