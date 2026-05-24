# Matriz de inventario
inventario = [
    [101, "Teclado", 3, 10],
    [102, "Mouse", 15, 10],
    [103, "Monitor", 2, 5],
    [104, "USB", 20, 15],
    [105, "Laptop", 1, 4]
]

# Función para calcular cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Recorrer la matriz
for articulo in inventario:

    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # Calcular pedido
    cantidad = calcular_pedido(stock_actual, stock_minimo)

    # Mostrar resultado
    print(nombre, "- Cantidad a pedir:", cantidad)