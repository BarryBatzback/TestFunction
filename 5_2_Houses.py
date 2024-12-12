
class House:
    def __init__(self, name, floor):
        self.name = name
        self.number_of_floors = floor


    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors: #Если new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "f"Такого этажа в здании '{self.name}' не существует""
            print(f"Такого этажа в здании '{self.name}' не существует")
        else:
            for i in range(1, new_floor + 1): #пробегаемся по этажам от первого до значения new_floor включительно.
                print(i)
        return

    def __len__(self):
        return self.number_of_floors #Возвращаем кол-во этажей в доме

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}" #Выводим принт "Название: <название>, кол-во этажей: <этажи>".



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)

h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)

print(h3)
print(h4)

print(len(h3))
print(len(h4))