import random

"""Создать класс Car: id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер.
Функции-члены реализуют запись и считывание полей (проверка корректности), вывода возраста машины.
Создать список объектов. Вывести: a)список автомобилей заданной марки
 b) список автомобилей заданной модели, которые эксплуатируются больше n лет;"""
class Car:
    id=0
    brend="No"
    model="no"
    dateOfIssue="no"
    color="no"
    price="no"
    registrationNumber="no"

    __count = 0

    """def __init__(self,id):
        self.id=int(id)
        print("Id присвоенно автоматически и = " + str(id) )
        self.brend=str(input("Марка"))
        self.model =str(input("Модель"))
        self. dateOfIssue=str(input("год выпуска"))
        self.price = str(input("Цена в формате XXXX.XX"))
        self.registrationNumber=str(input("Рег номер"))
        # какую тут проверку сделать хз
        Car.count+=1"""

    def __init__(self, id,brend,model,dateOfIssue,color, price,registrationNumber):
        self.id=id
        self.dateOfIssue=str(dateOfIssue)
        self.brend=brend
        self.model=model
        self.dateOfIssue=dateOfIssue
        self.color=color
        self.price=price
        self.registrationNumber=registrationNumber
        Car.__count += 1

    def __str__(self):
        return str(self.id) + " " + str(self. brend) + " " + str(self.model)

    def get_oldOfCar(self):
           print("возраст машины " + str(2021 - int(self.dateOfIssue)))
           return 0

    def get_Brand(self):
        return self.brend

    def get_id(self):
        return self.id
    def get_model(self):
        return self.model
    def get_dataOfIssure(self):
        return self.dateOfIssue
    def get_color(self):
        return self.price
    def get_price(self):
        return self.price
    def get_registerationNumber(self):
        return self.registrationNumber



AllCarS =[Car(1,"Audi","Q5","2019","Gray","32000","7472ae-7"),
          Car(2, "Acura", "f16", "2019", "Green", "27000", "8882ae-7"),
          Car(3,"Bmw","320","2012","Black","20000","8478ae-7"),
          Car(4, "Ford", "Transit", "2020", "White", "26000", "(6466ao-7",),
          Car(5, "Lada", "2111", "1986", "Red", "10000", "656e-7"),
          Car(6, "Lada", "2107", "2010", "Blue", "8000", "7772ae-7"),
          Car(7, "Lada", "2101", "1973", "Red", "800", "3215pp-7"),
          Car(8, "Mazda", "6", "2014", "red", "11200", "5642ae-7"),
          Car(9, "Mazda", "rx-7", "2007", "gray", "3000", "3172ae-7")]


def search_identical_brend():
    serch_brend=str(input("Введите искомый бренд:\n"))
    for i in range(len(AllCarS)-1):
        brend=AllCarS[i].get_Brand()
        if(brend == serch_brend):
            print("_____________________________________________________________")
            print(f'Id: {AllCarS[i].get_id()}')
            print(f'Brand: {AllCarS[i].get_Brand()}')
            print(f'Model: {AllCarS[i].get_model()}')
            print(f'Дата выпуска: {AllCarS[i].get_dataOfIssure()}')
            print(f'Стоимость: {AllCarS[i].get_price()}')
            print(f'цвет: {AllCarS[i].get_color()}')
            print(f'Регистрационный номер: {AllCarS[i].get_registerationNumber()}')
            print("_____________________________________________________________")

def search_Old_model():
    serch_model=str(input("Введите искомую модель:\n "))
    serch_year=str(input("Введите год с которого модель эксплуатируется:\n "))
    for i in range(len(AllCarS)):
        model=AllCarS[i].get_model()
        yearr = AllCarS[i].get_dataOfIssure()
        if(model == serch_model and serch_year>yearr ):
            print("_____________________________________________________________")
            print(f'Id: {AllCarS[i].get_id()}')
            print(f'Brand: {AllCarS[i].get_Brand()}')
            print(f'Model: {AllCarS[i].get_model()}')
            print(f'Дата выпуска: {AllCarS[i].get_dataOfIssure()}')
            print(f'Стоимость: {AllCarS[i].get_price()}')
            print(f'цвет: {AllCarS[i].get_color()}')
            print(f'Регистрационный номер: {AllCarS[i].get_registerationNumber()}')
            print("_____________________________________________________________")





menuKey=str(input("Выбирите и введите пункт меню программы:\nЦифра 1 для вывода списока автомобилей заданной марки\n"
                  "Цифра 2 для вывода списока автомобилей заданной модели, которые эксплуатируются больше n лет\n"
                  "Цифра 3 для вывода возраста машины.\n"
                  ))
if(int(menuKey)==1):search_identical_brend()
if(int(menuKey)==2):search_Old_model()
if (int(menuKey) == 3):
    numofcar=str(input("Введите id машины для определения ее возраста"))
    print(AllCarS[numofcar].get_oldOfCar())
else  :print("End of programm")
#print("End of programm")



