Cada cierto número de días se deben aplicar estas fórmulas sobre los precios de los productos:

`indice_demanda = num_compras / (num_ventas + num_compras)`

`indice_oferta = num_ventas / (num_ventas + num_compras)`

`precio_final = precio_actual * (1 + indice_demanda - indice_oferta)`

En caso de no cambiar el precio de un producto durante esos días y habiendo actividad en la tienda, se reducirá el precio en un 5% del precio base de dichos productos. Añadir un factor aleatorio para alterar muy ligeramente el precio durante ese periodo.

El precio máximo de un producto no puede superar bajo ningún concepto el 5000% del precio original y, por el contrario, un precio no puede ser inferior al 2% del precio original (los porcentajes son valores por defecto con posibilidad de ajuste personalizado).