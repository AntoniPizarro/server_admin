from STORE import *
from . import RCON

MONEY_SYMBOL = "ξ"  # ξ      &xi;    &#958;      xi

# Datos de la moneda
MONEY_MC_ID = "minecraft:emerald"
MONEY_NAME = "Leti"
MONEY_DESCRIPTION = "Moneda de comercio"
MONEY_TOKEN_TAG = "money_token"
MONEY_TOKEN = "6852146"


class MC_Store_XXXX(Store):
    def __init__(self, items, sales=None):
        super().__init__(items, sales)
        self.rcon = RCON(
            server_rcon_ip="161.97.132.162",
            server_rcon_port=33475,
            server_rcon_psw="LHga0WuD",
        )

    def give_money(self, player: str, count: int = 1):
        """
        Da a un jugador una cierta cantidad de dinero.
        """
        if count < 1:
            count = 1

        return self.rcon.command_response(
            "/give "
            + player
            + ' emerald{display:{Name:\'["",{"text":"Leti","italic":false,"color":"dark_green"}]\',Lore:[\'["",{"text":"Moneda de comercio.","italic":false,"color":"#66ff99"}]\']},money:8739} '
            + str(count)
        )

    def check_money(self, player: str, count: int):
        """
        Comprueba que un jugador tiene una cierta cantidad de dinero.
        """
        res = self.rcon.command_response(
            "/data get entity " + player + " Inventory[{tag:{money:8739}}].Count"
        )
        if "No entity was found" in res or "No player was found" in res:
            res = -1
        elif res[: len("Found no elements matching")] == "Found no elements matching":
            res = 0
        else:
            match_money = "has the following entity data: "
            res = res[res.find(match_money) + len(match_money) :]

            while res[-1] not in list("0123456789"):
                res = res[:-1]

            res = int(res)

        return res >= count

    def clear_money(self, player: str, max_count: int = 1):
        """
        Quita del inventario de un jugador una cierta cantidad de dinero.
        """
        if max_count < 1:
            max_count = 1

        return self.rcon.command_response(
            "/clear " + player + " minecraft:emerald{money:8739} " + str(max_count)
        )


class MC_Item(Store_Item):
    def __init__(
        self,
        id: str,
        minecraft_id: str,
        name: str,
        description: str,
        price: int,
        image: str,
        supplier: str,
        labels: list[str] = None,
        stock: int = 0,
        unlimited_stock: bool = False,
    ):
        super().__init__(
            id,
            name,
            description,
            price,
            image,
            supplier,
            labels,
            stock,
            unlimited_stock,
        )
        self.minecraft_id = minecraft_id

    def get_minecraft_id(self) -> str:
        """
        Devuelve el ID de Minecraft del item.
        """
        return self.minecraft_id

    def set_minecraft_id(self, new_minecraft_id) -> None:
        """
        Establece el nuevo ID de Minecraft del item.
        """
        self.minecraft_id = new_minecraft_id

    def get_item_obj(self) -> dict:
        return super().get_item_obj().update({"minecraft_id": self.get_minecraft_id()})


