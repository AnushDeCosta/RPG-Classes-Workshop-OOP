from Mage import Mage
from Warrior import Warrior
from Rogue import Rogue
from Battlemage import BattleMage
from Blademaster import BladeMaster
from Shadowcaster import ShadowCaster

# Base class tests
print("=== Base Class Tests ===")
mage = Mage("Gandalf", 50, 15)
print(f"Mage attack: {mage.attack()}")  # Expected: 15 * (50 / 10) = 75.0

warrior = Warrior("Thorin", 40, 20)
print(f"Warrior attack: {warrior.attack()}")  # Expected: 20 + 40 = 60

rogue = Rogue("Loki", 0.5, 10)
print(f"Rogue attack: {rogue.attack()}")  # Expected: 10 or 100 depending on roll

# Hybrid class tests
print("\n=== Hybrid Class Tests ===")
bm = BattleMage("Arcanus", 10, 100, 1000)
print(f"BattleMage attack: {bm.attack()}")  # Expected: Mage(1000*(100/10)) + Warrior(1000+10) = 11010.0

bl = BladeMaster("Thorne", 20, 0.5, 40)
print(f"BladeMaster attack: {bl.attack()}")  # Expected: 40+20 + 40 or 1600 depending on crit

sc = ShadowCaster("Veyra", 30, 0.25, 50)
print(f"ShadowCaster attack: {sc.attack()}")  # Expected: 50*(30/10) + 50 or 2500 depending on crit
