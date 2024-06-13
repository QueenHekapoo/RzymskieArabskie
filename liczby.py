class LiczbaRzymska:
    roman_numerals = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    def __init__(self, value):
        if isinstance(value, str):
            self.value = self.roman_to_int(value)
        elif isinstance(value, int):
            self.value = value
        else:
            raise TypeError("Wartość musi być liczbą.")

    @staticmethod
    def roman_to_int(s):
        i, num = 0, 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in LiczbaRzymska.roman_numerals:
                num += LiczbaRzymska.roman_numerals[s[i:i+2]]
                i += 2
            else:
                num += LiczbaRzymska.roman_numerals[s[i]]
                i += 1
        return num

    def int_to_roman(self, num):
        result = ""
        for roman, value in sorted(LiczbaRzymska.roman_numerals.items(), key=lambda t: t[1], reverse=True):
            while num >= value:
                result += roman
                num -= value
        return result

    def __str__(self):
        return f"{self.int_to_roman(self.value)} ({self.value})"

    def __int__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __add__(self, other):
        return LiczbaRzymska(self.value + other.value)

    def __iadd__(self, other):
        self.value += other.value
        return self

    def __contains__(self, item):
        return item in self.int_to_roman(self.value)

    def __len__(self):
        return len(self.int_to_roman(self.value))

    def __mul__(self, other):
        return LiczbaRzymska(self.value * other.value)

    def __sub__(self, other):
        result = self.value - other.value
        if result <= 0:
            raise ValueError("Wynik jest liczbą mniejszą od zera.")
        return LiczbaRzymska(result)

def get_liczba_rzymska(prompt):
    while True:
        value = input(prompt)
        try:
            if value.isdigit():
                return LiczbaRzymska(int(value))
            else:
                return LiczbaRzymska(value)
        except (ValueError, TypeError):
            print("Nieprawidłowa wartość. Spróbuj ponownie.")

print("Wprowadź dwie liczby rzymskie lub arabskie:")

a = get_liczba_rzymska("Podaj pierwszą liczbę: ")
b = get_liczba_rzymska("Podaj drugą liczbę: ")

print(f"a: {a}")
print(f"b: {b}")

print("Operacje:")
print(f"a == b: {a == b}")
print(f"a < b: {a < b}")
print(f"a > b: {a > b}")
print(f"a + b: {a + b}")

print(f"'V' in a: {'V' in a}")
print(f"'X' in a: {'X' in a}")
print(f"'L' in a: {'L' in a}")

a += b
print(f"a += b: {a}, b: {b}")

print(f"len(a): {len(a)}")

print("Operacje na dodatkowych liczbach:")
c = LiczbaRzymska(3)
d = LiczbaRzymska(8)

print(f"c: {c}")
print(f"d: {d}")
print(f"c * d: {c * d}")

try:
    print(f"d - c: {d - c}")
    print(f"c - d: {c - d}")
except ValueError as e:
    print(e)
