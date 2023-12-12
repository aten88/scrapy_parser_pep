АСИНХРОННЫЙ ПАРСЕР ДОКУМЕНТОВ PEP

ОПИСАНИЕ:
Парсер, собирающий информацию о статусах PEP их количества с сайта https://www.python.org/

Вся собранная информация сохраняется в файлы csv:
pep:
  - Информация о PEP: номер, статус, автор-(ы).
status_summary:
  - Количество каждого статуса + общая сумма всех статусов TOTAL.

Технологии которые применялись в создании проекта
Python;
Scrapy.

Запуск парсера
Склонируйте проект:
git clone git@github.com:aten88/scrapy_parser_pep.git

Установите и активируйте виртуальное окружение:
python -m venv venv
(windows) source venv/Scripts/activate
(linux/macos) source venv/bin/activate

Обновите пакетный менеджер PIP и установите зависимости:
python.exe -m pip install --upgrade pip
python -r requirements.txt

Запуск парсера:
В терминале введите команду: scrapy crawl pep

АВТОР:
Алексей Тен
