# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
#    Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
#    Достаточно вернуть один допустимый вариант.
#    *Верните все возможные варианты комплектации рюкзака.

max_weight = 20
items = {"палатка": 15, "нож": 0.6, "стол": 10, "стул": 5, "спальный мешок": 1.5, "Топор": 2, "продукты": 2}

backpack = []

for item, weight in items.items():  # такой записью иы сразу возвращаем список пар и записываем их в разные переменные
    # далее необходимо сравнить мх и узнать сколько влезет в рюкзак.
    if weight <= max_weight:
        backpack.append(item)
        max_weight -= weight

print(backpack)
