from STORE import *
from . import RCON

MONEY_SYMBOL = "ξ"  # ξ      &xi;    &#958;      xi


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
