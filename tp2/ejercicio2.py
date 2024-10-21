# Diccionario de productos y precios
productos = {
    "Producto1": 100,
    "Producto2": 200,
    "Producto3": 150
}

# Función para calcular el total a pagar
def calcular_total(compra):
    total = sum(productos[producto] for producto in compra)
    return total

# Productos que se quieren comprar
compra = ["Producto1", "Producto3"]

# Resultado
total = calcular_total(compra)
print(f"Total a pagar: {total}")
