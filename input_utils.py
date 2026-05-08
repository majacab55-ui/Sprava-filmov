ERROR_EMPTY = "Vstup nesmie byť prázdny."
ERROR_NUMBER = "Neplatné číslo. Skús znova."
ERROR_MIN = "Hodnota musí byť aspoň {min_val}."
ERROR_MAX = "Hodnota môže byť najviac {max_val}."


def get_text(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(ERROR_EMPTY)


def get_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    while True:
        try:
            value = int(input(prompt).strip())

            if min_val is not None and value < min_val:
                print(ERROR_MIN.format(min_val=min_val))
                continue

            if max_val is not None and value > max_val:
                print(ERROR_MAX.format(max_val=max_val))
                continue

            return value

        except ValueError:
            print(ERROR_NUMBER)


def get_float(prompt: str, min_val: float = None, max_val: float = None) -> float:
    while True:
        try:
            value = float(input(prompt).strip())

            if min_val is not None and value < min_val:
                print(ERROR_MIN.format(min_val=min_val))
                continue

            if max_val is not None and value > max_val:
                print(ERROR_MAX.format(max_val=max_val))
                continue

            return value

        except ValueError:
            print(ERROR_NUMBER)