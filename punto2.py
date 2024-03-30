def missing_number(n, secuencia):
    # Crea una lista con los números de 1 a n
    numeros = list(range(1, n + 1))
    # Recorre la lista secuencia
    for i in secuencia:
        # Si el número se encuentra en la lista de números, se elimina
        if i in numeros:
            numeros.remove(i)
    # Se retorna el número faltante
    return numeros[0]
# caso de prueba
assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"

print(missing_number(5, [1, 2, 4, 5]))