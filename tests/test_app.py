import pytest
from app import valid_grade, valid_component, jami_ball


@pytest.mark.parametrize("x, kutilgan", [
    (0, True), (100, True), (55, True),
    (-1, False), (101, False), (True, False), ("90", False), (90.5, False),
])
def test_valid_grade(x, kutilgan):
    assert valid_grade(x) is kutilgan


def test_component_chegaralari():
    assert valid_component("JN", 30)
    assert not valid_component("JN", 31)
    assert valid_component("ON", 0)
    assert not valid_component("YN", 51)


def test_noma_lum_tur():
    with pytest.raises(ValueError):
        valid_component("XX", 10)


def test_jami_ball():
    assert jami_ball(25, 15, 40) == 80


def test_jami_ball_xato():
    with pytest.raises(ValueError):
        jami_ball(35, 10, 10)
