import pytest
from pizza_slices import max_pizza_slices  # Импортируем функцию из файла pizza_slices.py

def test_max_pizza_slices():
    # Тесты для базовых значений
    assert max_pizza_slices(0) == 1, "При 0 разрезах должна быть 1 часть"
    assert max_pizza_slices(1) == 2, "При 1 разрезе должно быть 2 части"
    assert max_pizza_slices(2) == 4, "При 2 разрезах должно быть 4 части"
    assert max_pizza_slices(3) == 7, "При 3 разрезах должно быть 7 частей"
    assert max_pizza_slices(4) == 11, "При 4 разрезах должно быть 11 частей"
    
    # Проверка для произвольного значения
    assert max_pizza_slices(10) == 56, "При 10 разрезах должно быть 56 частей"
    
    # Проверка на большом значении
    assert max_pizza_slices(1000) == 500501, "При 1000 разрезах должно быть 500501 частей"
