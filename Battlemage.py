from Mage import Mage
from Warrior import Warrior


class BattleMage(Mage, Warrior):
    """
    Represents a BattleMage character in an RPG game.

    A BattleMage inherits abilities from both Mage and Warrior.
    Their total attack power is the sum of their magic-based and strength-based attacks.
    """

    def __init__(self, name, strength, magic, damage=30):
        """
        Initializes a BattleMage with name, magic, strength, and shared base damage.

        This constructor manually assigns attributes using each parent's naming convention
        to ensure compatibility with inherited attack methods.

        :param name: str - The name of the character
        :param magic: int - The magical ability value (used by Mage's attack logic)
        :param strength: int - The strength value (used by Warrior's attack logic)
        :param damage: int - The base damage shared between both parent classes (default is 30)
        """
        self.__name = name
        self._Mage__magic = magic
        self._Mage__damage = damage
        self._Warrior__strength = strength
        self._Warrior__damage = damage

    def attack(self):
        """
        Calculates the total attack value for the BattleMage.

        The result is the sum of the Mage's and Warrior's attack logic:
        - Mage: damage * (magic / 10)
        - Warrior: damage + strength

        :return: float - The combined attack value
        """
        return Mage.attack(self) + Warrior.attack(self)
