from collections import defaultdict
import csv
import datetime as dt
import os

from pep_parse.constants import BASE_DIR, STRF_FORMAT


class PepParsePipeline:
    """ Пайплайн для создания результатирующего файла """
    def open_spider(self, spider):
        """ Метод создания итогового словаря """
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        """ Метод подсчета статусов """
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        """ Метод создания итогового файла """
        now = dt.datetime.now().strftime(STRF_FORMAT)
        filename = f'status_summary_{now}.csv'
        filepath = BASE_DIR / filename
        os.makedirs(BASE_DIR, exist_ok=True)
        rows_to_write = []
        fieldnames = ['Статус', 'Количество']
        total_count = 0
        for status, count in self.status_counts.items():
            rows_to_write.append({'Статус': status, 'Количество': count})
            total_count += count
        rows_to_write.append({'Статус': 'Total', 'Количество': total_count})
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows_to_write)
