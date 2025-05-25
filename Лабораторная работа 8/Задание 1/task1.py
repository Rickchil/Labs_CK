class ElectronicDevice:
    """Базовый класс для электронных устройств.

    Attributes:
        model (str): Модель устройства
        power_consumption (int): Потребляемая мощность в ваттах
        _manufacturer (str): Производитель (инкапсулирован для защиты)
    """

    def __init__(self, model: str, power_consumption: int, manufacturer: str):
        """Инициализация устройства.

        Args:
            model: Модельное название устройства
            power_consumption: Потребляемая мощность (Вт)
            manufacturer: Производитель устройства
        """
        self.model = model
        self.power_consumption = power_consumption
        self._manufacturer = manufacturer  # Инкапсуляция для защиты бренда

    def get_power_info(self) -> str:
        """Возвращает информацию о потребляемой мощности.

        Returns:
            Строка с описанием мощности
        """
        return f"Потребляемая мощность: {self.power_consumption} Вт"

    def turn_on(self) -> str:
        """Включение устройства.

        Returns:
            Строка-подтверждение включения
        """
        return f"{self.model} включен(а)"

    def __str__(self) -> str:
        """Пользовательское строковое представление."""
        return (f"Устройство {self.model} от {self._manufacturer}. "
                f"{self.get_power_info()}")

    def __repr__(self) -> str:
        """Официальное строковое представление."""
        return (f"ElectronicDevice(model={self.model!r}, "
                f"power_consumption={self.power_consumption!r}, "
                f"manufacturer={self._manufacturer!r})")


class Smartphone(ElectronicDevice):
    """Класс смартфона, наследуется от ElectronicDevice.

    Attributes:
        os (str): Операционная система
        screen_size (float): Диагональ экрана в дюймах
        _imei (str): IMEI устройства (инкапсулирован для безопасности)
    """

    def __init__(
        self,
        model: str,
        power: int,
        manufacturer: str,
        os: str,
        screen_size: float,
        imei: str
    ):
        """Инициализация смартфона.

        Args:
            model: Модель смартфона
            power: Потребляемая мощность (Вт)
            manufacturer: Производитель
            os: Операционная система
            screen_size: Размер экрана (дюймы)
            imei: IMEI номер устройства
        """
        super().__init__(model, power, manufacturer)
        self.os = os
        self.screen_size = screen_size
        self._imei = imei  # Инкапсуляция IMEI для защиты

    def get_os_info(self) -> str:
        """Возвращает информацию об ОС.

        Returns:
            Строка с описанием операционной системы
        """
        return f"Операционная система: {self.os}"

    def turn_on(self) -> str:
        """Перегрузка метода включения с специфичной логикой смартфона.

        Перегружен для отражения дополнительных этапов включения:
        - Инициализация SIM-карты
        - Загрузка ОС
        - Проверка обновлений

        Returns:
            Строка-подтверждение включения смартфона
        """
        return (f"{self.model} загружается... "
                f"Инициализация {self.os}... Готово к использованию!")

    def __str__(self) -> str:
        """Пользовательское строковое представление смартфона."""
        base_info = super().__str__()
        return (f"{base_info}\n"
                f"Смартфон с экраном {self.screen_size}\". "
                f"{self.get_os_info()}")

    def __repr__(self) -> str:
        """Официальное строковое представление смартфона."""
        return (f"Smartphone(model={self.model!r}, "
                f"power_consumption={self.power_consumption!r}, "
                f"manufacturer={self._manufacturer!r}, "
                f"os={self.os!r}, screen_size={self.screen_size!r}, "
                f"imei='***')")


if __name__ == "__main__":
    # Тестирование базового класса
    device = ElectronicDevice("BaseModel-100", 50, "GenericTech")
    print(device)
    print(repr(device))
    print(device.turn_on())

    print("\n" + "=" * 50 + "\n")

    # Тестирование класса-наследника
    phone = Smartphone(
        model="Galaxy S23",
        power=15,
        manufacturer="Samsung",
        os="Android 13",
        screen_size=6.1,
        imei="123456789012345"
    )
    print(phone)
    print(repr(phone))
    print(phone.turn_on())
    print(phone.get_power_info())  # Демонстрация унаследованного метода