Feature: Проверка сертификата веб-ресурса
  Проверка удостоверяющего центра и срока действия сертификата

  Scenario: Сканирование веб-ресурса для получения информации о сертификате
    Given Запустить проверку инструментом nmap
    Then Получено подтверждение, что сертификат выпустил одобренный Центр сертификации и срок действия сертификата не истек