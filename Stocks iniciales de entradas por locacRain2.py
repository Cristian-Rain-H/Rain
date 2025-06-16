# Stocks iniciales de entradas por locación
stock_concepcion = 500
stock_puente_alto = 1300
stock_valparaiso = 100
stock_vina_del_mar = 50

# Listas para almacenar los nombres de compradores por locación
compradores_concepcion = []
compradores_puente_alto = []
compradores_valparaiso = []
compradores_vina_del_mar = []

def validar_nombre_comprador(nombre, lista_compradores):
    if nombre in lista_compradores:
        print("Error: El nombre del comprador ya está registrado para esta locación.")
        return False
    return True

def comprar_concepcion():

    global stock_concepcion
    print("\n-- Compra en Concepción --")
    if stock_concepcion <= 0:
        print("Lo sentimos, no quedan entradas para Concepción.")
        return

    nombre = input("Nombre del comprador: ").strip()
    if not validar_nombre_comprador(nombre, compradores_concepcion):
        return

    codigo_confirmacion = input("Código de confirmación: ")

    # Validar código de confirmación
    if (len(codigo_confirmacion) < 6 or
        not any(c.isupper() for c in codigo_confirmacion) or
        not any(c.isdigit() for c in codigo_confirmacion) or
        " " in codigo_confirmacion):
        print("Error: código de confirmación inválido.")
        print("Debe tener al menos 6 caracteres, 1 mayúscula, 1 número y sin espacios.")
        return

    # Si todas las validaciones son exitosas
    compradores_concepcion.append(nombre)
    stock_concepcion -= 1
    print(f"Entrada registrada! Stock restante: {stock_concepcion}")

def comprar_puente_alto():
    
    global stock_puente_alto
    print("\n-- Compra en Puente Alto --")
    if stock_puente_alto <= 0:
        print("Lo sentimos, no quedan entradas para Puente Alto.")
        return

    nombre = input("Nombre del comprador: ").strip()
    if not validar_nombre_comprador(nombre, compradores_puente_alto):
        return

    try:
        cantidad = int(input("Cantidad de entradas (máx 3): "))
    except ValueError:
        print("Error: Ingrese un número válido para la cantidad de entradas.")
        return

    if not (1 <= cantidad <= 3):
        print("Error: solo se permiten entre 1 y 3 entradas por persona.")
        return

    if stock_puente_alto < cantidad:
        print(f"Lo sentimos, solo quedan {stock_puente_alto} entradas disponibles.")
        return

    # Si todas las validaciones son exitosas
    compradores_puente_alto.append(nombre)
    stock_puente_alto -= cantidad
    print(f"Entradas registradas! Stock restante: {stock_puente_alto}")

def comprar_valparaiso():
    
    global stock_valparaiso
    print("\n-- Compra en Muelle Barón, Valparaíso --")
    if stock_valparaiso <= 0:
        print("Lo sentimos, no quedan entradas para Muelle Barón, Valparaíso.")
        return

    nombre = input("Nombre del comprador: ").strip()
    if not validar_nombre_comprador(nombre, compradores_valparaiso):
        return

    # Tipo de entrada "G" asignado por defecto
    tipo_entrada = "G"

    # Si todas las validaciones son exitosas
    compradores_valparaiso.append(nombre)
    stock_valparaiso -= 1
    print(f"Tipo de entrada asignado: {tipo_entrada}")
    print(f"Entrada registrada! Stock restante: {stock_valparaiso}")

def comprar_vina_del_mar():
    
    global stock_vina_del_mar
    print("\n-- Compra en Muelle Vergara, Viña del Mar --")
    if stock_vina_del_mar <= 0:
        print("Lo sentimos, no quedan entradas para Muelle Vergara, Viña del Mar.")
        return

    nombre = input("Nombre del comprador: ").strip()
    if not validar_nombre_comprador(nombre, compradores_vina_del_mar):
        return

    tipo_entrada = input("Tipo de entrada (Sun=Sunset, Ni=Night): ").strip().capitalize()

    if tipo_entrada not in ("Sun", "Ni"):
        print("Error: tipo de entrada inválido. Debe ser 'Sun' o 'Ni'.")
        return

    # Si todas las validaciones son exitosas
    compradores_vina_del_mar.append(nombre)
    stock_vina_del_mar -= 1
    print(f"Entrada registrada! Stock restante: {stock_vina_del_mar}")

def main():
    
    while True:
        print("\nTOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE")
        print("1.- Comprar entrada a “los Fortificados” en Concepción.")
        print("2.- Comprar entrada a “los Fortificados” en Puente Alto.")
        print("3.- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso.")
        print("4.- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar.")
        print("5.- Salir.")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            comprar_concepcion()
        elif opcion == '2':
            comprar_puente_alto()
        elif opcion == '3':
            comprar_valparaiso()
        elif opcion == '4':
            comprar_vina_del_mar()
        elif opcion == '5':
            print("\nPrograma terminado...")
            break
        else:
            print("\nDebe ingresar una opción válida!!")

if __name__ == "__main__":
    main()