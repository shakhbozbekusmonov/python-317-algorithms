# Warmup 1 by Coding Bat

# sleepIn(false, false) → true
# sleepIn(true, false) → false
# sleepIn(false, true) → true
def sleep_in(weekday: bool, vacation: bool) -> bool:
    return not (weekday and not vacation)


# monkeyTrouble(true, true) → true
# monkeyTrouble(false, false) → true
# monkeyTrouble(true, false) → false
def monkey_trouble(a_smile: bool, b_smile: bool) -> bool:
    return not (a_smile and not b_smile or not a_smile and b_smile)


# sumDouble(1, 2) → 3
# sumDouble(3, 2) → 5
# sumDouble(2, 2) → 8
def sum_double(a: int, b: int) -> int:
    if a == b:
        return (a + b) * 2
    else:
        return a + b

# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0


def diff21(n: int) -> int:
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2

# parrotTrouble(true, 6) → true
# parrotTrouble(true, 7) → false
# parrotTrouble(false, 6) → false


def parrot_trouble(talking: bool, hour: int) -> bool:
    return talking and (hour < 7 or hour > 20)

# makes10(9, 10) → true
# makes10(9, 9) → false
# makes10(1, 9) → true


def makes10(a: int, b: int) -> bool:
    return a == 10 or b == 10 or a + b == 10


# nearHundred(93) → true
# nearHundred(90) → true
# nearHundred(89) → false
def near_hundred(n: int) -> bool:
    return abs(100 - n) <= 10 or abs(200 - n) <= 10

# posNeg(1, -1, false) → true
# posNeg(-1, 1, false) → true
# posNeg(-4, -5, true) → true


def pos_neg(a: int, b: int, negative: bool) -> bool:
    if a > 0 > b and not negative:
        return True
    elif a < 0 < b and not negative:
        return True
    elif a < 0 and b < 0 and negative:
        return True
    else:
        return False


# notString("candy") → "not candy"
# notString("x") → "not x"
# notString("not bad") → "not bad
def not_string(str: str) -> str:
    if str.startswith("not"):
        return str
    else:
        return "not " + str

# missingChar("kitten", 1) → "ktten"
# missingChar("kitten", 0) → "itten"
# missingChar("kitten", 4) → "kittn"
def missing_char(str: str, n: int) -> str:
    return str[:n] + str[n + 1:]

# front3("Java") → "JavJavJav"
# front3("Chocolate") → "ChoChoCho"
# front3("abc") → "abcabcabc"
def front3(str: str) -> str:
    return str[:3] * 3

# backAround("cat") → "tcatt"
# backAround("Hello") → "oHelloo"
# backAround("a") → "aaa"
def back_around(str: str) -> str:
    return str[:-1] + str + str[:-1]

# or35(3) → true
# or35(10) → true
# or35(8) → false
def or35(n: int) -> bool:
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False

# front22("kitten") → "kikittenki"
# front22("Ha") → "HaHaHa"
# front22("abc") → "ababcab"
def front22(str: str) -> str:
    if len(str) > 2:
        return str[:2] + str + str[:2]
    else:
        return str[:len(str)] + str + str[:len(str)]

# startHi("hi there") → true
# startHi("hi") → true
# startHi("hello hi") → false
def start_hi(str: str) -> bool:
    return str.startswith("hi")


# icyHot(120, -1) → true
# icyHot(-1, 120) → true
# icyHot(2, 120) → false
def icy_hot(a: int, b: int) -> bool:
    if (a < 0 and b >= 100) or (a > 100 and b < 0):
        return True
    else:
        return False

# in1020(12, 99) → true
# in1020(21, 12) → true
# in1020(8, 99) → false
def in1020(a: int, b: int) -> bool:
    if 10 < a < 20 or 10 < b < 20:
        return True
    else:
        return False

