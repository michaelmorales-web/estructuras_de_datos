def obtener_primero_ultimo(lista):
    if not lista:
        return "Dato no válido. Lista vacía"
    
    if len(lista) >= 2:
        return (lista[0], lista[-1])
    else:
        return "La lista no tiene elementos suficientes"


# Prueba
lista_1 = [1, 2, 3, 4]
resultado = obtener_primero_ultimo(lista_1)
print(resultado)