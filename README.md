
# Nero - UCalgary Spider

## Development

Pip is needed to install the following packages:

```
pip install Scrapy
pip install scrapyd
pip install bs4
pip install nameparser
pip install unidecode
pip install xmltodict
pip install htmlmin

pip install pandas

pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_trf
```

## Run

Run a crawler

`scrapy crawl <crawler-name>`

List of crawlers are under directory `nero/spiders`

