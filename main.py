def adivina_el_numero():
    """
    Juego donde la computadora adivina el número que el usuario piensa (1-100)
    usando búsqueda binaria y guarda los intentos en una lista de tuplas.
    """
    print("Piensa en un número del 1 al 100. Yo trataré de adivinarlo.")
    input("Presiona Enter cuando estés listo...")

    bajo = 1
    alto = 100
    intentos = 0
    intentos_maximos = 10  # Límite para evitar bucles infinitos

    historial = []  # Lista de tuplas (intento, respuesta)

    while bajo <= alto and intentos < intentos_maximos:
        # Cálculo del número a adivinar (punto medio)
        intento = (bajo + alto) // 2
        intentos += 1

        print(f"Intento #{intentos}: ¿Es {intento} tu número?")
        respuesta = input("Responde 'mayor', 'menor' o 'sí': ").strip().lower()

        # Guardamos en la tupla
        historial.append((intento, respuesta))

        if respuesta in ("sí", "si"):
            print(f"🎉 ¡Genial! Adiviné tu número en {intentos} intentos.")
            break
        elif respuesta == "mayor":
            bajo = intento + 1
        elif respuesta == "menor":
            alto = intento - 1
        else:
            # Mensaje de error si la respuesta no es válida
            print("❌ Respuesta inválida. Por favor responde con 'mayor', 'menor' o 'sí'.")

    else:
        # Se ejecuta si el bucle termina sin adivinar
        print("🤔 Parece que hubo un error en las respuestas o se alcanzó el límite de intentos.")

    # Mostrar historial de intentos
    print("\n📜 Historial de intentos:")
    for intento, resp in historial:
        print(f"- Computadora dijo: {intento}, Usuario respondió: {resp}")


# Ejecutar el juego
if __name__ == "__main__":
    adivina_el_numero()
