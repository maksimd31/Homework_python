import time


class MyString(str):
    """
    MyString trending class
    """

    def __new__(cls, name):
        """
        Append trending name
        :param name: append name human
        """
        instance = super().__new__(cls, name)
        instance.name = name
        instance.time = time.time()
        return instance


p1 = MyString('Grosha')
print(p1)
print(p1.time)


# TASK2
class Archive:
    """
    Class trending Archive
    """
    my_llist_str = []
    my_list_int = []

    def __init__(self, my_int, my_str):
        """
        Append List string or Integer
        :param my_int: list integer
        :param my_str: list string
        """

        self.my_int = my_int
        self.my_str = my_str
        self.my_llist_str.append(my_str)
        self.my_list_int.append(my_int)

    def __str__(self):
        return f'List int {self.my_list_int}\nList str {self.my_llist_str}'

    def __repr__(self):
        return f'{self.my_llist_str =} {self.my_list_int}'


pp = Archive(1, '333')
print(f'{pp.my_list_int =} {pp.my_llist_str =}')
pp2 = Archive(2, '33esfdc')
print(print(f'{pp2.my_list_int =} {pp2.my_llist_str =}'))
print(repr(pp))
print(repr(pp2))
