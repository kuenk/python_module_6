import alchemy
from alchemy.elements import create_fire, create_water

print("=== Sacred Scroll Mastery ===\n")

print("Testint direct module acces:")
print(f"alchemy.elements.create_fire(): "
      f"{alchemy.elements.create_fire()}")
print(f"alchemy.elements.create_water(): "
      f"{alchemy.elements.create_water()}")
print(f"alchemy.elements.create_earth(): "
      f"{alchemy.elements.create_earth()}")
print(f"alchemy.elements.create_air(): "
      f"{alchemy.elements.create_air()}\n")
print("Testint package-level accces (controlled "
      "by __init__.py):")
print(f"alchemy.create_fire(): "
      f"{create_fire()}")
print(f"alchemy.create_water(): "
      f"{create_water()}")
try:
    print(f"alchemy.create_earth(): "
          f"{create_earth()}")
except NameError:
    print("alchemy.create_earth(): "
          "AttributeError - not exposed")
try:
    print(f"alchemy.create_air(): "
          f"{create_air()}\n")
except NameError:
    print("alchemy.create_air(): "
          "AttributeError - not exposed")

print("\nPackage metadata:")
print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")
