import json
import pandas as pd
from chunk import gerar_chunks

#Pega cada arquivo e separa em suas partes
def ler_paginas(caminho_arquivo):
    paginas_por_documento = {}
    arquivo = open(caminho_arquivo, "r", encoding="utf-8")

    for linha in arquivo:
        linha = linha.strip()
        if not linha:
            continue

        dado = json.loads(linha)
        doc_id = dado["document_id"]

        if doc_id not in paginas_por_documento:
            paginas_por_documento[doc_id] = []

        paginas_por_documento[doc_id].append({
            "page": dado["page"],
            "text": dado["text"],
        })

    arquivo.close()
    return paginas_por_documento

# Manda para gerar chunks
def construir_silver(caminho_entrada, caminho_saida):
    paginas_por_documento = ler_paginas(caminho_entrada)
    todos_os_chunks = []

    for doc_id in paginas_por_documento:
        paginas_do_doc = paginas_por_documento[doc_id]
        chunks_do_doc = gerar_chunks(doc_id, paginas_do_doc)

        for chunk in chunks_do_doc:
            todos_os_chunks.append(chunk)

    tabela = pd.DataFrame(todos_os_chunks)
    tabela["n_chars"] = tabela["text"].str.len()
    tabela.to_parquet(caminho_saida, index=False)

    print("Chunks gerados:", len(tabela))
    print("Salvo em:", caminho_saida)


if __name__ == "__main__":
    construir_silver(
        caminho_entrada="data/interim/paginas_limpas.jsonl",
        caminho_saida="data/silver/chunks.parquet",)