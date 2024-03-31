from coletor import Coletor
from indexador import * # IndexadorUm, IndexadorN
from buscador import Buscador
import streamlit as st

# urls = ['https://sobest.com.br/', 'https://pt.wikipedia.org/wiki/Estomaterapia']

# #coletor = Coletor('estomaterapia')
# coletor = Coletor('estomaterapia', 2) # Opcionalmente, pode-se passar o nível máximo de aprofundamento, max_depth.
# for url in urls:
    # coletor.add_url(url)

# #coletor.extract_information()
# coletor.bfs_extract_information(0)
# coletor.print_results()
# coletor.save_results()

# indexer = Indexador(coletor)
# indexer.inverted_index_generator()
# indexer.update_F()
# indexer.save_index()

st.write('Benvindo(a) ao seu buscador sobre Estomaterapia!')
st.markdown('--------')

query = st.text_input("O que você deseja pesquisar? ")
# query = input("[buscador ] O que você deseja pesquisar? ")

if query or st.button('Buscar'):
    searcher = Buscador("index-estomaterapia.json")
    results = searcher.new_search(query.lower())
    st.write(f"Resultados: ")
    for r in results:
       #print(f"[buscador ] Resultado: {r}")
       st.markdown('- ' + r)