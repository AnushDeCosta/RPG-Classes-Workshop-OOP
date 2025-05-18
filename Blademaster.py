from Rogue import Rogue
from Warrior import Warrior


class BladeMaster(Rogue, Warrior):
    """
    Represents a BladeMaster character in an RPG game.

    A BladeMaster inherits from both Rogue and Warrior.
    Their attack power is a combination of critical strike potential and brute strength.
    """

    def __init__(self, name, strength, critical_chance, damage=40):
        """
        Initializes a BladeMaster with name, strength, critical chance, and shared base damage.

        Attributes are manually assigned using each parent's name-mangled format
        to ensure compatibility with inherited attack methods.

        :param name: str - The name of the character
        :param strength: int - Physical power used by Warrior's attack
        :param critical_chance: float - Probability (0–1) of a critical strike from Rogue logic
        :param damage: int - Shared base damage used by both parent classes (default is 40)
        """
        self.__name = name
        self._Warrior__strength = strength
        self._Warrior__damage = damage
        self._Rogue__critical_chance = critical_chance
        self._Rogue__damage = damage

    def attack(self):
        """
        Calculates the total attack value for the BladeMaster.

        The result is the sum of:
        - Warrior.attack(): damage + strength
        - Rogue.attack(): either damage or damage^2 depending on critical roll

        :return: float - The combined attack value from both parents
        """
        return Warrior.attack(self) + Rogue.attack(self)
