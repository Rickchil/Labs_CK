def calculate_survival_months(
        money_capital: float,
        salary: float,
        spend: float,
        increase: float
) -> int:
    """
    Рассчитывает количество месяцев, которое можно прожить без долгов,
    используя текущую подушку безопасности с учётом роста цен.

    :param money_capital: Начальная подушка безопасности
    :param salary: Ежемесячная зарплата
    :param spend: Траты в первый месяц
    :param increase: Ежемесячный рост цен
    :return: Количество месяцев без долгов
    """
    months = 0
    current_spend = spend

    while True:
        # Рассчитываем доступный бюджет (зарплата + остаток подушки)
        available_budget = salary + money_capital

        # Если расходы превышают доступный бюджет - прекращаем расчёт
        if current_spend > available_budget:
            break

        # Корректируем подушку безопасности
        deficit = current_spend - salary
        if deficit > 0:
            money_capital -= deficit

        months += 1

        # Увеличиваем расходы на следующий месяц (кроме первого месяца)
        if months > 0:
            current_spend *= (1 + increase)

    return months


# Исходные параметры
INITIAL_CAPITAL = 20000  # Начальная подушка безопасности
MONTHLY_SALARY = 5000    # Ежемесячная зарплата
INITIAL_SPEND = 6000     # Траты в первый месяц
PRICE_INCREASE = 0.05    # Ежемесячный рост цен

# Расчёт и вывод результата
survival_months = calculate_survival_months(
    money_capital=INITIAL_CAPITAL,
    salary=MONTHLY_SALARY,
    spend=INITIAL_SPEND,
    increase=PRICE_INCREASE
)

print(f"Количество месяцев без долгов: {survival_months}")
