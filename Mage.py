class Mage:
    """
    Represents a Mage character in an RPG game.

    A Mage has magical abilities that scale their attack power based on their magic stat.
    """

    MAGIC_MULTIPLIER = 10

    def __init__(self, name, magic, damage=15):
        """
        Initializes a Mage with a name, magic stat, and base damage.

        :param name: str - The name of the Mage
        :param magic: Int - The magic level of the Mage used in attack calculations
        :param damage: Int - The base damage (default is 15)
        """
        self.__name = name
        self.__magic = magic
        self.__damage = damage

    def attack(self):
        """
        Calculates the attack value for the Mage.

        The attack is scaled by the Mage's magic stat using the formula:
        damage * (magic / MAGIC_MULTIPLIER)

        :return: float - The total calculated attack value
        """
        return self.__damage * (self.__magic / Mage.MAGIC_MULTIPLIER)