def calculate_money_capital(
    salary: int, spend: int, months: int, increase: float
) -> int:
    """
    Рассчитывает необходимую подушку безопасности для покрытия расходов
    в течение заданного количества месяцев с учётом инфляции.

    :param salary: Ежемесячная зарплата
    :param spend: Траты в первый месяц
    :param months: Количество месяцев для расчёта
    :param increase: Ежемесячный рост цен (в долях)
    :return: Необходимая сумма подушки безопасности
    """
    money_capital = 0  # Изначальная подушка безопасности
    current_spend = spend  # Текущие расходы (с учётом роста цен)

    for month in range(months):
        # Считаем дефицит (разницу между расходами и зарплатой)
        deficit = current_spend - salary
        if deficit > 0:
            money_capital += deficit

        # Увеличиваем расходы на следующий месяц (кроме последнего месяца)
        if month < months - 1:
            current_spend *= 1 + increase

    return round(money_capital)


# Исходные данные
SALARY = 5000  # Ежемесечная зарплата
SPEND = 6000  # Траты в первый месяц
MONTHS = 10  # Период планирования в месяцах
INFLATION = 0.03  # Ежемесячный рост цен

# Расчёт и вывод результата
required_capital = calculate_money_capital(
    salary=SALARY, spend=SPEND, months=MONTHS, increase=INFLATION
)

print(
    f"Подушка безопасности, чтобы протянуть {MONTHS} месяцев без долгов: "
    f"{required_capital}"
)