Feature: Тестирование неактуального протокола транспортного уровня
  Проверка поддержки протоколов tls версии 1.1, 1, ssl версии 2, 3 веб-ресурсом

  Scenario: Сканирование веб-ресурса на предмет поддержки протоколов tls 1.1, 1, ssl 2, 3
    Given Запустить проверку инструментом sslyze
    Then Получено подтверждение об отсутствии поддержки перечисленных протоколов