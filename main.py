import pytest


# set: позитивный
def test_set_union():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    assert set1.union(set2) == {1, 2, 3, 4, 5}


# set: негативный
def test_set_remove_non_existing_element():
    sample_set = {1, 2, 3}
    try:
        sample_set.remove(4)
        assert False, "Попытка удалить несуществующий элемент должна вызвать ошибку"
    except KeyError:
        pass


# set: параметризованный
@pytest.mark.parametrize("test_input, expected_output", [
    ([1, 2, 3, 2, 1], {1, 2, 3}),
    ([4, 4, 4, 4, 4], {4}),
    ([], set()),
])
def test_set_uniqueness_simple(test_input, expected_output):
    result = set(test_input)
    assert result == expected_output, f"Ожидался {expected_output}, но получили {result}"


# float: позитивный
def test_float_addition():
    result = 0.1 + 0.2
    assert result - 0.3 < 1e-9


# float: негативный
def test_float_from_invalid_string():
    try:
        float("not_a_number")
        assert False, "Тест не прошел: ожидалось ValueError"
    except ValueError:
        pass


# float: параметризованный
@pytest.mark.parametrize("a, b, expected", [
    (1.5, 0.5, 1.0),
    (2.3, 1.1, 1.2)
])
def test_float_subtraction(a, b, expected):
    result = a - b
    assert result - expected < 1e-9
