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