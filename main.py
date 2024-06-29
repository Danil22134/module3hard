data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_):
    summa = 0
    if isinstance(data_, str):
        return len(data_)
    elif isinstance(data_, (int, float)):
        return data_
    elif isinstance(data_, (list, tuple, set)):
        for item in data_:
            summa += calculate_structure_sum(item)
    elif isinstance(data_, dict):
        for key, value in data_.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
    return summa


result = calculate_structure_sum(data_structure)
print(result)
