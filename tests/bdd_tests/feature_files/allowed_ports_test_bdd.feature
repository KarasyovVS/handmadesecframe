Feature: Сканирование открытых портов
  Проверка соответствия открытых портов только разрешенным портам на веб-ресурсе

  Scenario: Сканирование веб-ресурса на наличие открытых портов
    Given Запустить проверку инструментом nmap
    Then Получено подтверждение о соответствии открытых портов только разрешенным