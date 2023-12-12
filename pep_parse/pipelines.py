from collections import defaultdict
import csv
import datetime as dt
import os

from pep_parse.constants import BASE_DIR


class PepParsePipeline:
    """ Пайплайн для создания результатирующего файла """
    def open_spider(self, spider):
        """ Метод создания итогового словаря """
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        """ Метод подсчета статусов """
        status = item['status']
        self.status_counts[status] += 1
        return item

    def close_spider(self, spider):
        """ Метод создания итогового файла """
        now = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"status_summary_{now}.csv"
        filepath = BASE_DIR / filename
        os.makedirs(BASE_DIR, exist_ok=True)
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Статус', 'Количество']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            total_count = 0
            for status, count in self.status_counts.items():
                writer.writerow({'Статус': status, 'Количество': count})
                total_count += count

            writer.writerow({'Статус': 'Total', 'Количество': total_count})
