from Mage import Mage
from Rogue import Rogue


class ShadowCaster(Mage, Rogue):
    """
    Represents a ShadowCaster character in an RPG game.

    A ShadowCaster inherits from both Mage and Rogue.
    Their attack power combines magical scaling with critical strike potential.
    """

    def __init__(self, name, magic, critical_chance, damage=50):
        """
        Initializes a ShadowCaster with name, magic, critical chance, and shared base damage.

        Attributes are manually assigned using each parent's name-mangled format
        to ensure compatibility with inherited attack methods.

        :param name: str - The name of the character
        :param magic: int - Magical power used by Mage's attack logic
        :param critical_chance: float - Probability (0–1) of a critical strike from Rogue logic
        :param damage: int - Shared base damage used by both parent classes (default is 50)
        """
        self.__name = name
        self._Mage__magic = magic
        self._Mage__damage = damage
        self._Rogue__critical_chance = critical_chance
        self._Rogue__damage = damage

    def attack(self):
        """
        Calculates the total attack value for the ShadowCaster.

        The result is the sum of:
        - Mage.attack(): damage * (magic / 10)
        - Rogue.attack(): either damage or damage^2 depending on critical roll

        :return: float - The combined attack value from both parents
        """
        return Mage.attack(self) + Rogue.attack(self)