def print_ascii_tablucya():
    print("Десяткова | Двійкова | Вісімкова | Шістнадцяткова | Символ")
    print("-" * 50)

    for code in range(128):  # Перебір кодів
        char = chr(code)  # Символ за кодом
        binary = bin(code)  # в 2ічну
        octal = oct(code)  # в 8мкову
        hexadecimal = hex(code)  # в 16кову

        print(f"{code:^9} | {binary:^8} | {octal:^8} | {hexadecimal:^14} | {char:^6}")#Виведення рядка таблиці


if __name__ == "__main__":
    print_ascii_tablucya()