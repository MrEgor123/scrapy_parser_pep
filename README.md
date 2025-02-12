## Scrapy parser pep

## Описание
Парсер на базе фреймворка Scrapy, предназначенный для сбора данных документов PEP с сайта https://www.python.org/.
Парсер собирает номера, имена и статусы всех PEP и сохраняет их в csv-файл.
Парсер сохраняет сводку по статусам PEP, сколько найдено документов в каждом статусе.

## Стек использованных технологий
- Python 3.11
- Scrapy 2.12

## Как развернуть проект
```
git clone https://github.com/MrEgor123/scrapy_parser_pep
```

## Команды запуска
Создать вирутальное окружение:
```
python3 -m venv venv
```
Активировать виртуальное окржуение (Windows / Linux):
```
venv\Scripts\activate.bat
```
```
source venv/bin/activate
```
Установить зависимости:
```
pip install -r requirements.txt
```
Запуск парсера:
```
scrapy crawl pep
```

## Как посмотреть результат
Для просмотра результат нужно перейти в директорию results/

## Автор
- Чарушин Егор
- Профиль GitHub: https://github.com/MrEgor123
