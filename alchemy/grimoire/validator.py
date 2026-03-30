def validate_ingredients(ingredients: str) -> str:
    element = ["fire", "water", "air", "earth"]
    ing = ingredients.split()
    for item in ing:
        if item not in element:
            return (f"{ingredients} - INVALID")
    return (f"{ingredients} - VALID")
