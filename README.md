# Асинхронный Парсер Документов PEP
## Описание проекта:
Проект позволяет изучить возможности асинхронного фреймворка для парсинга данных Scrapy. В проекте создан парсер, который собирает информацию о статусах PEP и их количестве с [сайта Python](https://www.python.org/), сохраняя всю собранную информацию в файлы CSV.
Парсер собирает следующую информацию:
- **pep**: Информация о PEP, включая номер, статус и авторов.
- **status_summary**: Количество каждого статуса и общая сумма всех статусов TOTAL.

#### Стек проекта: Python 3, Scrapy.
## Установка и запуск проекта:
- Клонируйте проект:
  ```
  git clone git@github.com:aten88/scrapy_parser_pep.git
  ```
- Создайте и активируйте виртуальное окружение:
   - Windows:
     ```
     python -m venv venv` и `venv\Scripts\activate
     ```
   - Linux/MacOS:
     ```
     python -m venv venv` и `source venv/bin/activate
     ```
- Обновите pip и установите зависимости:
  ```
  python -m pip install --upgrade pip && pip install -r requirements.txt
  ```
- Запуск парсера:
  ```
  scrapy crawl pep
  ```
### Автор: Алексей Тен.
