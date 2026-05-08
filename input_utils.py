def get_text(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Vstup nesmie byť prázdny.")

def get_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if min_val is not None and value < min_val:
                print(f"Hodnota musí byť aspoň {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Hodnota môže byť najviac {max_val}.")
                continue
            return value
        except ValueError:
            print("Neplatné číslo. Skús znova.")

def get_float(prompt: str, min_val: float = None, max_val: float = None) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if min_val is not None and value < min_val:
                print(f"Hodnota musí byť aspoň {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Hodnota môže byť najviac {max_val}.")
                continue
            return value
        except ValueError:
            print("Neplatné číslo. Skús znova.")