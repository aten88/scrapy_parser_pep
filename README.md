# Асинхронный Парсер Документов PEP

Этот парсер собирает информацию о статусах PEP и их количестве с [сайта Python](https://www.python.org/), сохраняя всю собранную информацию в файлы CSV.

## Описание

Парсер собирает следующую информацию:
- **pep**: Информация о PEP, включая номер, статус и авторов.
- **status_summary**: Количество каждого статуса и общая сумма всех статусов TOTAL.

## Технологии

Этот проект создан с использованием Python и фреймворка Scrapy.

## Установка и Запуск

1. Клонируйте проект: `git clone git@github.com:aten88/scrapy_parser_pep.git`
2. Создайте и активируйте виртуальное окружение:
   - Windows: `python -m venv venv` и `venv\Scripts\activate`
   - Linux/MacOS: `python -m venv venv` и `source venv/bin/activate`
3. Обновите pip и установите зависимости: `python -m pip install --upgrade pip && pip install -r requirements.txt`
4. Запуск парсера: `scrapy crawl pep`

## Автор

**Алексей Тен**
