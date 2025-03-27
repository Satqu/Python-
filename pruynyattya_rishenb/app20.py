from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class Tarif:
    stala_cina: float
    mb_scho_vhodyatb: int
    doplata_za_mb: float
    nastypnuy_tarif: Optional[int] = None

TARIFU: Dict[int, Tarif] = {
    1000: Tarif(stala_cina=20, mb_scho_vhodyatb=1000, doplata_za_mb=0.05, nastypnuy_tarif=2000),
    2000: Tarif(stala_cina=35, mb_scho_vhodyatb=2000, doplata_za_mb=0.04, nastypnuy_tarif=5000),
    5000: Tarif(stala_cina=85, mb_scho_vhodyatb=5000, doplata_za_mb=0.02)
}


def pidrahynok_cheky(tarif: int, used_mb: int) -> float:
    if used_mb < 0:
        raise ValueError("Кількість витрачених мегабайтів не може бути від'ємною.")

    if tarif not in TARIFU:
        raise ValueError("Невірний тариф. Будь ласка, оберіть 1000, 2000 або 5000.")

    tarif_data = TARIFU[tarif]
    extra_mb = max(used_mb - tarif_data.mb_scho_vhodyatb, 0)  # Позатарифні МБ (не менше 0)
    totalbnuy_rahynok = tarif_data.stala_cina + extra_mb * tarif_data.doplata_za_mb

    return totalbnuy_rahynok

def kraschuy_rahynok(teperishniy_tarif: int, vukorustani_mb: int) -> Optional[int]:

    if teperishniy_tarif not in TARIFU:
        return None

    teperishniy_tarif_data = TARIFU[teperishniy_tarif]
    nastypnuy_tarif = teperishniy_tarif_data.nastypnuy_tarif

    if nastypnuy_tarif and nastypnuy_tarif in TARIFU:
        next_tariff_data = TARIFU[nastypnuy_tarif]
        teperishnuy_rahynok = pidrahynok_cheky(teperishniy_tarif, vukorustani_mb)
        maubytnya_cina = pidrahynok_cheky(nastypnuy_tarif, vukorustani_mb)

        if maubytnya_cina < teperishnuy_rahynok:
            return nastypnuy_tarif

    return None

def main():
    print("Програма для розрахунку вартості інтернет-тарифу.")

    try:
        tarif = int(input("Введіть тариф (1000, 2000 або 5000): "))
        vukorustani_mb = int(input("Введіть кількість витрачених мегабайтів: "))

        vsya_cina = pidrahynok_cheky(tarif, vukorustani_mb)
        print(f"Загальна вартість: {vsya_cina:.2f} грн.")

        kraschuy_tarif = kraschuy_rahynok(tarif, vukorustani_mb)
        if kraschuy_tarif:
            better_cost = pidrahynok_cheky(kraschuy_tarif, vukorustani_mb)
            print(f"Якби ви перейшли на тариф {kraschuy_tarif}, ви б заплатили {better_cost:.2f} грн.")
    except ValueError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Сталася неочікувана помилка: {e}")


if __name__ == "__main__":
    main()