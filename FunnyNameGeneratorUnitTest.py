import pytest
from main import FunnyNameGenerator


# Тест на проверку работы отката в именах
def test_names_rollback():
    names_rollback_list = []
    generator = FunnyNameGenerator()
    for i in range(1, 2225):
        if i > 7:
            names_rollback_list.pop(0)
        new_value = generator.generate_name().split(" ")[-1]
        assert new_value not in names_rollback_list
        names_rollback_list.append(new_value)


# Тест на проверку работы отката в прилагательных
def test_adjectives_rollback():
    adjectives_rollback_list = []
    generator = FunnyNameGenerator()
    for i in range(1, 2225):
        if i > 7:
            adjectives_rollback_list.pop(0)
        new_value = generator.generate_name().split(" ")[0]
        assert new_value not in adjectives_rollback_list
        adjectives_rollback_list.append(new_value)


# Тест на отсутствие повторяющихся значений
def test_combined_names_rollback():
    combined_names_rollback_list = []
    generator = FunnyNameGenerator()
    for i in range(1, 2225):
        if i > 7:
            combined_names_rollback_list.pop(0)
        new_value = generator.generate_name()
        assert new_value not in combined_names_rollback_list
        combined_names_rollback_list.append(new_value)


# Тест на корректную работу с явным обозначением гендера
def test_with_specified_gender():
    generator = FunnyNameGenerator()
    for _ in range(1, 300):
        new_value = generator.generate_name(gender="female").split(" ")[0]
        assert new_value[-2:] in ["ая", "ая"]
    for _ in range(1, 300):
        new_value = generator.generate_name(gender="male").split(" ")[0]
        assert new_value[-2:] not in ["ая", "ая"]
    with pytest.raises(ValueError):
        generator.generate_name(gender="invalid")
