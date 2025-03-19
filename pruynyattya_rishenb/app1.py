
def need_set_bydilbnuk(is_vuhidnuy, is_vidpystka):
    if is_vuhidnuy or is_vidpystka:
        return False
    return True

def vvod_dannih(promt):
    while True:
        user_input = input(promt).strip().lower()
        if user_input in ['так', 'ні']:
            return user_input == 'так'
        print("Введіть 'так' або 'ні'")

def main():
    print("Чи треба вмикати будильник:")
    is_vuhidnuy = vvod_dannih("У вас сьогодні вихідний?")
    is_vidpystka = vvod_dannih("У вас сьогодні відпустка?")
    set_bydilbnuk = need_set_bydilbnuk(is_vuhidnuy, is_vidpystka)
    if set_bydilbnuk:
        print("Будильник встановлено")
    else:
        print("Будильник вимкнено")

if __name__ == "__main__":
    main()