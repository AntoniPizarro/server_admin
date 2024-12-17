from random import randint

from config import MIN_PRICE_PERCENTAGE, MAX_PRICE_PERCENTAGE

def apply_supply_demand_unlimited_stock(item, purchases_count: int, sales_count: int, max_price_percentage: float=MAX_PRICE_PERCENTAGE, min_price_percentage: float=MIN_PRICE_PERCENTAGE, variance: float=5):
    """
    Cálculo de los precios para generar un sistema de oferta y demanda.

    `indice_demanda = num_compras / (num_ventas + num_compras)`

    `indice_oferta = num_ventas / (num_ventas + num_compras)`
    
    `precio_final = precio_actual * (1 + indice_demanda - indice_oferta)`

    En caso de no cambiar el precio de un producto durante esos días y habiendo actividad en la tienda, se reducirá el precio en un 5% del precio base de dichos productos. Añadir un factor aleatorio para alterar muy ligeramente el precio durante ese periodo.

    El precio máximo de un producto no puede superar bajo ningún concepto el 5000% del precio original y, por el contrario, un precio no puede ser inferior al 2% del precio original (los porcentajes son valores por defecto con posibilidad de ajuste personalizado).
    """
    # Si no han habido compras ni ventas, los índices serán 0
    if purchases_count == 0 and sales_count == 0 and purchases_count == 0:
        demand_index = 0
        supply_index = 0
    # De lo contrario se aplican las fórmulas para obtener los índices de compra y venta
    else:
        demand_index = (purchases_count / (sales_count + purchases_count))
        supply_index = (sales_count / (sales_count + purchases_count))

    # En función de los índices obtenidos, se ajusta el nuevo precio
    final_price = item.get_price() + (item.get_base_price() * (1 + demand_index - supply_index)) - item.get_base_price()

    # Nos aseguramos de que ha cambiado el precio
    if int(final_price) == item.get_price():
        # Ajustamos ligeramente el precio en caso de no haber tenido iteracciones ni de compra ni de venta
        item.set_price(final_price * (1 - (randint(-variance, variance)) / 100))
    else:
        # Comprobamos si el precio es superior o no al precio máximo
        if final_price >= item.get_base_price() * max_price_percentage / 100:
            final_price = item.get_base_price() * max_price_percentage / 100
        # Comprobamos si el precio es superior o no al precio mínimo
        elif final_price <= item.get_base_price() * min_price_percentage / 100:
            final_price = item.get_base_price() * min_price_percentage / 100
        
        item.set_price(final_price)
    
    if item.get_price() <= 0:
        item.set_price(1)