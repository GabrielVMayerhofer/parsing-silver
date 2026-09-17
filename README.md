# Parsing Silver

Pipeline para extração, limpeza e divisão em chunks de documentos PDF.

## Estrutura

```text
data/
├── seed_v0/                    # PDFs originais
├── metadata/                   # Metadados dos documentos
├── raw_silver/                 # Textos extraídos
├── clean_silver/               # Textos limpos
└── silver/                     # Chunks gerados

src/parsing/
├── builder_silver.py           # Executa src/parsing/
└── parsing/
    ├── extract.py              # Extração
    ├── clean.py                # Limpeza
    └── chunk.py                # Chunking
```

## Execução

Na raiz do projeto:

```bash
python3 data/chunks_silver/builder_silver.py
```

O pipeline segue:

```text
PDF → Extração → Limpeza → Chunks
```

Os documentos processados são identificados pelo `document_id` presente em `data/metadata/documents.csv`.