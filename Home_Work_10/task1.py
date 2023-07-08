# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и
# параметры для этого типа. Внутри класса создайте экземпляр на основе переданного
# типа и верните его из класса-фабрики.

from task5 import Birds, Fish, Mammals, Animals


class Fabric:
    def __init__(self, obj_class, *args, **kwargs):
        self.obj_class = obj_class
        if self.obj_class == 'Birds':
            self.object = Birds(*args, **kwargs)
        elif self.obj_class == 'Fish':
            self.object = Fish(*args, **kwargs)
        elif self.obj_class == 'Mammals':
            self.object = Mammals(*args, **kwargs)
        else:
            self.object = Animals(*args, **kwargs)


dog = Fabric('Mammals', False, 'Собака', True)
print(f'Название: {dog.object.name}, хвост: {dog.object.tail}, спячка: {dog.object.specific()}')

swan = Fabric('Birds', 4, 'Лебедь', True)
print(f'Название: {swan.object.name}, хвост: {swan.object.tail}, длина крыла: {swan.object.specific()}')

shark = Fabric('Fish', 15, 'Акула', True)
print(f'Название: {shark.object.name}, хвост: {shark.object.tail}, глубина обитания: {shark.object.specific()}')

viper = Fabric('Reptile', 'Гадюка', True)
print(f'Название: {viper.object.name}, хвост: {viper.object.tail}')
