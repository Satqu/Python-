class Resurs:
    def __init__(self, typ_resursu):
        self.typ_resursu = typ_resursu


class Zavdannya:
    def __init__(self, typ_zavdannya, potribni_resursy):
        self.typ_zavdannya = typ_zavdannya
        self.potribni_resursy = potribni_resursy


def rozpodil(resurs, zavdannya):

    if resurs.typ_resursu not in ["пожежна бригада", "швидка допомога", "поліція"]:
        return "Помилка: невідомий тип ресурсу."

    if zavdannya.typ_zavdannya not in ["пожежа", "злочин", "медична допомога"]:
        return "Помилка: невідома задача."

    if len(zavdannya.potribni_resursy) == 0:
        return "Помилка: задача не потребує ресурсів."

    if resurs.typ_resursu not in zavdannya.potribni_resursy:
        return "Помилка: недостатня кількість ресурсів."

    return f"Ресурс '{resurs.typ_resursu}' успішно призначено для задачі '{zavdannya.typ_zavdannya}'."

testovi_vypadky = [
    {
        "id": 1,
        "opis": "Валідний ресурс і валідна задача з мінімальною кількістю ресурсів",
        "resurs": Resurs("пожежна бригада"),
        "zavdannya": Zavdannya("пожежа", ["пожежна бригада"]),
        "ochikuvany_rezultat": "Ресурс 'пожежна бригада' успішно призначено для задачі 'пожежа'."
    },
    {
        "id": 2,
        "opis": "Невідомий тип ресурсу",
        "resurs": Resurs("неіснуючий тип"),
        "zavdannya": Zavdannya("пожежа", ["пожежна бригада"]),
        "ochikuvany_rezultat": "Помилка: невідомий тип ресурсу."
    },
    {
        "id": 3,
        "opis": "Невідома задача",
        "resurs": Resurs("пожежна бригада"),
        "zavdannya": Zavdannya("неіснуюча задача", ["пожежна бригада"]),
        "ochikuvany_rezultat": "Помилка: невідома задача."
    },
    {
        "id": 4,
        "opis": "Задача не потребує ресурсів",
        "resurs": Resurs("пожежна бригада"),
        "zavdannya": Zavdannya("пожежа", []),
        "ochikuvany_rezultat": "Помилка: задача не потребує ресурсів."
    },

    {
        "id": 5,
        "opis": "Максимальна кількість ресурсів",
        "resurs": Resurs("пожежна бригада"),
        "zavdannya": Zavdannya("велика пожежа", ["пожежна бригада", "швидка допомога", "поліція"]),
        "ochikuvany_rezultat": "Ресурс 'пожежна бригада' успішно призначено для задачі 'велика пожежа'."
    },
    {
        "id": 6,
        "opis": "Нульова кількість ресурсів",
        "resurs": Resurs("пожежна бригада"),
        "zavdannya": Zavdannya("пожежа", []),
        "ochikuvany_rezultat": "Помилка: задача не потребує ресурсів."
    },

    {
        "id": 7,
        "opis": "Недостатня кількість ресурсів",
        "resurs": Resurs("пожежна бригада"),
        "zavdannya": Zavdannya("пожежа", ["швидка допомога"]),
        "ochikuvany_rezultat": "Помилка: недостатня кількість ресурсів."
    }
]

for vypadok in testovi_vypadky:
    rezultat = rozpodil(vypadok["resurs"], vypadok["zavdannya"])
    status = "Пройдено" if rezultat == vypadok["ochikuvany_rezultat"] else "Не пройдено"

    print(f"Тест {vypadok['id']}: {vypadok['opis']}")
    print(f"Очікуваний результат: {vypadok['ochikuvany_rezultat']}")
    print(f"Фактичний результат: {rezultat}")
    print(f"Статус: {status}")
    print("-" * 50)