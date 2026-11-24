"""USMS: baholarni tekshirish funksiyalari (5-laboratoriya)."""

MAX_BALL = {"JN": 30, "ON": 20, "YN": 50}


def valid_grade(x):
    """Umumiy baho 0..100 oralig'idagi butun son bo'lishi kerak (bool emas)."""
    return isinstance(x, int) and not isinstance(x, bool) and 0 <= x <= 100


def valid_component(turi, ball):
    """JN (0-30), ON (0-20), YN (0-50) ballarini tekshiradi; bool qaytaradi."""
    if turi not in MAX_BALL:
        raise ValueError(f"Noma'lum baho turi: {turi}")
    return valid_grade(ball) and ball <= MAX_BALL[turi]


def jami_ball(jn, on, yn):
    """Uchta komponent yig'indisi; noto'g'ri qiymatda ValueError."""
    for turi, b in (("JN", jn), ("ON", on), ("YN", yn)):
        if not valid_component(turi, b):
            raise ValueError(f"{turi} uchun noto'g'ri ball: {b}")
    return jn + on + yn
"""USMS: baholarni tekshirish funksiyalari (5-laboratoriya)."""

MAX_BALL = {"JN": 30, "ON": 20, "YN": 50}


def valid_grade(x):
    """Umumiy baho 0..100 oralig'idagi butun son bo'lishi kerak (bool emas)."""
    return isinstance(x, int) and not isinstance(x, bool) and 0 < x <= 100


def valid_component(turi, ball):
    """JN (0-30), ON (0-20), YN (0-50) ballarini tekshiradi."""
    if turi not in MAX_BALL:
        raise ValueError(f"Noma'lum baho turi: {turi}")
    return valid_grade(ball) and ball <= MAX_BALL[turi] or ball == 0


def jami_ball(jn, on, yn):
    """Uchta komponent yig'indisi; noto'g'ri qiymatda ValueError."""
    for turi, b in (("JN", jn), ("ON", on), ("YN", yn)):
        if not valid_component(turi, b):
            raise ValueError(f"{turi} uchun noto'g'ri ball: {b}")
    return jn + on + yn
