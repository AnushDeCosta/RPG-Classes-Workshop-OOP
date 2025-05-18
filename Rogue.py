import random


class Rogue:
    """
    Represents a Rogue character in an RPG game.

    A Rogue has a chance to land a critical strike which returns significantly higher damage.
    """

    def __init__(self, name, critical_chance=0.25, damage=10):
        """
        Initializes a Rogue with a name, critical strike chance, and base damage.

        :param name: str - The name of the Rogue
        :param critical_chance: float - The probability (0 to 1) of landing a critical hit
        :param damage: int - The base damage value (default is 10)
        """
        self.__name = name
        self.__critical_chance = critical_chance
        self.__damage = damage

    def attack(self):
        """
        Calculates the Rogue's attack value.

        If a random roll is below the critical chance, returns damage squared.
        Otherwise, returns regular damage.

        :return: int - The total attack value
        """
        roll = random.random()
        if roll < self.__critical_chance:
            return self.__damage ** 2
        else:
            return self.__damage
