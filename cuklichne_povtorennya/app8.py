def rozrahynok_kincevoi_ocinku(oсinka_za_praktuky, ocinka_za_ekzamen):
    if oсinka_za_praktuky >= 5 and ocinka_za_ekzamen >= 5:
        kinceva_ocinka = 0.3 * oсinka_za_praktuky + 0.7 * ocinka_za_ekzamen
    else:
        kinceva_ocinka = min(oсinka_za_praktuky, ocinka_za_ekzamen)

    return kinceva_ocinka


def main():
    ocinky = []

    while True:
        oсinka_za_praktuky = input("Оцінка за практичні заняття: ")

        if oсinka_za_praktuky == "-1":
            break

        ocinka_za_ekzamen = input("Оцінка за екзамен: ")

        try:
            oсinka_za_praktuky = float(oсinka_za_praktuky)
            ocinka_za_ekzamen = float(ocinka_za_ekzamen)

            if not (0 <= oсinka_za_praktuky <= 10 and 0 <= ocinka_za_ekzamen <= 10):
                print("Помилка: Оцінки повинні бути в межах від 0 - 10.")
                continue

            kinceva_ocinka = rozrahynok_kincevoi_ocinku(oсinka_za_praktuky, ocinka_za_ekzamen)
            ocinky.append(kinceva_ocinka)

            print(f"Кінцева оцінка: {kinceva_ocinka:.2f}")

        except ValueError:
            print("Помилка: Будь ласка, введіть числові значення.")

    if ocinky:
        serednya_ocinka = sum(ocinky) / len(ocinky)
        print(f"Середня оцінка по групі: {serednya_ocinka:.2f}")
    else:
        print("Оцінки не були введені.")

if __name__ == "__main__":
    main()