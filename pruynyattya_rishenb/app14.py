def sobaka_to_lyduna_years(sobaka_years):
    if sobaka_years < 0:
        return "Помилка: Введено від'ємне число. Будь ласка, введіть додатне число."
    elif sobaka_years <= 2:
        return sobaka_years * 10.5  # Перші 2 роки собаки = 21 рік людини
    else:
        return 21 + (sobaka_years - 2) * 4  # кожні +2 роки собаки = 4 роки людини


def main():
    try:
        pes_years = float(input("Введіть кількість років життя собаки: "))

        lyduna_years = sobaka_to_lyduna_years(pes_years)

        if isinstance(lyduna_years, str):
            print(lyduna_years)
        else:
            print(f"{pes_years} років життя собаки ≈ {lyduna_years} років життя людини.")
    except ValueError:
        print("Помилка: Будь ласка, введіть числове значення.")


if __name__ == "__main__":
    main()