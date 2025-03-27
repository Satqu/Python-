def desyatkove_do_dviykovogo(q):
    result = ""

    while q > 0:
        r = q % 2
        result = str(r) + result
        q = q // 2

    return result if result else "0"


def golovna():
    try:
        q = int(input("Введіть десяткове число: "))

        dviykovuy_result = desyatkove_do_dviykovogo(q)

        print(f"Двійкове представлення числа {q}: {dviykovuy_result}")
    except ValueError:
        print("Помилка: Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    golovna()