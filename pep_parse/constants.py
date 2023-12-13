from pathlib import Path

PEP_DOMAIN = 'peps.python.org'
PEP_URLS = f'https://{PEP_DOMAIN}/'
BASE_DIR = Path(__file__).resolve().parent.parent / 'results'
STRF_FORMAT = '%Y-%m-%d_%H-%M-%S'
