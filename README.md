# web-scraping-com-scrapy


Para executar a extração dos dados, executar o comando abaixo dentro da pasta "src"

```bash
scrapy crawl mercadolivre -o ../data/data.jsonl
```

Para rodar o PANDAS, executar o comando abaixo na pasta principal do projeto

```bash
python src/transformacao/main.py
```
