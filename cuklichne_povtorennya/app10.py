def rozrahynok_chusla_lyna(imei):
    suma = 0

    for i, chuslo in enumerate(imei):
        chuslo = int(chuslo)

        if i % 2 == 1:
            chuslo *= 2
            if chuslo > 9:
                chuslo = chuslo // 10 + chuslo % 10

        suma += chuslo

    chuslo_luna = (10 - (suma % 10)) % 10
    return chuslo_luna


def perevirka_avtentychnosti(imei):
    if len(imei) != 15:
        return False

    imei_bez_luna = imei[:14]

    chuslo_luna = rozrahynok_chusla_lyna(imei_bez_luna)

    return chuslo_luna == int(imei[-1])


def main():

    while True:
        imei = input("Введіть IMEI (15 цифр, який закінчується на 6): ")

        if imei.lower() == "вийти":
            break

        if len(imei) != 15 or not imei.endswith("6"):
            print("Помилка: IMEI має містити 15 цифр і закінчуватися на 6.")
            continue

        if not imei.isdigit():
            print("Помилка: IMEI має містити лише цифри.")
            continue

        if perevirka_avtentychnosti(imei):
            print("IMEI автентичний.")
        else:
            print("IMEI не автентичний.")

if __name__ == "__main__":
    main()