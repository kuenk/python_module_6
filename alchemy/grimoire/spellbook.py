def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    ing = validate_ingredients(ingredients)
    if "INVALID" in ing:
        return (f"Spell rejected: {spell_name} ({ing})")
    else:
        return (f"Spell recorded: {spell_name} ({ing})")
