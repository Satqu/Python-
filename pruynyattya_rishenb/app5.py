def get_dni_misyacya(misyacb):

    dni_misyacya = {
        "січень": 31,
        "лютий": "28 або 29 днів",
        "березень": 31,
        "квітень": 30,
        "травень": 31,
        "червень": 30,
        "липень": 31,
        "серпень": 31,
        "вересень": 30,
        "жовтень": 31,
        "листопад": 30,
        "грудень": 31
    }

    month = misyacb.lower()

    if month in dni_misyacya:
        return f"У місяці {month} {dni_misyacya[month]} днів."
    else:
        return "Введіть коректну назву."


def main():
    print("Програма для визначення кількості днів у місяці.")

    misyacb_input = input("Введіть назву місяця: ").strip()

    result = get_dni_misyacya(misyacb_input)
    print(result)

if __name__ == "__main__":
    main()