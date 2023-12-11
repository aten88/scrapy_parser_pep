BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['name', 'number', 'status'],
        'overwrite': True
    },
    # 'pep_statuses_count.csv': {
    #     'format': 'csv',
    #     'fields': ['status'],
    #     'overwrite': True
    # },
}
