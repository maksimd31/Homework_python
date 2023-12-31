# Шпаргалка: Работа с модулями в Python
## Особенности импорта объектов в проект в Python

В Python модуль - это файл, содержащий определения функций, классов и других объектов, которые могут быть использованы в других программах.

Для импорта модуля в Python используется ключевое слово `import` и название модуля. Например, для импорта модуля `math` необходимо выполнить следующую команду:

```
import math

```

После этого, все объекты, определенные в модуле `math`, будут доступны в текущей программе через префикс `math.`. Например, для использования функции `sqrt` из модуля `math` необходимо написать следующую команду:

```
import math

x = math.sqrt(25)

```

Можно импортировать отдельные объекты из модуля, используя ключевое слово `from`. Например, для импорта только функции `sqrt` из модуля `math` необходимо выполнить следующую команду:

```
from math import sqrt

x = sqrt(25)

```

## Встроенные модули и возможности по созданию своих модулей и пакетов в Python

Python содержит множество встроенных модулей, которые могут быть использованы в программах без дополнительной установки. Некоторые из наиболее часто используемых встроенных модулей:

- `math` - математические функции
- `random` - генерация случайных чисел
- `datetime` - работа с датами и временем
- `os` - функции операционной системы

Также в Python есть возможность создания своих модулей и пакетов. Модуль - это просто файл с расширением `.py`, в котором содержатся определения объектов. Пакет - это директория, содержащая файлы модулей и файл `__init__.py`.

Для использования модуля или пакета в Python, его необходимо импортировать с помощью ключевого слова `import`.

## Модуль random отвечающий за генерацию случайных чисел в Python

Модуль `random` в Python предоставляет функции для генерации псевдослучайных чисел. Некоторые из наиболее часто используемых функций:

- `random()` - возвращает случайное число в диапазоне от 0.0 до 1.0
- `randint(a, b)` - возвращает случайное целое число в диапазоне от a до b включительно
- `choice(seq)` - возвращает случайный элемент из последовательности `seq`
- `shuffle(seq)` - перемешивает элементы в последовательности `seq` в случайном порядке

Например, для генерации случайного числа от 1 до 10 необходимо выполнить следующую команду:

```
import random

x = random.randint(1, 10)

```