# Ambos extremos están incluidos en el intervalo de años válidos.
def anio_valido(anio):
    return 1800 <= anio <= 2026


# Repetimos el pedido hasta recibir un año válido; return termina la función.
def pedir_anio():
    while True:
        anio = int(input("Año entre 1800 y 2026 (número entero): "))
        if anio_valido(anio):
            return anio
        print("Año fuera del intervalo. Intentá otra vez.")


# Para probarlo, ingresá 1799, luego 2027 y por último 2020.
anio_elegido = pedir_anio()
print("Año aceptado:", anio_elegido)
