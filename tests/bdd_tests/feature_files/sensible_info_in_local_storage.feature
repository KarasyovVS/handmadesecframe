Feature: Проверка локального хранилища
  Проверка локального хранилища на отсутствие введеной чувствительной информации

  Scenario: Проверка локального хранилища
    Given Авторизоваться в системе под определенной ролью, заполнить формы приложения чувствительной информацией
    Then Проверить содержимое локального хранилища на отсутствие чувствительной информации