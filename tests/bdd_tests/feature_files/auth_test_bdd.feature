Feature: Тестирование аутентификации
  Проверка корректности работы подсистемы аутентификации в системе

  Scenario: Аутентификация в системе
    Given Открыть страницу аутентификации, ввести логин, пароль и нажать на кнопку входа
    Then Должна открыться страница успешной аутентификации или страница ввода второго фактора