class MC_Money:
    def __init__(
        self,
        minecraft_id: str,
        name: str,
        description: str,
        amount: int,
        money_token: str = MONEY_TOKEN,
    ) -> None:
        self.minecraft_id = minecraft_id
        self.name = name
        self.description = description
        self.amount = amount
        self.money_token = money_token

        if ":" not in self.minecraft_id:
            self.minecraft_id = "minecraft:" + self.minecraft_id

    def get_minecraft_id(self) -> str:
        """
        Devuelve el ID del item de Minecraft para la moneda.
        """
        return self.minecraft_id

    def set_minecraft_id(self, new_minecraft_id: str) -> None:
        """
        Establece el nuevo ID del item de Minecraft para la moneda.
        """
        self.minecraft_id = new_minecraft_id

    def get_name(self) -> str:
        """
        Devuelve el nombre de la moneda.
        """
        return self.name

    def set_name(self, new_name: str) -> None:
        """
        Establece el nuevo nombre de la moneda.
        """
        self.name = new_name

    def get_description(self) -> str:
        """
        Devuelve la descripción de la moneda.
        """
        return self.description

    def set_description(self, new_description: str) -> None:
        """
        Establece la nueva descripción de la moneda.
        """
        self.description = new_description

    def get_amount(self) -> int:
        """
        Devuelve la cantidad de la moneda.
        """
        return self.amount

    def set_amount(self, new_amount: int) -> None:
        """
        Establece la nueva cantidad de la moneda.
        """
        self.amount = new_amount

    def get_money_token(self) -> str:
        """
        Devuelve el token de la moneda.
        """
        return self.money_token

    def set_money_token(self, new_money_token: str) -> None:
        """
        Establece el nuevo token de la moneda.
        """
        self.money_token = new_money_token

    def __repr__(self) -> str:
        """
        Devuelve la representación del comando.
        """
        minecraft_id = self.get_minecraft_id()
        name = self.get_name()
        lore = self.get_description()

        return (
            minecraft_id
            + '{display:{Name:\'["",{"text":"'
            + name
            + '","italic":false,"color":"dark_green"}]\',Lore:[\'["",{"text":"'
            + lore
            + '","italic":false,"color":"#66ff99"}]\']},'
            + MONEY_TOKEN_TAG
            + ':"'
            + self.get_money_token()
            + '"} '
            + str(self.get_amount())
        )


class MC_Store(Store):
    def __init__(
        self,
        name,
        description,
        owner,
        items,
        money,
        unlimited_money=True,
        money_symbology=MONEY_SYMBOL,
    ):
        super().__init__(
            name, description, owner, items, money, unlimited_money, money_symbology
        )

    def give_money(self, player: str, ammount: int = 1):
        """
        Da a un jugador una cierta cantidad de dinero.
        """
        if ammount < 1:
            ammount = 1

        money = MC_Money(MONEY_MC_ID, MONEY_NAME, MONEY_DESCRIPTION, ammount)

        return self.rcon.command_response(f"/give {player} {money}")

    def check_money(self, player: str, ammount: int):
        """
        Comprueba que un jugador tiene una cierta cantidad de dinero.
        """
        # Nos aseguramos de que se pretende comprobar una cantidad positiva
        if ammount < 0:
            ammount = 0

        # Generamos el objeto que representa el dinero
        money = MC_Money(MONEY_MC_ID, MONEY_NAME, MONEY_DESCRIPTION, ammount)

        # Lanzamos el comando para comprobar el inventario en busca de la moneda
        res = self.rcon.command_response(
            "/data get entity "
            + player
            + " Inventory[{tag:{"
            + MONEY_TOKEN_TAG
            + ":"
            + money.get_money_token()
            + "}}].Count"
        )

        if "No entity was found" in res or "No player was found" in res:
            # Si el servidor no devuelve que no se ha encontrado al jugador/entidad,
            # establecemos que res es -1, dando a entender que no se puede comprobar sobre algo o alguien que no existe
            res = -1
        elif res[: len("Found no elements matching")] == "Found no elements matching":
            # Si el jugador/entidad no tiene el dinero en el inventario, establecemos res a 0
            res = 0
        else:
            # Si encuentra coincidencia, nos quedamos con la cantidad que se ha encontrado
            match_money = "has the following entity data: "
            res = res[res.find(match_money) + len(match_money) :]

            while res[-1] not in list("0123456789"):
                res = res[:-1]

            res = int(res)

        # Comparamos la cantidad que se ha encontrado con la que se pretende checkear
        return res >= ammount

    def clear_money(self, player: str, max_ammount: int = 1):
        """
        Quita del inventario de un jugador una cierta cantidad de dinero.
        """
        # Nos aseguramos que almenos quitamos una cantidad de 1
        if max_ammount < 1:
            max_ammount = 1

        # Generamos el objeto que representa el dinero
        money = MC_Money(MONEY_MC_ID, MONEY_NAME, MONEY_DESCRIPTION, max_ammount)

        # Ejecutamos el comando
        command = f'/clear {player} {money.get_minecraft_id()} {{"{MONEY_TOKEN_TAG}":{money.get_money_token()}}} {money.get_amount()}'
        return self.rcon.command_response(command)
