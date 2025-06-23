class SocialNetwork:
    """
    Базовый класс для социальных сетей.

    Атрибуты:
        name (str): Название социальной сети.
        _users (int): Количество пользователей (инкапсулирован — не редактируется напрямую).

    Причина инкапсуляции: изменение числа пользователей должно происходить через методы.
    """

    def __init__(self, name: str, users: int) -> None:
        self.name = name
        self._users = users

    def __str__(self) -> str:
        return f"Социальная сеть: {self.name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, users={self._users})"

    def get_users_count(self) -> int:
        """
        Возвращает текущее количество пользователей.

        :return: число пользователей
        """
        return self._users

    def add_users(self, count: int) -> None:
        """
        Увеличивает количество пользователей.

        :param count: количество новых пользователей
        :raises ValueError: если count отрицательный
        """
        if count < 0:
            raise ValueError("Нельзя добавить отрицательное количество пользователей.")
        self._users += count


class Facebook(SocialNetwork):
    """
    Класс для Facebook. Расширяет базовый класс SocialNetwork.

    Атрибуты:
        region (str): Регион, в котором работает экземпляр платформы.
    """

    def __init__(self, name: str, users: int, region: str) -> None:
        super().__init__(name, users)
        self.region = region

    def __str__(self) -> str:
        return f"Facebook ({self.region}) — {self.get_users_count()} пользователей"

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name={self.name!r}, users={self._users}, "
                f"region={self.region!r})")

    def add_users(self, count: int, verified: bool = True) -> None:
        """
        Перегруженный метод добавления пользователей.

        Причина перегрузки:
        В Facebook мы хотим учитывать только проверенных пользователей.

        :param count: количество новых пользователей
        :param verified: учитывать ли только проверенных пользователей
        :raises ValueError: если count отрицательный
        """
        if not verified:
            print("Добавление не прошедших проверку пользователей запрещено.")
            return
        super().add_users(count)
