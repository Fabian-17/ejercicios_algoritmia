def number_spiral(x, y):
    # Verificar si x e y son enteros positivos
    if not (isinstance(x, int) and isinstance(y, int)) or x <= 0 or y <= 0:
        return "x e y deben ser números enteros positivos"
    # se usa la función abs para obtener el valor absoluto de x e y
    if abs(x) > 10 ** 6 or abs(y) > 10 ** 6:
        return "x e y no deben superar 10^6"
    
    # Calcula el número en la posición (x, y)
    if x > y:
        if x % 2 == 0:
            # si x es mayor que y, si x es par, se calcula x al cuadrado menos y, más 1
            return x ** 2 - y + 1
        if x % 2 != 0:
            # si x es mayor que y, si x es impar, se calcula x menos 1 al cuadrado más y
            return (x - 1) ** 2 + y
    else:
        if y % 2 == 0:
            # si y es mayor que x, si y es par, se calcula y menos 1 al cuadrado más x
            return (y - 1) ** 2 + x
        if y % 2 != 0:
            # si y es mayor que x, si y es impar, se calcula y al cuadrado menos x, más 1
            return y ** 2 - x + 1

# caso de prueba
assert number_spiral(2, 2) == 3, "Error en el caso de prueba"

print(number_spiral(2, 2))
