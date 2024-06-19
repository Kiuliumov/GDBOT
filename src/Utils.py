import secrets

class Utils:


    @staticmethod
    def generate_random_hex_int() -> int:
        random_int = secrets.randbelow(0xFFFFFF + 1)
        return random_int

