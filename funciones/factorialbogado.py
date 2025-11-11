def factorial(n):
    """Devuelve el factorial de un número entero no negativo."""
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
