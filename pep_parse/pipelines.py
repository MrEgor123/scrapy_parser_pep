import csv
import datetime as dt
from collections import defaultdict

import pep_parse.settings as settings


class PepParsePipeline:
    """Класс для обработки и сохранения результатов парсинга."""

    def __init__(self):
        self.results_dir = settings.BASE_DIR / settings.RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        """Метод вызывается при запуске паука."""
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        """Метод обработки каждого элемента."""
        self.statuses[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        """Метод вызывается при закрытии паука, сохраняет результаты в CSV."""
        now = dt.datetime.now()
        now_formatted = now.strftime(settings.DATETIME_FORMAT)

        file_name = (
            f'{settings.SUMMARY_NAME}_{now_formatted}.'
            f'{settings.FILE_FORMAT}'
        )

        file_path = self.results_dir / file_name

        with open(file_path, mode='w', encoding='utf-8') as csvfile:
            csv.writer(
                csvfile,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE,
            ).writerows([
                settings.SUMMARY_TABLE_HEADER,
                *self.statuses.items(),
                (settings.SUMMARY_TABLE_BOTTOM, sum(self.statuses.values())),
            ])
