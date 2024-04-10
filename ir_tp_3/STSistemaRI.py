from coletor import Coletor
from indexador import *
from buscador import Buscador
import streamlit as st
import re

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

def to_assessment():
    print(f'[to_assessment] {st.session_state.checker}')
    
def type_of_query():
    print(f'[type_of_query]{str(st.session_state.radio)}')
    
def specific_context():
    print(f'[specific_context]{str(st.session_state.context_checker)}')

st.title('SIRIE - Sistema de Recuperação de Informação sobre Enfermagem')
st.write('Benvindo(a) ao seu buscador sobre Enfermagem!')
st.markdown('--------')

contexto = 'enfermagem'
query = st.text_input("O que você deseja pesquisar? ")

with st.sidebar:
    st.sidebar.title("Ferramentas de pesquisa")

    #query_type = 1 # 1 = Interseção; 2 = União.
    query_type_option = st.sidebar.radio("Estratégia de processamento das consultas:",
                                    options=["todas as palavras", "qualquer das palavras"],
                                    captions=["(Interseção)", "(União)"],
                                    on_change=type_of_query,
                                    key="radio")
    if (query_type_option == "todas as palavras"):
        query_type = 1
    else:
        query_type = 2
    
    if st.sidebar.checkbox("Especificar contexto", value=False, on_change=specific_context, key="context_checker"):
        contexto = st.text_input('Contexto específico: ', 'estomaterapia')
    else:
        contexto = 'enfermagem'

    #assessment = True
    assessment = st.sidebar.checkbox("Avaliar o Sistema de RI", value=False, on_change=to_assessment, key="checker")
    
    relevant_urls = st.sidebar.text_area(label="URLs relevantes:")        

st.markdown('--------')
                
relevants = list(relevant_urls.replace('\n','').replace('\t','').replace(' ','').split(sep=','))
#relevants = list(re.split(',| |',relevant_urls)) # usando regex!

if query or st.button('Buscar'):
    searcher = Buscador("index-"+contexto+".json")
    results = searcher.new_search(query.lower(), query_type) # passar o tipo de query!
    st.write(f"{len(results)} resultados encontrados: ")
    for r in results:
       st.markdown('- ' + r)
    if assessment and len(relevants) > 0 and len(results) > 0:
        st.write("Avaliação do Sistema de Recuperação de Informação:")
        st.markdown('- Precisão = ' + str(searcher.precision(relevants, results)))
        st.markdown('- Revocação = ' + str(searcher.recall(relevants, results)))
        #st.write(relevantes)