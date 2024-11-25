# main.py
def max_pizza_slices(N):
    if N < 0:
        raise ValueError("Количество разрезов не может быть отрицательным")
    return (N * (N + 1)) // 2 + 1
