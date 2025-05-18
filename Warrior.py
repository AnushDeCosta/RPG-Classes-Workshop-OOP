class Warrior:
    """
    Represents a Warrior character in an RPG game.

    A Warrior's attack power is calculated by adding their strength to their base damage.
    """

    def __init__(self, name, strength, damage=20):
        """
        Initializes a Warrior with a name, strength stat, and base damage.

        :param name: str - The name of the Warrior
        :param strength: Int - The strength value that boosts attack power
        :param damage: Int - The base damage value (default is 20)
        """
        self.__name = name
        self.__strength = strength
        self.__damage = damage

    def attack(self):
        """
        Calculates the Warrior's attack value.

        The attack is calculated as:
        damage + strength

        :return: float - The total attack value
        """
        return self.__damage + self.__strength