def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    """Devuelve a / b. Lanza ValueError si b es 0."""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

if __name__ == "__main__":
    # Ejemplos rápidos de uso
    print("2 + 3 =", sumar(2, 3))
    print("5 - 2 =", restar(5, 2))
    print("3 * 4 =", multiplicar(3, 4))
    try:
        print("10 / 2 =", dividir(10, 2))
        print("10 / 0 =", dividir(10, 0))
    except ValueError as e:
        print("Error:", e)