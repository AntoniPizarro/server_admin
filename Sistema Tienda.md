# Sistema Tienda
## Dinero
- Efectivo
    - Item del juego modificado con algún identificador (ej /give @r stick{my_custom_value:123}).

- Virtual
    - Scoreboard (4.294.967.295 valores).

## Compra en la WEB
Pasos:
1. El usuario inicia sesión utilizando su nombre de usuario en el server.
2. Se le enviará un código de confirmación por el chat de 7 dígitos.
3. Se cargará la información del usuario: dinero en la cuenta, otras compras, inventario actual...
4. Añadirá los items que desea comprar a la cesta.
5. Antes de realizar la compra se le enviará un segundo código de confirmación antes de comprar.
6. Aquí puede suceder una de dos cosas (por decidir)
    - El usuario recibirá los items directamente en el inventario.
    - El usuario recibirá un "ticket" para invocar un cofre que caiga desde arriba.