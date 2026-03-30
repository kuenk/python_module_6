from . import elements


def healing_potion() -> str:
    return (f"Healing potion brewed with "
            f"{elements.create_fire()} and "
            f"{elements.create_water()}")


def strength_potion():
    return (f"Strengh potion brewed with "
            f"{elements.create_earth()} and "
            f"{elements.create_fire()}")


def invisibility_potioin():
    return (f"Invisibility potion brewed with "
            f"{elements.create_air()} and "
            f"{elements.create_water()}")


def wisdom_potion():
    return (f"Wisdom potion brewed with "
            f"{elements.create_water()}, "
            f"{elements.create_fire()}")
