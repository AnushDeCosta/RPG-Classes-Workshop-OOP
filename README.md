# RPG Classes Workshop – OOP Project

![Image](https://github.com/user-attachments/assets/cd72abfe-41f5-440c-8dfa-feba17bcb480)

## Summary
**RPG Classes Workshop** is a Python-based object-oriented program that simulates role-playing game (RPG) characters using core OOP principles including inheritance, encapsulation, polymorphism, and manual multiple inheritance.

The system defines three base character types (`Mage`, `Warrior`, `Rogue`) and three hybrid classes (`BattleMage`, `BladeMaster`, `ShadowCaster`), each with unique attributes and behavior.

## Introduction
This project was developed to reinforce OOP fundamentals as part of the **Week 7 Workshop** for the Bachelor of Data Analytics (XBDA) at the **University of South Australia (UniSA)**. It focuses on:

- Manual implementation of multiple inheritance without `super()`
- Combining behavior from multiple parents through polymorphism
- Encapsulation of class attributes using private variables
- Clean, testable logic in hybrid attack methods

> **Note**: Hybrid classes use direct parent method calls and name mangling to simulate behavior composition.

## Project Features

- **Base Character Classes**:
  - `Mage`: magic-scaled attack
  - `Warrior`: strength-based attack
  - `Rogue`: critical chance attack (randomized)

- **Hybrid Classes**:
  - `BattleMage` = Mage + Warrior → combines both attack styles
  - `BladeMaster` = Warrior + Rogue → brute force with critical hit potential
  - `ShadowCaster` = Mage + Rogue → magical burst damage with crit

### Core Mechanics
- Private attributes using double underscores (`__`) with name mangling
- Hybrid classes manually assign mangled attributes for compatibility
- attack() methods override behavior and return combined results

## Tools
- Python 3.10+
- PyCharm or VSCode
- GitHub for version control and modular development

## Files
```
├── mage.py            # Mage base class
├── warrior.py         # Warrior base class
├── rogue.py           # Rogue base class
├── battlemage.py      # Hybrid: Mage + Warrior
├── blademaster.py     # Hybrid: Warrior + Rogue
├── shadowcaster.py    # Hybrid: Mage + Rogue
├── main.py            # Testing hybrid and base class logic
└── README.md          # Project documentation
```

## Usage
To use and test characters:

```python
from battlemage import BattleMage
from blademaster import BladeMaster
from shadowcaster import ShadowCaster

bm = BattleMage("Arcanus", 10, 100, 1000)
print(bm.attack())  # Expected: 11010

bl = BladeMaster("Thorne", 20, 0.5, 40)
print(bl.attack())

sc = ShadowCaster("Veyra", 30, 0.25, 50)
print(sc.attack())
```

## Sample Output
```
Arcanus the BattleMage dealt 11010.0 damage!
Thorne the BladeMaster dealt 60 or 1600 damage (depending on crit)!
Veyra the ShadowCaster dealt 150.0 or 2500.0 damage!
```

## Concepts Demonstrated
- **Encapsulation** via name-mangled attributes
- **Inheritance** of behaviors across multiple parent classes
- **Polymorphism** through shared `attack()` interface
- **Manual attribute wiring** instead of `super()`

## Future Enhancements
- Add visual interface or CLI interaction
- Introduce additional character archetypes
- Use abstract base class for attack contract

## License
This project is intended for educational purposes only as part of coursework for the **University of South Australia (UniSA)** Bachelor of Data Analytics (XBDA) degree.  
© 2025 Anush De Costa.

## Acknowledgements
Thanks to the teaching team at UniSA for their guidance on object-oriented design, attribute encapsulation, and test-driven development.
