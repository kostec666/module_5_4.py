class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Добавляем название здания в историю
        if args:
            cls.houses_history.append(args[0])
        # Создаем новый экземпляр
        return super(House, cls).__new__(cls)

    def __init__(self, first, second=None, third=None):
        self.name = first
        self.floors = second if second is not None else 0  # По умолчанию 0 этажей, если не передано

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floors}'

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

# Пример выполнения программы:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2
del h3

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

del h1  # Удаляем последний объект



