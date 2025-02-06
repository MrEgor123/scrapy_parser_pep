from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

PEP_SPIDER_URL = 'peps.python.org'

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent

RESULTS = 'results'
RESULTS_DIR = BASE_DIR / RESULTS

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

LOG_FILE = RESULTS_DIR / 'parser.logs'
LOG_FORMAT = '%(asctime)s - [%(levelname)s] - %(message)s'
LOG_LEVEL = 'DEBUG'
LOG_FILE_APPEND = True

FILE_FORMAT = 'csv'

SUMMARY_NAME = 'status_summary'
SUMMARY_TABLE_HEADER = ('Status', 'Quantity')
SUMMARY_TABLE_BOTTOM = 'Total'

PEP_NAME = 'pep'
# Важно: используем двойной % чтобы после обработки f‑строкой получился шаблон %(time)s,
# который затем Scrapy подставит своим механизмом (например, "pep_2025-02-06T15-40-31+00-00.csv")
#PEP_FILE_NAME = f'{PEP_NAME}_%%(time)s.{FILE_FORMAT}'

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

if not RESULTS_DIR.exists():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
